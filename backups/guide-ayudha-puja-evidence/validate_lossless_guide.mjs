#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";

function usage(message) {
  if (message) console.error(message);
  console.error(
    "Usage: validate_lossless_guide.mjs --data FILE --guide-key KEY " +
      "[--baseline FILE] [--audio-root DIR] [--require-spacing] [--skip-audio] [--require-enrichment] [--evidence-manifest FILE]"
  );
  process.exit(2);
}

function parseArgs(argv) {
  const result = {
    baseline: null,
    audioRoot: null,
    requireSpacing: false,
    skipAudio: false,
  };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--require-enrichment") result.requireEnrichment = true;
    else if (arg === "--require-spacing") result.requireSpacing = true;
    else if (arg === "--skip-audio") result.skipAudio = true;
    else if (["--data", "--guide-key", "--baseline", "--audio-root", "--evidence-manifest"].includes(arg)) {
      const value = argv[index + 1];
      if (!value) usage(`Missing value for ${arg}`);
      index += 1;
      if (arg === "--data") result.data = value;
      else if (arg === "--guide-key") result.guideKey = value;
      else if (arg === "--baseline") result.baseline = value;
      else if (arg === "--evidence-manifest") result.evidenceManifest = value;
      else result.audioRoot = value;
    } else usage(`Unknown argument: ${arg}`);
  }
  if (!result.data || !result.guideKey) usage("Both --data and --guide-key are required");
  return result;
}

function loadGuides(file) {
  const source = fs.readFileSync(file, "utf8");
  const sandbox = { window: {} };
  vm.createContext(sandbox);
  vm.runInContext(source, sandbox, { filename: file, timeout: 5000 });
  const guides = sandbox.window.GUIDES;
  if (!Array.isArray(guides)) throw new Error(`${file} did not populate window.GUIDES`);
  return JSON.parse(JSON.stringify(guides));
}

function findGuide(file, key) {
  const guide = loadGuides(file).find((candidate) => candidate.key === key);
  if (!guide) throw new Error(`Guide ${JSON.stringify(key)} not found in ${file}`);
  if (!Array.isArray(guide.sections)) throw new Error(`Guide ${key} has no sections array`);
  return guide;
}

function withoutBlocks(guide) {
  const copy = structuredClone(guide);
  for (const section of copy.sections) delete section.structuredBlocks;
  return copy;
}

function normalizedWhitespace(text) {
  return String(text ?? "").trim().replace(/\s+/gu, " ");
}

function actionBlocks(guide) {
  return guide.sections.flatMap((section) =>
    section.structuredBlocks.filter((block) => block.kind === "action")
  );
}

function mantraText(guide) {
  return guide.sections
    .flatMap((section) =>
      section.structuredBlocks
        .filter((block) => block.kind === "mantra")
        .map((block) => block.text)
    )
    .join(" ");
}

const args = parseArgs(process.argv.slice(2));
const dataFile = path.resolve(args.data);
const guide = findGuide(dataFile, args.guideKey);
const seenIds = new Set();
const seenSlugs = new Set();
let sourceCharacters = 0;
let mantraBoxes = 0;
let actionBoxes = 0;
let paragraphBreaks = 0;
let audioFiles = 0;

for (const section of guide.sections) {
  if (seenIds.has(section.id)) throw new Error(`Duplicate section id: ${section.id}`);
  if (seenSlugs.has(section.slug)) throw new Error(`Duplicate section slug: ${section.slug}`);
  seenIds.add(section.id);
  seenSlugs.add(section.slug);
  if (typeof section.originalScript !== "string") {
    throw new Error(`Section ${section.id} has no originalScript string`);
  }
  if (!Array.isArray(section.structuredBlocks)) {
    throw new Error(`Section ${section.id} has no structuredBlocks array`);
  }

  const rebuilt = section.structuredBlocks
    .map((block) => {
      if (typeof block.sourceOriginal !== "string") {
        throw new Error(`Section ${section.id} has a block without sourceOriginal`);
      }
      if (block.kind === "mantra") {
        mantraBoxes += 1;
        if (typeof block.text !== "string" || !block.text.trim()) {
          throw new Error(`Section ${section.id} has an empty mantra display`);
        }
        paragraphBreaks += (block.text.match(/\n\n/gu) ?? []).length;
      } else if (block.kind === "action") {
        actionBoxes += 1;
        if (typeof block.sourceRoman !== "string" || !block.sourceRoman.trim()) {
          throw new Error(`Section ${section.id} has an action without sourceRoman`);
        }
        if (typeof block.english !== "string" || !block.english.trim()) {
          throw new Error(`Section ${section.id} has an action without English`);
        }
      } else {
        throw new Error(`Section ${section.id} has unknown block kind ${block.kind}`);
      }
      return block.sourceOriginal;
    })
    .join("");

  if (rebuilt !== section.originalScript) {
    throw new Error(`Section ${section.id} does not reconstruct originalScript exactly`);
  }
  for (let index = 1; index < section.structuredBlocks.length; index += 1) {
    if (
      section.structuredBlocks[index - 1].kind === "mantra" &&
      section.structuredBlocks[index].kind === "mantra"
    ) {
      throw new Error(`Section ${section.id} has adjacent mantra boxes`);
    }
  }
  sourceCharacters += section.originalScript.length;

  if (!args.skipAudio) {
    if (!args.audioRoot) usage("--audio-root is required unless --skip-audio is used");
    const relativeAudio =
      section.audioFile ??
      path.join(guide.audioDir ?? "", `${section.id}-${section.slug}.mp3`);
    const audioPath = path.resolve(args.audioRoot, relativeAudio);
    if (!fs.existsSync(audioPath)) {
      throw new Error(`Missing audio for section ${section.id}: ${audioPath}`);
    }
    audioFiles += 1;
  }
}


function requireText(value, label) {
  if (typeof value !== "string" || !value.trim()) throw new Error(`Missing ${label}`);
}
function lexical(text) { return text.trim().split(/\s+/u).filter(x => !/^[|।॥.,!?;:]+$/u.test(x)); }
if (args.requireEnrichment) {
  if (!args.evidenceManifest) throw new Error("Enriched guides require --evidence-manifest");
  for (const s of guide.sections) {
    for (const field of ["contemplate", "action"]) {
      requireText(s[field], `${field} for section ${s.id}`);
      const evidence = s.enrichmentEvidence?.[field] ?? s.guidanceReferences?.[field];
      if (!Array.isArray(evidence) || !evidence.length || evidence.some(e => !e || typeof e !== "object" || (!e.sourceId && !e.reference))) {
        throw new Error(`Missing ${field} evidence for section ${s.id}`);
      }
    }
    for (const b of s.structuredBlocks.filter(b => b.kind === "mantra")) {
      const lines = b.gloss?.lines?.filter(Boolean);
      const display = b.text.split("\n").filter(x => x.trim());
      if (!lines || lines.length !== display.length) throw new Error(`Incomplete line glosses in ${s.id}`);
      lines.forEach((line, i) => {
        if (line.text !== display[i]) throw new Error(`Gloss line differs from recitation in ${s.id}`);
        requireText(line.meaning, `line meaning in ${s.id}`);
        if (!Array.isArray(line.words) || !line.words.length) throw new Error(`Missing word glosses in ${s.id}`);
        line.words.forEach(w => { requireText(w.text, "gloss token"); requireText(w.meaning, "word meaning"); });
        if (JSON.stringify(line.words.map(w => w.text)) !== JSON.stringify(lexical(line.text))) throw new Error(`Word gloss coverage differs in ${s.id}`);
      });
    }
  }
}
if (args.evidenceManifest) {
  const manifest = JSON.parse(fs.readFileSync(args.evidenceManifest, "utf8"));
  if (!Array.isArray(manifest.sources) || !manifest.sources.length || !Array.isArray(manifest.segments)) throw new Error("Invalid evidence manifest");
  const sources = new Map(), texts = new Map(), last = new Map(), lastRanges = new Map(), mapped = new Map(), ids = new Set();
  for (const source of manifest.sources) {
    if (!source.id || sources.has(source.id) || typeof source.originalScript !== "string" || !source.originalScript.length) throw new Error("Invalid or duplicate source");
    if (source.kind === "text") {
      if (source.durationSeconds !== undefined) throw new Error("Text sources must not invent an audio duration");
    } else if (!Number.isFinite(source.durationSeconds) || source.durationSeconds <= 0) throw new Error("Invalid media duration");
    sources.set(source.id, source); texts.set(source.id, "");
  }
  for (const seg of manifest.segments) {
    const source = sources.get(seg.sourceId);
    if (!seg.id || ids.has(seg.id) || !source || typeof seg.sourceOriginal !== "string") throw new Error(`Invalid segment: ${seg.id}`);
    if (source.kind === "text") {
      const start = seg.startCharacter, end = seg.endCharacter;
      if (!Number.isInteger(start) || !Number.isInteger(end) || start !== (last.get(seg.sourceId) ?? 0) || end <= start || end > source.originalScript.length || source.originalScript.slice(start, end) !== seg.sourceOriginal || seg.start !== undefined || seg.end !== undefined) throw new Error(`Invalid text character range: ${seg.id}`);
      last.set(seg.sourceId, end);
    } else {
    const priorRange = lastRanges.get(seg.sourceId);
    const shared = seg.sharedCaptionCue;
    const explainedOverlap = priorRange && shared && priorRange.sharedCaptionCue &&
      JSON.stringify(shared) === JSON.stringify(priorRange.sharedCaptionCue) &&
      Array.isArray(shared.cueIndices) && shared.cueIndices.length > 0 && shared.cueIndices.every(i => Number.isInteger(i) && i > 0) &&
      Number.isFinite(shared.start) && Number.isFinite(shared.end) && shared.start >= 0 && shared.end <= source.durationSeconds && shared.end > shared.start &&
      seg.start >= priorRange.start && seg.start >= shared.start && priorRange.end <= shared.end;
    if (!seg.id || ids.has(seg.id) || !source || !Number.isFinite(seg.start) || !Number.isFinite(seg.end) || seg.start < 0 || seg.end <= seg.start || seg.end > source.durationSeconds || (seg.start < (last.get(seg.sourceId) ?? 0) && !explainedOverlap) || typeof seg.sourceOriginal !== "string") throw new Error(`Invalid segment or timestamp: ${seg.id}`);
    last.set(seg.sourceId, Math.max(last.get(seg.sourceId) ?? 0, seg.end)); lastRanges.set(seg.sourceId, seg);
    }
    ids.add(seg.id); texts.set(seg.sourceId, texts.get(seg.sourceId) + seg.sourceOriginal);
    const section = guide.sections.find(s => s.id === seg.sectionId);
    if (!section || !Number.isInteger(seg.blockIndex) || !section.structuredBlocks[seg.blockIndex]) throw new Error(`Unmapped segment: ${seg.id}`);
    const key = `${seg.sectionId}:${seg.blockIndex}`, prior = mapped.get(key);
    if (prior && prior.sourceId !== seg.sourceId) throw new Error(`Mixed source block: ${key}`);
    mapped.set(key, {sourceId:seg.sourceId, text:(prior?.text ?? "") + seg.sourceOriginal});
  }
  for (const [id, source] of sources) if (texts.get(id) !== source.originalScript) throw new Error(`Incomplete source reconstruction: ${id}`);
  for (const section of guide.sections) section.structuredBlocks.forEach((b, i) => {
    if (mapped.get(`${section.id}:${i}`)?.text !== b.sourceOriginal) throw new Error(`Block evidence mismatch: ${section.id}:${i}`);
  });
}

if (args.requireSpacing && mantraBoxes > 0 && paragraphBreaks === 0) {
  throw new Error("No blank-line mantra spacing was found");
}

if (args.baseline) {
  const baselineFile = path.resolve(args.baseline);
  const baseline = findGuide(baselineFile, args.guideKey);
  if (JSON.stringify(withoutBlocks(baseline)) !== JSON.stringify(withoutBlocks(guide))) {
    throw new Error("Non-structured guide content differs from the baseline");
  }
  if (JSON.stringify(actionBlocks(baseline)) !== JSON.stringify(actionBlocks(guide))) {
    throw new Error("English action blocks differ from the baseline");
  }
  if (normalizedWhitespace(mantraText(baseline)) !== normalizedWhitespace(mantraText(guide))) {
    throw new Error("Roman mantra characters differ from the baseline beyond whitespace");
  }
}

console.log(
  JSON.stringify(
    {
      guideKey: guide.key,
      sections: guide.sections.length,
      sourceCharacters,
      mantraBoxes,
      actionBoxes,
      paragraphBreaks,
      audioFiles,
      baselineChecked: Boolean(args.baseline),
    },
    null,
    2
  )
);

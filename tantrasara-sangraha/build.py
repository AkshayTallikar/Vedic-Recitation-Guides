#!/usr/bin/env python3
"""Build the source-aligned Tantrasara-Sangraha web reader.

reader-source.json is the exact 401-verse Devanagari text behind the attached
Sarvamula reader export. The older Tantrasara-vivrti edition in text/ch*.md is
used only for its English translations and word/compound explanations. A
global line alignment prevents edition-only verses from entering the reader.
"""

from collections import defaultdict
from difflib import SequenceMatcher
import html
import json
import os
import re
import unicodedata

from indic_transliteration import sanscript


BASE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.join(BASE, "text")
SOURCE = os.path.join(BASE, "reader-source.json")
VERSE_END = re.compile(r"॥\s*([०-९]+)\s*॥")


MANUAL_TRANSLATIONS = {
    (3, (15, 16, 17)): (
        "The navel is one and a half aṅgulas, half an aṅgula deep, round, and turning to the "
        "right; the girth at the middle is forty-two aṅgulas. At the breasts the girth is six "
        "aṅgulas greater. The breadth of the chest is nineteen aṅgulas; the next measure is a "
        "quarter-aṅgula less, and together with the arms one and a half more. The breadth of "
        "the two shoulders is eight aṅgulas each, and their height above the armpit is held to "
        "be seven aṅgulas."
    ),
    (3, (18,)): (
        "The measure of the two hands is declared to be thirty-eight aṅgulas. The girth of the "
        "upper arms is declared to be eighteen aṅgulas; diminishing progressively, at their "
        "ends it is stated to be eight and a half aṅgulas."
    ),
    (3, (26, 27, 28, 29, 30, 31, 32)): (
        "The mouth is four aṅgulas. The lower lip is one and a half barley-corns; the upper lip "
        "one barley-corn; the space above it is like the lower lip. Below the lower lip is one "
        "and a half aṅgulas. Each side of the mouth up to the ear is six aṅgulas; the side of "
        "the nose up to the ear is seven. The nose is one and a quarter aṅgulas high; each "
        "nostril-wing and its middle are half an aṅgula. The nose is a barley-corn in breadth, "
        "and the two eyes span three aṅgulas. An eye is one aṅgula wide when open and half that "
        "when otherwise. The brows are four aṅgulas long and half an aṅgula broad, separate yet "
        "dense; the eyelashes are deep blue-black. The ears are three aṅgulas long and two and "
        "a half broad; with the earrings, the aperture is declared to be the same, and the "
        "ear-tendrils make a breadth of two aṅgulas. The lotus-face is adorned with a thousand "
        "dark curls."
    ),
    (3, (63,)): (
        "Three kiṣkus is remembered as the circular station of Śakra and the other deities. "
        "Then one should construct a well-proportioned pavilion for the installation."
    ),
    (3, (117,)): (
        "Having again made the temple by the very procedure already stated, one should bathe "
        "the Lotus-eyed Lord with twice the magnificence, following the prescribed course, and "
        "then again recite the mantras in their direct order."
    ),
    (3, (118, 119, 120)): (
        "By the very procedure stated, with half that magnificence—or even with only a quarter—"
        "the wise person should bathe Hari as prescribed. By this same procedure, having again "
        "made the temple, one should worship the Lord of the universe while meditating with "
        "devotion as taught. The procession is likewise as before, and so in every festival. "
        "Worship and the offering of bali are always to be performed at festivals according to "
        "the kalaśa procedure; a kalaśa is to follow the festival, and the place and course of "
        "the procession are to be arranged exactly according to the stated procedure."
    ),
    (4, (10,)): (
        "The five limbs are declared as: ‘bhīṣaya’ twice, ‘trāsaya,’ ‘pramardaya,’ then "
        "‘pradhvaṃsaya,’ and ‘rakṣa.’"
    ),
    (4, (11,)): (
        "Bearing the Sun and Moon, the discus and conch, and the treasures named Śaṅkha and "
        "Padma, He is to be contemplated as satisfying us with wealth through His hands, with "
        "Lakṣmī seated on His lap and Himself stationed on Garuḍa’s shoulder. ‘The fierce, the "
        "heroic, the mighty Viṣṇu, blazing and facing every direction, the man-lion, causing "
        "fear, auspicious, the slayer even of Death—I myself bow to Him’: this is Hari’s mantra "
        "of thirty-two syllables."
    ),
    (4, (90,)): (
        "His own name, placed in the dative, preceded by its first letter and joined with "
        "‘namaḥ,’ is the great Dhanvantari mantra, destroyer of the disease of transmigration, "
        "resembling the foremost jewel among all the mantras taught here."
    ),
}


def parse(path):
    blocks = []
    current = None
    buffer = []
    with open(path, encoding="utf-8") as stream:
        for raw in stream:
            line = raw.rstrip("\n")
            if current is None:
                if line.startswith("#H "):
                    blocks.append(("H", line[3:].strip()))
                elif line.startswith("#P "):
                    blocks.append(("P", line[3:].strip()))
                elif line.strip() in ("#V", "#T", "#C", "#CT", "#FN"):
                    current = line.strip()[1:]
                    buffer = []
            elif line.strip() == f"#{current}-END":
                blocks.append((current, "\n".join(buffer).strip()))
                current = None
                buffer = []
            else:
                buffer.append(line)
    if current is not None:
        raise ValueError(f"Unclosed #{current} block in {path}")
    return blocks


def iast(devanagari):
    return sanscript.transliterate(devanagari, sanscript.DEVANAGARI, sanscript.IAST)


def line_units(text):
    text = VERSE_END.sub("॥", text)
    return [part.strip() for part in re.split(r"[।॥]+", text) if part.strip() and part.strip() != "ॐ"]


def normalized(text):
    value = unicodedata.normalize("NFD", iast(text)).lower()
    return re.sub(r"[^a-zāīūṛṝḷḹṅñṭḍṇśṣṃḥ]+", "", value)


def global_alignment(source_lines, edition_lines):
    """Needleman-Wunsch alignment with fuzzy Sanskrit line matching."""
    rows, cols = len(source_lines), len(edition_lines)
    gap = -0.65
    scores = [[0.0] * (cols + 1) for _ in range(rows + 1)]
    back = [[None] * (cols + 1) for _ in range(rows + 1)]
    for row in range(1, rows + 1):
        scores[row][0] = row * gap
        back[row][0] = "source"
    for col in range(1, cols + 1):
        scores[0][col] = col * gap
        back[0][col] = "edition"
    for row in range(1, rows + 1):
        left = normalized(source_lines[row - 1][2])
        for col in range(1, cols + 1):
            ratio = SequenceMatcher(None, left, normalized(edition_lines[col - 1][0])).ratio()
            match_score = 2 * ratio - 0.65 if ratio >= 0.62 else -99
            scores[row][col], back[row][col] = max(
                (scores[row - 1][col - 1] + match_score, "match"),
                (scores[row - 1][col] + gap, "source"),
                (scores[row][col - 1] + gap, "edition"),
            )
    alignment = []
    row, col = rows, cols
    while row or col:
        step = back[row][col]
        if step == "match":
            alignment.append((row - 1, col - 1))
            row -= 1
            col -= 1
        elif step == "source":
            alignment.append((row - 1, None))
            row -= 1
        else:
            alignment.append((None, col - 1))
            col -= 1
    return list(reversed(alignment))


def clean_translation(text):
    value = text.strip()
    if value.startswith('"'):
        value = value[1:]
    value = re.sub(r'"?\s*\((?:\d+)(?:\s*[–-]\s*\d+)?\)', "", value)
    value = re.sub(r"\s*\[The edition[^\]]+\]", "", value)
    return value.strip().strip('"').strip()


def edition_records(chapter):
    blocks = parse(os.path.join(TEXT, f"ch{chapter}.md"))
    records = {}
    lines = []
    for index, (kind, payload) in enumerate(blocks):
        if kind != "V":
            continue
        translation = ""
        commentary = ""
        for next_index in range(index + 1, len(blocks)):
            next_kind, next_payload = blocks[next_index]
            if next_kind == "V":
                break
            if next_kind == "T" and not translation:
                translation = next_payload
            elif next_kind == "CT":
                commentary += (" " if commentary else "") + next_payload
        records[index] = {"translation": translation, "commentary": commentary}
        for unit in line_units(payload):
            lines.append((unit, index))
    return records, lines


def build_groups(chapter_data):
    chapter = chapter_data["number"]
    verses = chapter_data["verses"]
    records, edition_lines = edition_records(chapter)
    source_lines = [
        (verse_index, verse["number"], unit)
        for verse_index, verse in enumerate(verses)
        for unit in line_units(verse["devanagari"])
    ]
    mapping = defaultdict(set)
    unmatched = set()
    for source_index, edition_index in global_alignment(source_lines, edition_lines):
        if source_index is not None and edition_index is not None:
            verse_index = source_lines[source_index][0]
            mapping[verse_index].add(edition_lines[edition_index][1])
        elif source_index is not None:
            unmatched.add(source_lines[source_index][0])

    parents = list(range(len(verses)))

    def find(value):
        if parents[value] != value:
            parents[value] = find(parents[value])
        return parents[value]

    def union(left, right):
        left, right = find(left), find(right)
        if left != right:
            parents[right] = left

    block_to_verses = defaultdict(list)
    for verse_index, block_indexes in mapping.items():
        for block_index in block_indexes:
            block_to_verses[block_index].append(verse_index)
    for verse_indexes in block_to_verses.values():
        for verse_index in verse_indexes[1:]:
            union(verse_indexes[0], verse_index)

    components = defaultdict(list)
    for verse_index in range(len(verses)):
        components[find(verse_index)].append(verse_index)

    groups = []
    for verse_indexes in sorted(components.values(), key=lambda item: item[0]):
        numbers = tuple(verses[index]["number"] for index in verse_indexes)
        block_indexes = sorted(set().union(*(mapping.get(index, set()) for index in verse_indexes)))
        key = (chapter, numbers)
        if key in MANUAL_TRANSLATIONS:
            translation = MANUAL_TRANSLATIONS[key]
            commentary = ""
        else:
            translation = " ".join(
                clean_translation(records[index]["translation"])
                for index in block_indexes if records[index]["translation"]
            ).strip()
            commentary = " ".join(
                records[index]["commentary"] for index in block_indexes if records[index]["commentary"]
            ).strip()
        if not translation:
            raise ValueError(f"No translation for chapter {chapter}, verses {numbers}")
        groups.append({
            "verses": [verses[index] for index in verse_indexes],
            "translation": translation,
            "commentary": commentary,
            "source_unmatched": any(index in unmatched for index in verse_indexes),
        })
    return groups


def esc(text):
    return html.escape(text, quote=True)


def format_devanagari(text):
    return esc(text).replace("। ", "।<br>")


def format_iast(text):
    return esc(text).replace("| ", "|<br>")


def range_label(verses):
    first = verses[0]["number"]
    last = verses[-1]["number"]
    return str(first) if first == last else f"{first}–{last}"


def main():
    source = json.load(open(SOURCE, encoding="utf-8"))
    counts = [len(chapter["verses"]) for chapter in source["chapters"]]
    if counts != [75, 24, 141, 161]:
        raise ValueError(f"Unexpected source counts: {counts}")

    output = [HEAD, COVER]
    group_count = 0
    for chapter in source["chapters"]:
        groups = build_groups(chapter)
        group_count += len(groups)
        output.append(
            f'<section class="chapter" id="ch{chapter["number"]}">'
            f'<h1>Chapter {chapter["number"]}<span>{esc(chapter["title"])}</span></h1>'
        )
        last_topic = None
        for group in groups:
            topic = group["verses"][0]["topic"]
            if topic != last_topic:
                output.append(f'<h2>{esc(topic)}</h2>')
                last_topic = topic
            label = range_label(group["verses"])
            search_text = " ".join(
                [topic, group["translation"]]
                + [verse["devanagari"] + " " + verse["iast"] for verse in group["verses"]]
            )
            output.append(
                f'<article class="translation-unit" id="ch{chapter["number"]}-v{group["verses"][0]["number"]}" '
                f'data-search="{esc(search_text.lower())}">'
                f'<div class="unit-label">Chapter {chapter["number"]} · verse{("s" if len(group["verses"]) > 1 else "")} {label}</div>'
            )
            for verse in group["verses"]:
                output.append(
                    '<div class="verse">'
                    f'<div class="verse-number">{chapter["number"]}.{verse["number"]}</div>'
                    f'<div class="dev">{format_devanagari(verse["devanagari"])}</div>'
                    f'<div class="iast">{format_iast(verse["iast"])}</div>'
                    '</div>'
                )
            label_text = "Exact combined meaning" if len(group["verses"]) > 1 else "Exact English meaning"
            output.append(f'<div class="meaning"><span>{label_text}</span>{esc(group["translation"])}</div>')
            if len(group["verses"]) > 1:
                output.append(
                    '<p class="alignment-note">These verses form one translation unit because the '
                    'commentary edition joins their Sanskrit syntax across different verse boundaries.</p>'
                )
            if group["commentary"]:
                output.append(
                    '<details><summary>Word and compound explanation</summary>'
                    f'<div class="commentary">{esc(group["commentary"])}</div></details>'
                )
            output.append('</article>')
        output.append('</section>')
    output.append(FOOT)
    page = "\n".join(output)
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as stream:
        stream.write(page)
    print(f"wrote index.html: 401 verses in {group_count} source-aligned translation units")


HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Exact Devanagari, IAST, and complete English meaning for all 401 verses of the Sarvamula Tantrasara-Sangraha reader.">
<title>Tantrasāra-Saṅgraha — Exact Verse Translation</title>
<style>
:root{--paper:#fbf6ec;--card:#fffdf8;--ink:#2c2418;--muted:#776a55;--red:#8b2f18;--line:#e5d8c0;--gold:#b58a34}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.6}
.site-nav{position:sticky;top:0;z-index:10;display:flex;gap:15px;align-items:center;justify-content:center;flex-wrap:wrap;padding:10px 16px;background:rgba(255,253,248,.97);border-bottom:1px solid var(--line);backdrop-filter:blur(8px)}
.site-nav a{color:var(--red);font:600 13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;text-decoration:none}.site-nav a:hover{text-decoration:underline}
.shell{max-width:960px;margin:0 auto;background:var(--card);min-height:100vh;padding:0 38px 70px;box-shadow:0 8px 30px rgba(72,42,12,.08)}
.cover{text-align:center;padding:74px 10px 42px;border-bottom:1px solid var(--line)}.cover .dev-title{font-family:"Kohinoor Devanagari","Noto Sans Devanagari",serif;font-size:36px;color:var(--red)}
.cover h1{font-size:30px;margin:10px 0 6px}.cover .byline{font-style:italic;color:#51483a}.cover .promise{max-width:760px;margin:30px auto 12px;font-size:18px}.cover .source-note{max-width:760px;margin:18px auto 0;color:var(--muted);font-size:14px}
.toolbar{position:sticky;top:43px;z-index:8;display:flex;align-items:center;gap:12px;padding:13px 0;background:var(--card);border-bottom:1px solid var(--line)}
.toolbar input{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:#fff;font:15px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.count{white-space:nowrap;color:var(--muted);font:13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.chapter{padding-top:34px}.chapter>h1{text-align:center;color:var(--red);font-size:27px;margin:0 0 28px}.chapter>h1 span{display:block;font-family:"Kohinoor Devanagari","Noto Sans Devanagari",serif;font-size:20px;color:var(--muted);font-weight:normal}.chapter>h2{text-align:center;color:var(--red);font-family:"Kohinoor Devanagari","Noto Sans Devanagari",serif;font-size:18px;font-weight:normal;margin:34px 0 14px}
.translation-unit{margin:0 0 24px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 2px 10px rgba(72,42,12,.04)}.unit-label{padding:8px 14px;background:#f4ead8;color:var(--red);font:700 12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.35px;text-transform:uppercase}
.verse{position:relative;padding:18px 20px 17px;background:#fbf8f1;border-bottom:1px solid #eee4d2}.verse-number{position:absolute;right:14px;top:12px;color:#aa9a7d;font:12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.dev{font-family:"Kohinoor Devanagari","Devanagari Sangam MN","Noto Sans Devanagari",serif;font-size:20px;line-height:1.8;padding-right:36px}.iast{font-size:16px;font-style:italic;color:#655a4c;margin-top:7px;line-height:1.65;padding-right:36px}
.meaning{padding:17px 20px;font-size:16px}.meaning>span{display:block;margin-bottom:7px;color:var(--red);font:700 12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.45px;text-transform:uppercase}.alignment-note{margin:0;padding:0 20px 15px;color:var(--muted);font-size:13px;font-style:italic}
details{border-top:1px solid var(--line)}summary{cursor:pointer;padding:12px 20px;color:var(--red);font:600 13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.commentary{padding:0 20px 18px;color:#473d30;font-size:14px}
footer{text-align:center;color:var(--muted);font-size:13px;padding:38px 0 0}.hidden{display:none!important}
@media(max-width:680px){.shell{padding:0 14px 45px;box-shadow:none}.site-nav{gap:11px}.toolbar{top:74px}.cover{padding:42px 4px 30px}.cover .dev-title{font-size:28px}.cover h1{font-size:24px}.dev{font-size:18px;padding-right:25px}.iast{font-size:15px;padding-right:25px}.verse,.meaning{padding-left:15px;padding-right:15px}}
@media print{body{background:#fff}.site-nav,.toolbar{display:none}.shell{max-width:none;padding:0;box-shadow:none}.translation-unit{break-inside:avoid;box-shadow:none}.chapter{break-before:page}.cover{break-after:page}details{display:none}}
</style></head><body>
<nav class="site-nav" aria-label="Reader navigation"><a href="../index.html">← All guides</a><a href="#ch1">Chapter 1</a><a href="#ch2">Chapter 2</a><a href="#ch3">Chapter 3</a><a href="#ch4">Chapter 4</a></nav>
<main class="shell">"""

COVER = """
<section class="cover">
  <div class="dev-title">॥ तन्त्रसारसङ्ग्रहः ॥</div>
  <h1>Tantrasāra-Saṅgraha</h1>
  <div class="byline">of Śrī Ānandatīrtha Bhagavatpādācārya (Madhvācārya)</div>
  <p class="promise">Every one of the attached reader’s 401 numbered verses: exact Devanagari source, IAST, and complete English meaning with no summarization.</p>
  <p class="source-note">The verse divisions and numbering follow the attached Sarvamūla reader exactly: 75 verses in Chapter 1, 24 in Chapter 2, 141 in Chapter 3, and 161 in Chapter 4. The complete Tantrasāra-vivṛti edition supplies the literal translations and optional word/compound explanations. Where that edition joins syntax across different verse boundaries, the affected source verses are kept together as one clearly marked translation unit so every Sanskrit word remains accounted for.</p>
</section>
<div class="toolbar"><input id="search" type="search" placeholder="Search Devanagari, IAST, topic, or English meaning…" aria-label="Search verses"><span class="count" id="count">401 verses</span></div>
"""

FOOT = """
<footer>Source-aligned study edition · 401 numbered verses · no abridgment</footer>
</main>
<script>
(function(){
  const input=document.getElementById('search'), units=[...document.querySelectorAll('.translation-unit')], count=document.getElementById('count');
  input.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();let verses=0;units.forEach(unit=>{const show=!q||unit.dataset.search.includes(q);unit.classList.toggle('hidden',!show);if(show)verses+=unit.querySelectorAll('.verse').length});count.textContent=q?verses+' of 401 verses':'401 verses';document.querySelectorAll('.chapter>h2').forEach(h=>{let n=h.nextElementSibling,show=false;while(n&&!n.matches('h2')){if(n.matches('.translation-unit')&&!n.classList.contains('hidden'))show=true;n=n.nextElementSibling}h.classList.toggle('hidden',!show)})});
})();
</script></body></html>
"""


if __name__ == "__main__":
    main()

# Jyeṣṭhā Devī practice audio workflow

The reviewed manuscript remains the text authority. Never replace it with an
ASR hypothesis. The three instruction-only cards remain text-only; each of the
30 Sanskrit recitation cards receives its own replayable practice clip.

These clips are synthesized, not recordings of a priest. They do not establish
traditional pronunciation, metre, or Vedic svara. Follow a qualified teacher
and your family tradition. Su-śrotā transcripts are diagnostic evidence, not
pronunciation certification.

## Notebook

Saved working notebook: [Jyeshtha Devi Puja – Mantra Audio](https://colab.research.google.com/drive/1-vPiE_fG4e7xA37NvxngffHai3vnxWyo).

The isolated Python 3.10 TTS environment uses the author's official Vāgdhenu
renderer, voice and BigVGAN checkpoints, with 64 synthesis steps, speed 0.90,
CFG 3.0 and seed 50. Use full precision. The mixed-precision/model-reuse
experiment failed audio checks and must not be used. Failed experimental
outputs are quarantined outside the draft directory.

The ASR environment uses NeMo 2.3.2 and the requested
`sushrota_sanskrit_asr_v13b.nemo`. Its original preprocessor, encoder and CTC
tensors are loaded with strict state checks; unused custom RNNT code is not
instantiated. Sanskrit SentencePiece has 256 tokens, offset 4096 and blank 5632.
Decode only this slice. The global-versus-slice log-softmax normalization does
not change its greedy argmax.

Do not Run All blindly: the saved notebook contains earlier failed diagnostic
experiments. Use the validated full-precision renderer and explicit staged
`--only` selections. Let each stage finish and its ZIP transfer complete before
starting another stage; a long foreground cell can delay Colab downloads.
Keep downloaded results before releasing any Colab runtime. After a runtime
replacement, recreate the isolated environments and scripts, preserve the
local checkpoints, and render only unfinished cards. Cell numbers are not a
stable run order.

Downloaded units can also be checked locally with the same strict CTC loader
in an isolated Python 3.10 environment. The tested macOS fallback uses PyTorch
2.5.1, NeMo 2.3.2, NumPy 1.26.4 and SciPy 1.13.1. Install NeMo's Python ASR
dependencies without the unused `texterrors` extension when its native compiler
build is unavailable. This does not replace or modify the CTC tensors.

## Import and validation

Extract the final ZIP into a task-specific temporary folder, then run from the
audio worktree:

```sh
node scripts/install-jyeshtha-audio.mjs /absolute/path/to/extracted-drafts
node scripts/build-jyeshtha-guide.mjs
node scripts/sync-jyeshtha-page.mjs
node scripts/test-jyeshtha-generator.mjs
node scripts/validate-jyeshtha-audio.mjs /absolute/path/to/validate_verse_audio_guide.mjs
```

The installer checks all original-script hashes, mono 24 kHz WAVs, durations,
per-unit reference text and ASR evidence. It creates MP3s and a provenance
manifest. Raw ASR transcripts are retained in the ignored
`build/jyeshtha-audio-work/asr-diagnostics.json`, not the published site.
Inspect high-difference diagnostic units and re-render or flag actual
problems; do not silently change printed Sanskrit.

Saṅkalpa practice reads both printed weekday alternatives separately. During
pūjā choose the actual weekday and complete information omitted by the source
ellipses. It is not a completed, date-specific saṅkalpa.

After import, test first/last playback, three-repeat practice, search, mobile
overflow and browser errors. Preserve all other guide blocks and the altar
illustration. Website publication is a separate release step.

## Model attribution

- [Vāgdhenu](https://huggingface.co/prathoshap/vagdhenu) and
  [official source](https://github.com/prathoshap/vagdhenu): Prathosh A P,
  Indian Institute of Science, Bengaluru.
- [Su-śrotā Sanskrit ASR](https://huggingface.co/prathoshap/sushrota-sanskrit-asr):
  Prathosh A P; derived from AI4Bharat IndicConformer.
- [IndicF5](https://huggingface.co/ai4bharat/IndicF5) and
  [NVIDIA BigVGAN](https://github.com/NVIDIA/BigVGAN): observe the respective
  model and code license terms.

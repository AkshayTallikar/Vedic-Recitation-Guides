# Sadāchāra Saṅgrahaḥ — Shloka Website

A collection of recitable shlokas extracted from **Sadāchāra Saṅgrahaḥ** (Vidwan T. P. Vishnumurthy Acharya, Śrī Raghavendra Trust, Udupi, 2010) — a Mādhva daily-ritual manual — presented as a searchable website with Sanskrit, transliteration, English meaning, ritual context, and chant audio.

> This is distinct from the `../site/` project ("Deva Pūjā Paddhati", built from a YouTube recitation). This folder is the book-extraction → shloka-corpus → website pipeline. Both sites are joined by the landing page at `../index.html`; this site's header has a "← All guides" link back to it.

## What's here

| Path | What it is |
|------|-----------|
| `shlokas/NNN-slug.md` | One markdown file per shloka (the source of truth). **127 files.** |
| `audio/NNN-slug.wav` | Chant audio, 24 kHz mono. Rendered by the vāgdhenu TTS model. |
| `audio_manifest.json` | Generated list of `{id, slug, meter, padas}` fed to the audio renderer. Excludes Vedic sūktas. |
| `index.html` | The website — **self-contained**, generated. Open directly in a browser. |
| `build_site.py` | Builds `index.html` from `shlokas/*.md`. |
| `vagdhenu_batch_audio_kaggle_full.ipynb` | Kaggle notebook that renders all pending audio. |
| `PROGRESS.md` | Extraction tracker: page-by-page status, skip-list, resume points, TODOs. |

## Each shloka file

```markdown
---
id: 1
slug: brahme-muhurte
title: Brāhme Muhūrte
chapter: Prātaḥsnānātpūrvakarma — Rituals before the morning bath
book_page: 1
meter: anuṣṭubh          # MUST be a vāgdhenu bank key (see below)
audio: audio/001-brahme-muhurte.wav
# tts_skip: true         # add for Vedic sūktas — keeps text, excludes from audio
---

# Brāhme Muhūrte
## Sanskrit (Devanagari)
> ब्राह्मे मुहूर्ते चोत्थाय हरिं ध्यायेदतन्द्रितः ॥
## Transliteration (IAST)
> brāhme muhūrte cotthāya hariṃ dhyāyedatandritaḥ ॥
## English meaning
A devotee should arise at *brahmamuhūrta* …
## Action while reciting
Wake during *brahmamuhūrta* …
```

The Devanagari `> ` lines are what get fed to the TTS model (one pada per line; daṇḍas/verse-numbers stripped automatically).

### Valid `meter:` values (vāgdhenu reference bank)
`anuṣṭubh`, `pramāṇikā`, `vasantatilakā`, `upajāti`, `indravajrā`, `upendravajrā`, `vaṃśastha`, `rathoddhatā`, `śālinī`, `indravaṃśā`, `drutavilambita`, `bhujaṅgaprayāta`, `mālinī`, `śārdūlavikrīḍita`, `sragdharā`, `vrutta-1`, `gadya`, `gadya_mbtn`.
A meter outside this list will fail at render. Use `gadya` for prose mantras.

## The pipeline

```
shlokas/*.md  ──build_site.py──▶  index.html        (the website)
      │
      └────────(regen)──────────▶  audio_manifest.json
                                        │
                                   Kaggle notebook (GPU)
                                        │
                                        ▼
                                   audio/*.wav  ──▶ picked up by the site
```

### 1. Build / refresh the website
```bash
python3 build_site.py          # writes index.html
open index.html                # or: python3 -m http.server 8000
```
The site has chapter grouping, live search, a "jump to section" dropdown, and an audio player on every shloka that has a wav.

### 2. Regenerate the audio manifest (after adding/editing shlokas)
The manifest is rebuilt by the same parsing logic the site uses (extract Devanagari padas, skip `tts_skip` files). See the regeneration snippet in `PROGRESS.md`; it also refreshes the embedded manifest inside the Kaggle notebook.

### 3. Render audio (Kaggle, free GPU)
The vāgdhenu model needs a CUDA GPU (not available on this Mac). Use Kaggle:
1. Kaggle account → **Settings → Phone Verification** (required to enable Internet).
2. **Create → New Notebook → File → Import → Upload** `vagdhenu_batch_audio_kaggle_full.ipynb`.
3. Right panel: **Accelerator → GPU T4 x2**, **Internet → On**.
4. **Run All.** Setup ~8 min; ~1–1.5 min per shloka. The render loop **skips wavs that already exist**, so re-running resumes safely.
5. Download `sadachara_audio_all.zip` from the **Output** tab; unzip into `audio/`.

### 4. Integrate & verify rendered audio
After unzipping wavs into `audio/`:
```bash
python3 verify_audio.py --tidy   # moves excluded (tts_skip) wavs to audio/_excluded/, then reports
python3 build_site.py            # rebuild so the site picks up the new audio
```
`verify_audio.py` checks coverage against the manifest and validates each wav (readable, non-empty, 24 kHz mono, sane duration). It reports: valid-present, missing (still to render), flagged, and corrupt/empty. Use `--tidy` when a batch was rendered before a `tts_skip` exclusion was applied — it relocates those wavs so the site doesn't show plain-tone audio for an excluded mantra. (Excluded wavs are *moved, not deleted* — they live in `audio/_excluded/`.)

The site header shows live counts — **N with audio · N to render · N external/text-only** — and the **⏳ To render** filter chip lists exactly what still needs the GPU.

## Scope notes
- **Vedic content is excluded from audio.** The vāgdhenu model mis-voices Vedic svara (udātta/anudātta intonation), so that audio is sourced separately. Two tiers are tagged `tts_skip: true`: (a) full **Vedic sūktas** (Śrī, Puruṣa, Devī, Agni, etc.); (b) **major Vedic mantras** in Sandhyāvandanam — the Gāyatrī, mārjana (*āpo hi ṣṭhā*), the dik/sūrya upasthāna set, *ā kṛṣṇena*, *catvāri śṛṅgā*, Aghamarṣaṇa. Short ritual formulas (ācamana, prāyaścitta jala-mantras, yajñopavīta) are kept renderable in plain tone. All `tts_skip` files keep their text on the site (with a `tts_note` explaining why no model audio); they're excluded from the manifest/render. One verse (121) is `tts_skip` for a different reason — its metre (rucirā) isn't in the voice bank.
- **Sourcing the excluded audio**: see [`EXTERNAL_AUDIO.md`](EXTERNAL_AUDIO.md) — a map of where to find authoritative svara recitations for the 17 excluded Vedic shlokas (most are covered by a single Sandhyāvandanam recitation). Drop a clip at `audio/NNN-slug.wav` and the site plays it (file-existence overrides `tts_skip`).
- The book's recitable shloka corpus (daily ritual, daily japa, the full Lakṣmīnārāyaṇa pūjā paddhati, festival dhyānas, bhojana/tarpaṇa/bedtime/ekādaśī verses) is **complete at 127** (book swept page-by-page p1–290). Text is character-verified (Devanagari↔IAST cross-check, metre syllable-check). Remaining uncaptured material is the excluded Vedic content and procedural prose. See `PROGRESS.md` for the full audit trail.

## Source
Page renders are read from the scanned PDF in `~/Downloads/` (no text layer). Offset: **PDF page index = book page + 24**.

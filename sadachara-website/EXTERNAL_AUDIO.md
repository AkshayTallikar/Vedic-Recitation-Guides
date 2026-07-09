# External audio — sourcing the excluded Vedic shlokas

The vāgdhenu TTS model mis-voices Vedic **svara** (udātta/anudātta/svarita intonation), so 17 Vedic shlokas are marked `tts_skip` and left out of the model render. Their **text stays on the site**; their **audio is to be sourced from authoritative recitations** (your plan). This file is the sourcing map.

> The 18th `tts_skip` file, **121** (*paramātmane satatamekarūpiṇe*), is excluded for a different reason — its metre (rucirā) isn't in the voice bank. It's not Vedic; you could record it plainly or leave it text-only. Not covered below.

## The shortcut: one Sandhyāvandanam recitation covers most of them

13 of the 17 are part of the daily **Sandhyāvandanam** and are recited in sequence in any complete Sandhyāvandanam audio. So you don't need 13 separate clips — one good recitation, segmented, covers: **017, 033, 034, 038, 059, 061, 062, 063, 064, 065, 066, 067, 069, 071**.

**Pick the recitation matching your śākhā.** This is a Mādhva (Udupi) manual; Mādhva families follow either Ṛgveda or (Kṛṣṇa) Yajurveda Sandhyāvandanam depending on lineage — confirm your family's before choosing. Authoritative, freely available:
- **Vaidika Vignanam** — full Sandhyāvandanam with audio, multiple śākhās & scripts: <https://vignanam.org/english/rigveda-sandhya-vandanam.html> (also Yajurveda, Devanāgarī/Kannada/Grantha versions linked on the site).
- **Internet Archive** — text + recitation collections: <https://archive.org/details/RigvedaSandhyavandanamEngV1>
- For a guided recitation to segment from, search a reputable pāṭhaśālā recording (e.g., established Veda-pāṭhaśālā channels) for "Rigveda Sandhyavandanam full" / "Yajur Sandhyavandanam full".

## The 4 standalone sūktas / mantras (separate recordings)

| id | shloka | Vedic source | where to find authoritative svara audio |
|----|--------|--------------|------------------------------------------|
| 079 | *catvāri śṛṅgā* | RV 4.58.3 | part of many Agni-sūkta / Mahānyāsa recitations; Vaidika Vignanam, archive.org |
| 082 | **Śrī Sūkta** | Ṛgveda khila | very widely recorded — Vaidika Vignanam (Sri Suktam, with audio), plus countless pāṭhaśālā recitations |
| 083 | **Devī Sūkta** (Ambhṛṇī) | RV 10.125 | Vaidika Vignanam (Devi Suktam / Ratri Suktam), archive.org |
| 017 | **Aghamarṣaṇa Sūkta** | RV 10.190 (*ṛtaṃ ca satyaṃ ca*) | recited in snāna/Sandhyā; in full Sandhyāvandanam audio, and standalone on Vaidika Vignanam |

## Full list of the 17 Vedic items (for reference)

| id | shloka | source | in Sandhyāvandanam? |
|----|--------|--------|---------------------|
| 017 | Aghamarṣaṇa Sūkta | RV 10.190 | yes (snāna) |
| 033 | Prāṇāyāma — vyāhṛtis + Gāyatrī + *āpo jyotī* | RV 3.62.10 + Taittirīya | yes |
| 034 | Mārjana — *āpo hi ṣṭhā* | RV 10.9.1–3 | yes |
| 038 | *ā kṛṣṇena rajasā* | RV 1.35.2 | yes (arghya/noon) |
| 059 | **Gāyatrī Mahāmantra** | RV 3.62.10 | yes |
| 061 | *mitrasya carṣaṇīdhṛtaḥ* | RV 3.59 | yes (digupasthāna, morning) |
| 062 | *imaṃ me varuṇa* | RV 1.25 | yes (digupasthāna, evening) |
| 063 | *udvayaṃ tamasaspari* | RV 1.50.10 | yes (sūryopasthāna) |
| 064 | *ud u tyaṃ jātavedasaṃ* | RV 1.50.1 | yes (sūryopasthāna) |
| 065 | *citraṃ devānām* | RV 1.115.1 | yes (sūryopasthāna) |
| 066 | *tac cakṣur devahitaṃ* | ŚYV 36.24 | yes (sūryadarśana) |
| 067 | *ya udagān mahato'rnavāt* | sūrya mantra | yes (sūryopasthāna) |
| 069 | *indra śreṣṭhāni draviṇāni* | RV 2.21.6 | yes (diṅnamaskāra, east) |
| 071 | *dhruvāsu tvāsu* | Varuṇa mantra | yes (dik-upasthāna, west) |
| 079 | *catvāri śṛṅgā* | RV 4.58.3 | no (daily Agni) |
| 082 | **Śrī Sūkta** | Ṛgveda khila | no (Lakṣmī pūjā) |
| 083 | **Devī Sūkta** | RV 10.125 | no (Vedic sūktas) |

## Wiring external audio into the site

The site shows an audio player for any shloka that has a wav file at `audio/NNN-slug.wav` — **regardless of `tts_skip`** (file-existence wins). So once you have a recitation clip for an excluded shloka:

1. Convert/trim it to a wav (any sample rate; 24 kHz mono matches the model output but isn't required).
2. Name it exactly `audio/NNN-slug.wav` (match the id and slug — see the filename in `shlokas/`).
3. Run `python3 build_site.py`.

The site will then play your authoritative svara recitation for that shloka, with the `tts_note` no longer shown (since audio now exists). `verify_audio.py` will list it under "wavs outside manifest" (expected — it's external, not model-rendered), which is just informational.

> Tip: keep model-rendered and externally-sourced audio distinguishable if you like — e.g., drop external clips in `audio/` directly (they'll play) and note them here as you add them.

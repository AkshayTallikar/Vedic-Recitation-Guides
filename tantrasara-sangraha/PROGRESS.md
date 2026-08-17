# Tantrasāra-Saṅgraha reader

## Published source

The website follows the attached **Sarvamūla — Reader.pdf** exactly. Its four chapters contain 401 numbered verses:

- Chapter 1: 75
- Chapter 2: 24
- Chapter 3: 141
- Chapter 4: 161

The matching IAST is reproduced from the attached **IASTR.pdf**. The Devanagari source is retained in `reader-source.json`; the English meaning is aligned to that source rather than to the numbering of a different printed edition.

## Translation policy

- Every source verse is represented once and in order.
- English is complete and non-abridged.
- Where Sanskrit syntax continues across verse boundaries, the verses are displayed individually but share one combined English meaning so words are neither dropped nor translated twice.
- Optional word and compound explanations preserve useful detail from the commentary-based working translation.

## Files

- `reader-source.json` — 401 source verses with Devanagari and IAST
- `extract_reader_source.py` — reproducible extraction/normalization utility for the Sarvamūla reader database
- `text/ch1.md` … `text/ch4.md` — commentary-based translation working corpus used for alignment
- `build.py` — validates, aligns, and builds the reader
- `index.html` — generated website

To rebuild:

```sh
python3 build.py
```

The build must report: `401 verses in 244 source-aligned translation units`.

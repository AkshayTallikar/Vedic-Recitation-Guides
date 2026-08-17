# Padyamālā literal English reader

## Source

The reader follows [padhyamala12022013.pdf](https://srimadhvyasa.wordpress.com/wp-content/uploads/2013/02/padhyamala12022013.pdf), a 16-page publication of Śrī Jayatīrtha's Padyamālā. The main Sanskrit work is printed in Kannada script on PDF pages 4-16 and contains 122 numbered verses.

The website retains:

- all 122 numbered verses;
- the authorship and concluding colophons;
- the `śrīkṛṣṇārpaṇam astu` dedication;
- the final two-line prayer.

The English is literal and non-abridged. Named mantras or hymns that the work cites only by their opening words remain references rather than being replaced with text from outside the source.

## Files

- `source.tsv` — audited IAST source and complete English meaning
- `build.py` — validates the sequence, generates Kannada script from IAST, and builds the reader
- `index.html` — generated website

To rebuild, install `indic-transliteration` and run:

```sh
python3 build.py
```

The build must report: `122 numbered verses and 4 closing units`.

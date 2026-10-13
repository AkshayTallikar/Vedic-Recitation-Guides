# Ayudha Puja source preservation and review

Source: [Sumadhwa Seva, Ayudha pooja](https://www.sumadhwaseva.com/festivals/aashwayuja/ayudha-pooja/).

The user supplied the complete article in chat. `source-user.txt` is that supplied text, with its original whitespace and one final newline. The production guide is `site/data18.js`, key `ayudha-puja`: 20 sections, 41 ordered blocks, 80 Sanskrit learning lines (including the article’s parallel-script prayer copies). No recording was supplied. This is a text guide.

`evidence-manifest.json` reconstructs all 6,926 UTF-16 source code units exactly. Every segment maps to one guide block. Section guidance is an editorial addition, attributed to the relevant character spans. English prose already present in the source is retained; Kannada prose is fully translated and romanized. Printed text, Roman source readings, reviewed mantra display and learning glosses remain distinct.

The mantra dictionaries preserve the detailed correction reasons and confidence. The guide displays those repairs in expandable lists. `content-review.json` records source limitations and the unresolved tattvanāsikā deity-class reading. This preservation and editorial review does not certify the uncertain printed reading.

Reading comparisons: Rigveda 10.9.1–3 at the University of Texas Linguistics Research Center; the dagger prayer quoted from Vishnudharma in Shudrakamalakara; the selected Kalasha prayer lines in Samskararatnamala, part 1, printed p. 151 (scan page 155). Their links are included in the guide. Additional stanzas from those witnesses are not imported, and they are not used as authority to alter the Madhva deity hierarchy.

Rebuild from repository root:

```sh
python3 backups/guide-ayudha-puja-evidence/build_guide.py .
python3 build/inline.py
node backups/guide-ayudha-puja-evidence/validate_lossless_guide.mjs --data site/data18.js --guide-key ayudha-puja --skip-audio --require-spacing --require-enrichment --evidence-manifest backups/guide-ayudha-puja-evidence/evidence-manifest.json
```

`validation.json` records structural checks. `validator-check.json` records rejection of character gaps, reordering, source drift, fabricated durations/seconds, missing Action and missing word glosses, plus UTF-16 surrogate testing and regression of the existing three-video Saraswati manifest. `browser-check.json` records desktop/mobile widths, all 80 rendered meanings and lexical rows, 20 Contemplate/Action pairs, search, archived-guide visibility, original-source/correction details, print visibility and existing Saraswati audio/auto-scroll operation.

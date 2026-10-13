Visarjana source reconciliation
==============================

sections.json is the integration artifact: V01–V11, 32 ordered blocks, full Kannada Roman/English and Sanskrit Roman/line meanings/lexical glosses. The parent guide should add source URL/audio mapping without changing the source reconstruction.

complete-source.txt is exact concatenation of all sourceOriginal fields. Raw GPT and captions are separate and unchanged. source-ledger.json includes their paths and SHA256 hashes. evidence-manifest.json and aligned-segments.json map every ordered retained block. caption-event-audit.json accounts for all 454 native word events. fine-window-clause-audit.json explicitly maps all 134 fine-witness clause artifacts to retained blocks (or identifies punctuation-only ellipses).

Six targeted gpt-4o-transcribe acoustic windows and unchanged responses reside here; target-checks-manifest.json gives their origin/length. They corroborate damaged Sanskrit phonetic clusters rather than resolve them. No personal listening interface was available. Caption-marker alignment is not exact acoustic certification.

Uncertain readings are visible in individual block.notes, section.verifyNotes and uncertainty-inventory.json. The establishment phrase, Madhva prayer opening/count/compound endings, shami verses and charity quotation remain specifically uncertain. They must not be silently replaced from memory. The turmeric/kumkuma instruction conflicts with a coarse ASR reading of ashtanga-namaskara; the material reading is provisional and no bodily gesture was invented. Recorded Thursday/fourth-day context is from the 2025 recording.

All timing endpoints are actual embedded VTT markers, except final endpoint 416.612438, the ffprobe measured media duration. Native ending cue is longer than the actual media. Internal 0.01-second cue transition gaps are documented as gaps rather than certified silence. No shared-caption overlap was required because embedded markers permit ordered language splits.

Reproduce canonical data in order using the bundled Python runtime:
1. build.py
2. refine-audit.py (once, immediately after build.py)
3. audit.py
4. clause-mapping.py (the explicit clause review replaces broad initial candidate mappings)

validation.json records structural checks; it does not certify all uncertain words or acoustic sync. Parent integration must verify exported audio bounds and rendered line replay.

Textual revision: after refine-audit.py run textual-reconcile.py, then audit.py and clause-mapping.py. The Madhva opening display is now abhramaṃ bhaṅgarahitam, backed by matching local UTM page 33/data10 candidates and compatible acoustic shapes. Original script/phonetic Roman remain unchanged; readingReconciliation explains the correction. Shami textual candidates improve gloss interpretation but do not replace the unresolved recorded wording. The located digitized text lacks official-edition metadata, so it is not represented as an authenticated official primary witness. Charity remains unresolved.

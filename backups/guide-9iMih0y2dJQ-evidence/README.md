# Ganapati Pūjā guide evidence

This directory preserves the compact evidence used to build the complete Roman-script guide for YouTube video `9iMih0y2dJQ`:

- the original YouTube metadata and source-media checksum;
- the original YouTube auto-caption track, losslessly compressed as `.vtt.gz`;
- three independent `gpt-transcribe` passes (300-second overlapping, 180-second overlapping, and 150-second contiguous windows);
- 18 short boundary-window transcripts used to reconcile every 150-second join.

The downloaded source and temporary WebM chunks are intentionally omitted because they can be reproduced from the source URL and would add roughly 180 MB to the repository. The 19 compressed practice clips used by the published guide are retained under `site/audio13/`.

No API key or authorization header is stored here or anywhere in the guide data.

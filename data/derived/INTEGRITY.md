# Derived Data Integrity Snapshot

This snapshot records the repository state after the row-aligned visibility field was verified and added to the public annotation release.

| Artifact | Data rows | True Positive | False Positive | Git object SHA |
|---|---:|---:|---:|---|
| `annotation_candidate_records_deidentified.csv` | 546 | 450 | 96 | `79442d00b0d9d662b686b8b80fbb42bb776a2100` |
| `annotation_candidate_records_audited.csv` | 545 | 449 | 96 | `5d33988e887566413df2115205e97959b7f20f91` |

The raw table contains 172 `good`, 152 `moderate`, and 222 `partial_occlusion` visibility annotations. These values were recovered from the row-aligned source text, not inferred from notes.

The one-row raw/canonical difference is the exact repeated `624-506 / clip_001.mp4` match+clip key. The audited table retains the first canonical occurrence and excludes only the repeated occurrence.

These counts were verified from the committed derived-data content. They are integrity/provenance checks, not additional full-system model-performance claims.

If either annotation artifact changes, this snapshot must be regenerated and the evidence ledger updated.

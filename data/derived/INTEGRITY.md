# Derived Data Integrity Snapshot

This snapshot records the repository state after the first public annotation-evidence release.

| Artifact | Data rows | True Positive | False Positive | Git object SHA |
|---|---:|---:|---:|---|
| `annotation_candidate_records_deidentified.csv` | 546 | 450 | 96 | `1f2f1a1acae866f7ec13fa786eccea846d313391` |
| `annotation_candidate_records_audited.csv` | 545 | 449 | 96 | `80fb4140a043153995af5beda37b17d405efed84` |

The one-row difference is the exact repeated match/clip key identified in the audit. The audited table retains the first canonical occurrence and excludes only the repeated occurrence.

These counts were re-read from the committed CSV files after publication to GitHub. They are integrity/provenance checks, not additional model-performance claims.

If either artifact changes, this snapshot should be regenerated and the evidence ledger updated.

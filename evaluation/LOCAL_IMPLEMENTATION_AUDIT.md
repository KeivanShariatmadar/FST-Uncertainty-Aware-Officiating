# Local FST v4.2 Implementation Audit

The FST v4.2 source package is intentionally kept outside the public SSAC repository. The public repository contains the evaluation code, model-output schema and implementation-audit procedure, not the production source itself.

## Why a local audit is sufficient for the next step

SSAC states that model code is encouraged but not required. The research package still needs enough model/configuration provenance to make the released predictions interpretable and traceable.

The private implementation can therefore be inspected locally and summarized through non-source artifacts:

- source-package SHA-256;
- per-file SHA-256 inventory;
- dependency/runtime files;
- model/weight candidates;
- likely entry points;
- implementation-signal file locations;
- final frozen inference configuration;
- frozen prediction export.

## Run the privacy-preserving package inventory

From the repository root:

~~~bash
python evaluation/inspect_fst_package.py \
  "/path/to/FSTai_Competition_Platform_v4_2(1).zip" \
  --out fst_package_audit
~~~

This produces package_manifest.json, file_inventory.csv, and implementation_signals.csv.

The script does not write source-code snippets or secret values. Its reports should still be reviewed before any public release because filenames can themselves contain sensitive information.

## Next local inspection

Using implementation_signals.csv, inspect privately the source files associated with:

1. video/frame input and timestamp handling;
2. head-kick/action classification;
3. contact/impact logic;
4. event aggregation/deduplication;
5. confidence;
6. genuine model uncertainty/credal/random-set logic;
7. defer/abstain logic;
8. model loading/weight identifiers;
9. logging/export;
10. compute latency.

Record verified findings in IMPLEMENTATION_AUDIT_CHECKLIST.md or a private working copy. Do not infer implementation behavior solely from the FST papers.

## Frozen prediction export

Once the implementation path is known, add an exporter that emits exactly the fields in FROZEN_MODEL_EXPORT_SPEC.md without loading the human annotations or final ground truth. Hash the resulting prediction file and record the package/model/configuration identifiers in a populated model manifest.

Only after the prediction file is frozen should it be compared with ground_truth_events.csv.

## Important

Do not upload:
- API keys;
- environment files containing credentials;
- private keys;
- production model weights unless the owners intentionally choose to release them;
- source footage without verified redistribution rights.

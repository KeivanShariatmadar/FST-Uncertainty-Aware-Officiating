# SSAC27 Open-Source Compliance Review

Last reviewed against the official MIT Sloan Sports Analytics Conference Research Paper Competition page on 2026-09-22.

## Conference requirement

The current SSAC27 rules state that all research-paper submissions must be open-source and must provide a GitHub or other open repository containing **the data used to conduct the research**. The rules explicitly say this includes publicly available data and private/proprietary data, with personal information anonymized using the authors' best judgment. Model code is encouraged but is **not required**.

Official rules: https://www.sloansportsconference.com/research-paper-competition

## Current repository status

### Public now
- de-identified candidate-level annotation records;
- exact-deduplicated audited candidate table;
- audit log and machine-readable audit summaries;
- metric definitions and statistical-analysis plan;
- deterministic event-matching, validation, audit and evaluation scripts;
- evidence ledger and claim-provenance documentation;
- submission/abstract material.

### Not public now
- raw championship video;
- frozen production FST source/weights;
- private deployment configuration/logs.

Production model code is not required by the SSAC rule. The **data** question is more important.

## Compliance risk: competition video

If a submitted SSAC result depends directly on raw championship video that is not publicly available, the current repository may not fully satisfy Sloan's stated data requirement.

The fact that the authors own FST does not automatically establish redistribution rights for third-party competition footage, broadcasts, athlete likenesses, event branding or federation-controlled material.

Therefore a headline model-performance experiment based on such footage should not be described as fully open-source until one of the following is true:

1. **Authorized public release:** the relevant evaluation video/clips can legally be redistributed and are publicly released;
2. **Legally anonymized public input release:** a scientifically equivalent public evaluation input (for example appropriately transformed/cropped/anonymized clips) is produced and its redistribution rights are established;
3. **Conference-confirmed alternative:** Sloan confirms in writing that a specified derived representation is acceptable in place of non-redistributable third-party raw video.

## Evidence-safe abstract path

The current evidence-safe abstract uses the public de-identified candidate-annotation dataset as the analysed population and does not claim independently reproduced full-video model recall/F1. That analysis is reproducible from the repository as it stands.

If stronger FST model-performance numbers are inserted later, the corresponding input-data release status must be revisited before submission.

## Licensing risk

Public visibility alone is not equivalent to a reuse license. The repository currently has no blanket license (`CITATION.cff: NOASSERTION`).

The authors have indicated an intended boundary of public/non-commercial research use while preserving FST commercial rights. That intent is compatible with keeping the production FST implementation outside the SSAC repository because model code is not mandatory, but the exact license for released data/evaluation scripts remains an author-level legal decision.

No license is imposed automatically by this audit.

## Submission gate

Before the final repository URL is entered into the form, verify:

- [x] repository is public;
- [x] FST/FST 2.0 scope only;
- [x] data supporting current evidence-safe numerical results are public;
- [x] public analysis/evaluation scripts are present;
- [x] personally identifying athlete names removed from released candidate table;
- [ ] rights/compliance resolved for any raw-video-dependent headline result;
- [ ] reuse-license choice finalized or explicitly confirmed acceptable for Sloan;
- [ ] final abstract contains only claims whose public evidence status matches this repository.

## Practical interpretation

The repository is already suitable for the **current evidence-safe annotation-audit results**. It is not yet safe to call a future raw-video FST benchmark fully open-source merely because the derived prediction CSV is public. The input-data rights/release question must be resolved at the same time as that stronger experiment.

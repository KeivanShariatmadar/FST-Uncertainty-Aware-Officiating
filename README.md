# FST: Uncertainty-Aware AI-Assisted Officiating in Competitive Taekwondo

This repository accompanies the **SSAC27** research submission:

**Uncertainty-Aware AI-Assisted Video Review for Faster and More Reliable Officiating in Competitive Taekwondo**

**Authors:** Keivan Shariatmadar¹ · Ahmad Osman¹ · Ramin Rey²  
¹ htw saar – University of Applied Sciences, Saarbrücken, Germany  
² Austrian Taekwondo Federation (AUT), Austria

## Purpose
FST.ai investigates human-in-the-loop artificial intelligence for assisting video-review decisions in competitive Taekwondo. This SSAC research package is deliberately restricted to the FST.ai / FST.ai 2.0 officiating research line. APEX, Digital TA, WT-SCIP/SCIP, SILs and other projects are outside the scope of this submission.

The central question is whether AI-assisted review can improve the speed, reliability, transparency and auditability of difficult officiating decisions while preserving final human authority.

## What is public here
The repository now contains:
- research and reproducibility documentation;
- evaluation and claim-audit protocols;
- metric definitions;
- executable validation/evaluation scripts;
- a de-identified candidate-level annotation release and canonical exact-deduplicated audit;
- FST/FST 2.0 publication references;
- SSAC submission material.

The candidate annotation release is **not** presented as a complete model-performance benchmark: it does not independently enumerate false negatives and its human confidence labels are not model epistemic uncertainty.

## Human-in-the-loop principle
FST.ai is decision support. AI outputs are evidence and recommendations for authorized human officials; they are not autonomous competition decisions. Ambiguous or insufficient-evidence cases remain subject to human adjudication.

## Evidence discipline
No quantitative result is promoted to the SSAC manuscript unless its evaluation unit, sample size, denominator, source, reference procedure and calculation are traceable. Public preprint claims that are not yet independently reconstructed are explicitly quarantined in the published-claims audit rather than silently repeated as new evidence.

## Open research and implementation boundary
Public availability of this repository does not by itself publish production FST source code, trained production weights, credentials, confidential deployment configuration or protected implementation know-how. The SSAC competition states that model code is encouraged but not required; the data used for the research and reproducible evaluation evidence are the priority of this package.

Third-party competition footage is not redistributed unless the authors have the legal authority and appropriate permissions to do so.

## Repository map
- `DATA_STATEMENT.md` — provenance, availability and restrictions
- `REPRODUCIBILITY.md` — reproducibility scope
- `IP_AND_LICENSING.md` — IP/licensing boundary
- `CITATION.cff` — citation metadata
- `paper/` — SSAC abstract/submission material and readiness notes
- `data/derived/` — de-identified audited annotations and target derived-evidence schemas
- `evaluation/` — metrics, evidence audit, claim audit and executable evaluation scripts
- `references/` — FST.ai and FST.ai 2.0 publication record

## Current evidence status
The first annotation audit contains 546 raw candidate-level records and 545 canonical records after removal of one exact duplicate match/clip key. The final manuscript-ready benchmark still requires an independent ground-truth event inventory and frozen FST/FST 2.0 prediction export so that TP, FP and FN are derived through deterministic event matching.

See `evaluation/ANNOTATION_AUDIT.md`, `evaluation/PUBLISHED_CLAIMS_AUDIT.md`, and `paper/SSAC27_SUBMISSION_READINESS.md`.

## Contact
Scientific correspondence: Keivan Shariatmadar, htw saar – University of Applied Sciences.

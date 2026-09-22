# Data Statement

## 1. Scope
This statement describes the data status for the SSAC27 study on uncertainty-aware AI-assisted video review in competitive Taekwondo. The study is restricted to the FST.ai / FST.ai 2.0 officiating research line.

## 2. Source material
The FST research uses competition-video evidence and associated officiating information for studying difficult scoring actions, including head-kick review. Some underlying material may contain identifiable athletes, officials, event branding, broadcast material, or other content controlled by third parties.

## 3. Rights and privacy constraints
Public possession of a research result does not imply that the authors own redistribution rights to every underlying video frame or recording. Source footage is therefore not placed in this repository unless redistribution rights, privacy basis, and relevant permissions have been verified.

Restrictions may arise from athlete privacy and likeness rights, event or federation rights, broadcasting rights, contractual obligations, or other third-party rights.

## 4. Currently released derived data
The repository releases a de-identified candidate-level annotation table and its canonical exact-deduplicated audit version. Athlete names are removed. Audit fields preserve duplicate/bookkeeping provenance without presenting the table as a complete ground-truth benchmark.

The released candidate annotations currently contain 546 raw candidate records. One exact repeated match/clip key yields 545 canonical records after exact deduplication. See `evaluation/ANNOTATION_AUDIT.md` for the evidence interpretation and limitations.

## 5. What may additionally be released
Subject to provenance and rights review, the authors intend to release research artifacts sufficient to support independent scrutiny of reported results where legally permissible, including:
- de-identified ground-truth event/action records;
- frozen model outputs used in evaluation;
- review-latency observations;
- numerical uncertainty or confidence outputs;
- aggregate contingency tables and summary statistics;
- data dictionaries; and
- scripts that reproduce reported metrics.

## 6. What is not currently released
This repository does not publish raw competition video whose third-party redistribution rights have not been verified, production model weights, credentials, confidential deployment configuration, or protected implementation know-how.

The absence of restricted source footage must not be interpreted as a claim that the source footage is open data.

## 7. Quantitative-claim provenance
Every SSAC headline result must be linked to its evaluation population, denominator, measurement protocol and releasable evidence artifact. Public FST/FST 2.0 preprint claims that have not yet been independently reconstructed are tracked separately in `evaluation/PUBLISHED_CLAIMS_AUDIT.md`.

## 8. Access questions
Questions about whether a specific research artifact can be shared should be directed to the corresponding author. Access cannot be promised where the authors do not control the relevant third-party rights.

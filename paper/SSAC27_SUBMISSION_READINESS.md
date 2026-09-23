# SSAC27 Submission Readiness

## Competition identity
The current MIT Sloan Sports Analytics Conference research-paper page states that **submissions for SSAC27 are open**, with abstract submissions due **October 1, 2026 at 11:59 p.m. Eastern Time**. The repository naming as SSAC27 is therefore intentional.

Official rules: https://www.sloansportsconference.com/research-paper-competition

## Abstract requirements
The submitted abstract should:
- contain fewer than 500 words, including title and body;
- use the required sections: Introduction, Methods, Results, Conclusion;
- report actual rather than promised results;
- include no more than two figures/tables combined;
- be supported by an open repository containing the data used to conduct the research.

## Current readiness

### Complete / materially complete
- public SSAC27 repository with functioning write access;
- author/affiliation metadata;
- strict FST.ai / FST.ai 2.0 officiating scope (APEX, Digital TA, WT-SCIP/SCIP, SILs excluded);
- updated data, IP and reproducibility statements;
- metric definitions and statistical analysis plan;
- bout-level split/leakage policy and validator;
- evidence-audit protocol;
- populated claim/evidence ledger;
- published-claims reconciliation audit;
- de-identified 546-row candidate annotation release;
- verified row-aligned visibility annotations;
- 545-row canonical exact-deduplicated candidate table;
- public audit log, category counts, joint-pattern table, stratified descriptive table and integrity snapshot;
- reproducible candidate-annotation audit script;
- deterministic one-to-one temporal/class event-matching script;
- derived-data structural validator;
- performance / cluster-bootstrap / risk-coverage evaluator;
- candidate-vs-decision-level selective-prediction protocol;
- frozen-model export specification and model-manifest template;
- private-package implementation-audit checklist and privacy-preserving ZIP inventory utility;
- final SSAC27 abstract candidate with **393 words including title and section headings**;
- claim-to-evidence map for the abstract;
- open-source compliance review;
- fully rewritten current-evidence manuscript with literature positioning, audited methods/results, limitations and reproducibility section.

### Current verified abstract-stage results
The public evidence currently supports:
- 546 raw candidate records across 74 recorded match IDs;
- one exact duplicate match+clip occurrence;
- 545 canonical candidate records;
- 449 TP-labelled and 96 FP-labelled canonical candidates;
- 82.39% canonical candidate-confirmation rate, explicitly **not** described as recall/F1/overall accuracy;
- 535/546 (97.99%) raw rows in four dominant annotation patterns;
- verified visibility counts: 172 good, 152 moderate, 222 partial occlusion;
- all 96 FP-labelled raw candidates occur in the Medium-confidence / Hard / uncertain-event / uncertain-contact / partial-occlusion annotation pattern.

These are annotation/candidate-population results, not a substitute for an independent event-level FST benchmark.

### Not yet manuscript-ready for stronger FST efficacy claims
- independently enumerated ground-truth event inventory that observes false negatives;
- audited train/validation/test split manifest at bout level;
- completed private inspection of the supplied FST v4.2 source package;
- frozen FST/FST 2.0 prediction export tied to code/model/configuration fingerprints;
- actual event matching between independent ground truth and frozen predictions;
- model-generated numerical uncertainty/evidence field for selective-prediction evaluation;
- reconciled raw/reconstructable latency observations supporting a headline review-time reduction;
- reconciled raw/reconstructable referee survey observations supporting a headline trust statistic.

## Supplied implementation package
A private package named `FSTai_Competition_Platform_v4_2(1).zip` has been supplied to the research workspace. The public repository intentionally does not publish it.

The current ChatGPT/container workspace has not been able to extract/read the ZIP at byte level reliably, so no implementation behavior is claimed as code-verified yet. The repository now includes `inspect_fst_package.py` and `LOCAL_IMPLEMENTATION_AUDIT.md` so the same audit can be completed locally without exposing source code.

## Open-source/data gate
Sloan's current rule requires a public repository containing the data used to conduct the research; model code is encouraged but not mandatory.

The data supporting the current evidence-safe annotation-audit results are public. A stronger raw-video model benchmark introduces a separate rights/compliance question for championship footage. See `SSAC27_OPEN_SOURCE_COMPLIANCE.md`.

## Submission rule
Do not promote a public-paper number into the SSAC Results section merely because it already appears on arXiv. A headline number becomes SSAC-ready only when the evidence ledger records the evaluation unit, sample size, denominator, source, reference procedure, calculation and release status.

## Recommended empirical hierarchy
The strongest final FST abstract/paper should prioritize:
1. event-level detection/classification performance from independent ground truth;
2. robustness under visibility/occlusion/contact difficulty;
3. risk-versus-coverage / defer-to-human behavior from actual FST uncertainty;
4. operational review latency;
5. human acceptance/trust as a separate user-study outcome.

The current recommended abstract is `SSAC27_ABSTRACT_FINAL_CANDIDATE.md`. It uses only verified current-study results and does not promote unreconciled prior-public headline figures. The rewritten current-evidence manuscript is `SSAC27_FULL_PAPER_CURRENT_EVIDENCE.md`.

## Owner-level licensing item
The repository currently has no blanket reuse license (`CITATION.cff` states `NOASSERTION`). Granting a license changes legal reuse rights, so no new data/software license has been imposed automatically.

Before final submission, the authors should reconcile the intended non-commercial research-use boundary with Sloan's open-source requirement.

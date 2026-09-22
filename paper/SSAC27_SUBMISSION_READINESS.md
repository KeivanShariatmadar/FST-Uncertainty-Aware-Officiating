# SSAC27 Submission Readiness

## Competition identity
The current MIT Sloan Sports Analytics Conference research-paper page states that **submissions for SSAC27 are open**, with abstract submissions due **October 1, 2026 at 11:59 p.m. Eastern Time**. The repository naming as SSAC27 is therefore intentional.

## Abstract requirements
The submitted abstract should:
- contain fewer than 500 words, including title and body;
- use the required sections: Introduction, Methods, Results, Conclusion;
- report actual rather than promised results;
- include no more than two figures/tables combined;
- be supported by an open repository containing the data used to conduct the research.

## Current readiness
### Complete / materially complete
- public SSAC27 repository;
- author/affiliation metadata;
- FST/FST 2.0-only scope boundary;
- data statement and IP boundary;
- reproducibility statement;
- metric definitions;
- evidence-audit protocol;
- evidence ledger template;
- executable derived-data validator;
- executable performance / clustered-bootstrap / risk-coverage evaluator;
- de-identified candidate-level annotation release;
- raw-versus-canonical exact-duplicate audit;
- published-claims reconciliation audit.

### Not yet manuscript-ready
- independently enumerated ground-truth event inventory with false negatives;
- frozen FST/FST 2.0 prediction export tied to an implementation/version identifier;
- deterministic event matching between ground truth and predictions;
- model-generated numerical uncertainty/evidence field for selective-prediction evaluation;
- raw/reconstructable latency observations supporting a headline reduction;
- raw/reconstructable referee survey observations supporting a headline trust statistic.

## Submission rule
Do not promote a public-paper number into the SSAC Results section merely because it already appears on arXiv. A headline number becomes SSAC-ready only when the evidence ledger records the evaluation unit, sample size, denominator, source, ground-truth/reference procedure, calculation and release status.

## Recommended abstract strategy
The strongest final abstract should center on real competitive officiating and uncertainty-aware selective decision support, not on the broader FST 2.0 ecosystem.

The preferred empirical hierarchy is:
1. event-level detection/classification performance from independent ground truth;
2. robustness under visibility/occlusion/contact difficulty;
3. risk-versus-coverage / defer-to-human behavior from actual FST uncertainty;
4. operational review latency;
5. human acceptance/trust as a separate user-study outcome.

If the frozen event-level experiment is not complete by the abstract deadline, the abstract must be limited to quantities whose evidence has already passed the claim gate.

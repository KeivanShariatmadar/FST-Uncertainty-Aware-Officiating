# Published-Claims Audit

## Purpose
This file separates statements already present in the public FST.ai / FST.ai 2.0 research record from quantities that are independently verified for the SSAC27 evidence package.

A value being present in a public preprint is **not** sufficient, by itself, for promotion to a new SSAC empirical result. Headline results require traceable observations, denominators, measurement procedures and a reproducible calculation.

## FST.ai (arXiv:2507.14657)
The 2025 FST.ai preprint describes a real World Taekwondo Cadet World Championship IVR example in Fujairah in which a head-kick review took nearly 90 seconds. It also describes the FST workflow as returning a jury-facing decision package within approximately 3–5 seconds.

The paper additionally gives architecture-level and illustrative latency examples for pose estimation, action classification and impact analysis. These are useful system-design references but are not treated as a replacement for a controlled latency dataset.

**SSAC status:** useful public provenance and operational motivation; new latency-effect claims require the underlying observation set and comparable baseline/assisted timing definitions.

## FST.ai 2.0 (arXiv:2510.18193)
The public abstract reports:
- 85% reduction in decision-review time;
- 93% referee trust in AI-assisted decisions.

Publicly accessible body text associated with the same preprint also reports multiple more specific pilot quantities, including examples such as:
- mean review time 89.7 s versus 4.6 s, described as a 94.8% reduction;
- N=27 referees and a 4.65/5 (93%) trust rating;
- model-human/jury-consensus accuracy around 0.927;
- a historical-to-pilot jury override reduction from 0.31 to 0.18 (41.9%);
- a 68-match pilot description.

A later experimental-results section in the same public document reports a second set of descriptions, including:
- 156 IVR requests across four competition days;
- average review duration 89.3 s versus 4.6 s;
- head-kick classification accuracy 92.8%;
- 87% of referees and 93% of coaches rating assistance as valuable or very valuable.

## Reconciliation issue
The public record therefore contains quantities that are not fully internally aligned. In particular:
1. 89.7 -> 4.6 s corresponds to about 94.9%, not 85%;
2. the identity/meaning of the 93% acceptance/trust figure differs across passages;
3. sample units vary across matches, IVR requests, referees and coaches;
4. reported accuracy/precision terminology is not always consistent.

These discrepancies are not silently resolved in this repository.

## SSAC claim gate
Until raw or auditable source observations are linked to each quantity:
- **85% review-time reduction:** public FST.ai 2.0 claim, not yet independently reconstructed here;
- **93% referee trust:** public FST.ai 2.0 claim, not yet independently reconstructed here;
- **89.7/89.3 s -> 4.6 s:** public pilot descriptions requiring reconciliation;
- **92.7/92.8% model accuracy:** public pilot description requiring event-level denominator and ground-truth reconstruction;
- **41.9/42% override reduction:** public historical comparison requiring the underlying historical and pilot counts.

The SSAC manuscript should use only a reconciled version whose source observations and definitions can be placed in the evidence ledger.

## Scope restriction
For SSAC27, only the FST.ai / FST.ai 2.0 officiating research line is in scope. Material from APEX, Digital TA, WT-SCIP/SCIP, SILs or other systems is not imported into this evidence package.

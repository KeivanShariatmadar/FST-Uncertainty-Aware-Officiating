# Final Scientific Review — SSAC27 FST Submission

## Overall assessment

The paper is now framed around the evidence that is actually available rather than around unreconciled headline claims from earlier FST publications. The final title,

**When Should AI Defer? An Evidence Audit of AI-Assisted Video Review in Competitive Taekwondo**

is intentionally narrower than earlier versions. This resolves the largest validity risk in the previous draft: the title no longer implies that model-generated epistemic uncertainty or risk-coverage has already been empirically validated when the current released data contain human annotation confidence rather than a frozen numerical FST uncertainty output.

## Why the final framing is stronger

The submission now has a coherent scientific object:

1. audit the championship-derived FST candidate evidence;
2. quantify what the candidate table supports;
3. identify the concentration and dependence structure of difficult cases;
4. state explicitly what the table cannot estimate;
5. convert those findings into a prespecified decision-to-defer benchmark for the frozen FST implementation.

This creates a direct link between the empirical results and the human-in-the-loop application without manufacturing false negatives or relabelling human confidence as model uncertainty.

## Abstract review

The authoritative abstract is 'SSAC27_ABSTRACT_FINAL.md'.

It contains 362 whitespace-delimited words including title and section headings and uses the required Introduction / Methods / Results / Conclusion structure.

The abstract now does four things efficiently:

- states the industry problem as support-versus-deferral rather than generic AI accuracy;
- reports the actual audited population and cluster-aware interval;
- makes the strongest empirical observation—the concentration of all 96 FP-labelled candidates in one difficult/ambiguous/partially occluded state—without presenting that association as causal calibration;
- gives a concrete application: auditable support on well-evidenced cases and human deferral for the ambiguous tail.

## Full-paper review

The authoritative manuscript is 'SSAC27_FULL_PAPER_MASTER.md'.

The final rewrite improves the manuscript in five ways.

### 1. Claim-to-evidence alignment
All current-study numerical claims remain traceable to the public candidate data and audit outputs. Candidate confirmation is not called recall, F1, or complete event-level accuracy.

### 2. Stronger methodological structure
The Methods section now separates source data, evidence roles, audit/canonicalization, estimands, dependence-aware inference, annotation-structure analysis, the event-level benchmark, and the selective-prediction benchmark.

### 3. Better uncertainty framing
The paper distinguishes:
- human annotation confidence;
- model confidence;
- model-generated epistemic uncertainty;
- candidate-level selective validation;
- preferred IVR decision-level risk-coverage.

This prevents a common but serious conflation between human uncertainty and model uncertainty.

### 4. Stronger literature positioning
The paper now connects FST to:
- Taekwondo and combat-sport computer vision;
- the Paris 2024 Taekwondo AI video-review study;
- selective classification and reject-option theory;
- learning to defer;
- human-AI selective prediction;
- uncertainty evaluation under shift.

The contribution is therefore positioned as an evidence-validity and decision-to-defer problem rather than another generic action-recognition study.

### 5. Clearer sports-industry application
The Discussion now translates the technical audit into operational requirements for federations and tournament organizers: preserve provenance, evaluate the correct denominator, separate human and model uncertainty, design deferral explicitly, and evaluate the combined human-AI review process.

## Remaining scientific limitation

The major remaining limitation is deliberate and visible: the present released evidence does not yet include an independent event census with false negatives or frozen numerical FST uncertainty outputs.

Accordingly, the current manuscript does **not** report:
- event-level recall or F1;
- a completed FST risk-coverage curve;
- a newly verified latency reduction;
- a newly verified 93% trust result;
- a newly verified approximately 92.8% accuracy result.

Those results should be added only when their source evidence passes the repository evidence ledger.

## Full-paper upgrade path

If the frozen FST benchmark becomes available before the full-paper deadline, the current master paper should be upgraded in place. The highest-value additions would be:

- independent TP/FP/FN results with bout-clustered intervals;
- turning/non-turning and occlusion robustness;
- numerical uncertainty ranking and risk-coverage;
- deferred-case composition;
- paired end-to-end review latency;
- a documented referee/user study if the underlying observations can be reconstructed.

The present paper is intentionally structured so these analyses can be inserted into Methods, Results, and Discussion without changing the core evidence-governance logic.

## Submission recommendation

For the abstract phase, use the authoritative final abstract exactly as stored unless a factual evidence status changes. Avoid adding attractive but unreconciled historical FST numbers during last-minute editing.

For a later full-paper submission, use 'SSAC27_FULL_PAPER_MASTER.md' as the base manuscript and strengthen it only with newly verified evidence.

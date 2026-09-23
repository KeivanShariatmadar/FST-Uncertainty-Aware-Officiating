# SSAC27 Final Submission Checklist

## Competition
- Abstract deadline: **October 1, 2026, 11:59 p.m. Eastern Time**.
- Full manuscript deadline if invited: **December 4, 2026, 11:59 p.m. Eastern Time**.
- Track: **Other Sports**.
- Open repository: https://github.com/KeivanShariatmadar/FST-Uncertainty-Aware-Officiating

## Recommended submission title
**When Should AI Defer? An Evidence Audit of AI-Assisted Video Review in Competitive Taekwondo**

## Recommended abstract
Use exactly:
- 'SSAC27_ABSTRACT_FINAL.md', or
- 'SSAC27_SUBMISSION_COPY_PASTE.txt' for direct form entry.

The authoritative abstract contains 362 whitespace-delimited words including title/headings, is below the 500-word limit, and uses the required Introduction / Methods / Results / Conclusion structure.

## Evidence status
### Ready for abstract-stage use
- 546 raw candidate records;
- 74 recorded match IDs;
- 73 bout clusters after documented ID linkage;
- one exact duplicate match+clip key;
- 545 canonical candidate records;
- 449 TP-labelled and 96 FP-labelled canonical candidates;
- 82.39% candidate-confirmation fraction;
- bout-cluster jackknife 95% CI: 81.16%–83.61%;
- 535/546 (97.99%) raw rows in four dominant joint annotation patterns;
- 222 partial-occlusion rows: 126 TP-labelled and 96 FP-labelled;
- all 96 FP-labelled rows share the Medium / Hard / uncertain-event / uncertain-contact / partial-occlusion pattern.

### Do not present as new SSAC empirical results
- 85% decision-review-time reduction;
- 93% referee trust;
- approximately 92.7–92.8% accuracy descriptions;
- 89.7/89.3 s to 4.6 s latency comparisons;
- recall or F1 from the current candidate table.

These remain prior-public or incomplete-evidence claims until the raw observations/denominators are reconstructed.

## Files to keep public
- de-identified candidate data;
- audited canonical candidate data;
- audit log;
- audit summaries;
- evaluation scripts;
- evidence ledger;
- statistical analysis plan;
- abstract and claim map;
- current-evidence full paper.

## Files not to publish automatically
- FST production source;
- production model weights;
- credentials or .env files;
- confidential deployment configuration;
- raw championship footage without verified redistribution rights.

## Final form checks immediately before submission
- confirm author spelling and order;
- confirm Ramin **Rey** spelling for SSAC submission;
- confirm repository is public;
- confirm repository URL opens without authentication;
- recount pasted abstract in the submission form;
- do not add unreconciled headline numbers during last-minute editing;
- retain a PDF/screenshot of the final submitted abstract and confirmation page.

## Full-paper upgrade if invited
The authoritative full paper is:
'SSAC27_FULL_PAPER_MASTER.md'.

Before the December full-paper deadline, the strongest upgrade is:
1. independently enumerate all eligible reference events;
2. freeze FST/FST 2.0 inference;
3. export model predictions and genuine numerical uncertainty;
4. derive TP/FP/FN using the registered event matcher;
5. report precision/recall/F1 with bout-clustered intervals;
6. generate risk-coverage/selective-deferral results;
7. reconcile latency observations;
8. reconcile the referee/coach human-study data;
9. resolve public-data rights for any raw-video-dependent headline result.

No placeholder or synthetic number should be inserted for any of these items.

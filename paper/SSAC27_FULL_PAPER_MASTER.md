# When Should AI Defer? An Evidence Audit of AI-Assisted Video Review in Competitive Taekwondo

**Keivan Shariatmadar¹, Ahmad Osman¹, Ramin Rey²**  
¹ htw saar – University of Applied Sciences, Saarbrücken, Germany  
² Austrian Taekwondo Federation (AUT), Austria

## Abstract

### Introduction
AI-assisted video review in combat sports is often judged by agreement or accuracy, yet the most consequential officiating failures occur when the visual evidence itself is weak. For a human-in-the-loop system, the operational question is therefore not only whether a detected action is correct, but when the AI should stop short of a recommendation and defer. We examine this question for FST.ai using championship-derived Taekwondo head-kick review evidence and audit what the available annotations can validly establish about performance and uncertainty.

### Methods
We audited 546 FST candidate clips from 74 recorded match identifiers. Each candidate contained a human validation label (True Positive or False Positive), human confidence, difficulty, action type, contact quality, and row-aligned visibility. The raw evidence was preserved; one exact duplicate match/clip record was excluded from the canonical population, and two identifiers documented as the same bout were treated as one clustering unit. We estimated the candidate-confirmation fraction, TP/(TP+FP), with a delete-one-bout cluster jackknife interval and examined the joint structure of the annotation fields. Because the candidate set does not independently enumerate missed true events, recall and F1 were not estimated. Human confidence was treated as annotation metadata, not model epistemic uncertainty.

### Results
The canonical population contains 545 candidates: 449 TP-labelled and 96 FP-labelled, giving an 82.39% candidate-confirmation fraction (95% bout-cluster jackknife CI: 81.16%–83.61%). Annotation structure was highly concentrated: 535 of 546 raw records (97.99%) fall into four repeated joint patterns. Among 222 partially occluded candidates, 126 were TP-labelled and 96 FP-labelled, a descriptive confirmation fraction of 56.76%. All 96 FP-labelled candidates share the same Medium-confidence, Hard, uncertain-action, uncertain-contact, partial-occlusion state. Thus, false candidates are concentrated in difficult visual evidence, but the strong coupling among human annotations prevents those fields from serving as independent validation of FST uncertainty.

### Conclusion
The audit changes how AI-assisted officiating should be evaluated. Candidate-only validation cannot establish full detection performance, and human confidence cannot substitute for model-generated uncertainty. We release the de-identified evidence and reproducible evaluation code and specify the stronger benchmark: an independent event census, frozen FST outputs, and risk-coverage analysis of model-generated uncertainty. For sports organizations, the practical target is reliable support on well-evidenced cases and auditable deferral of the ambiguous tail, with the authorized official retaining the final decision.

**Keywords:** sports analytics; Taekwondo; video review; human-in-the-loop AI; uncertainty; selective prediction; abstention; computer vision; officiating

---

## 1. Introduction

Video review is intended to correct consequential officiating errors, but the situations that trigger review are often the least convenient for automated vision: brief contacts, fast body rotation, athlete overlap, camera-relative occlusion, and uncertain contact geometry. In such settings, an AI system can be fast and apparently accurate on average while still failing on the cases that matter most. For an officiating tool, this creates a different objective from conventional image classification. The relevant system should not only recognize an action; it should also expose when the evidence is insufficient and route the decision back to the authorized official.

Competitive Taekwondo provides a concrete setting for this problem. Electronic Protector and Scoring Systems automate parts of point registration, while Instant Video Replay remains part of the adjudication process under World Taekwondo rules [1]. Head-kick review is particularly demanding because a valid scoring action may be visually brief, mechanically unregistered, or partly hidden. The practical problem is therefore not simply one of detecting a kick. It is one of supporting a rule-governed human decision under incomplete evidence.

FST.ai was introduced as an AI-assisted officiating framework for Taekwondo, with computer-vision, pose/motion, impact-related, and low-latency components intended to support review [2]. FST.ai 2.0 extended that research toward pose-based action recognition, explainability, and epistemic-uncertainty representations based on credal-set ideas [3]. The intended operating model is human-in-the-loop: the AI provides evidence or a recommendation, but the authorized referee or jury retains the final competition decision.

That operating model makes evaluation unusually important. A standard detector metric answers whether predictions match reference labels. It does not by itself answer whether an AI system knows when to abstain, whether its uncertainty is meaningful, whether its errors are concentrated in a specific evidence regime, or whether its reported performance was estimated from a complete event population. These distinctions matter because selective classification explicitly trades coverage for lower retained risk [4,5], while learning-to-defer methods treat the human expert as part of the decision system rather than as a passive fallback [6,7]. Human-AI experiments further show that deferral behavior and the way it is communicated can alter the quality of the combined decision process [8].

The present study addresses a prerequisite that is often skipped when operational sports-AI data are converted into research evidence: **what exactly does the available annotation table allow us to claim?** We audit a championship-derived FST candidate dataset before using it to make accuracy or uncertainty claims. This is not a semantic exercise. A table of system-proposed candidate detections can estimate how often surfaced candidates are confirmed, but it cannot establish recall unless missed true events are independently enumerated. Likewise, a human annotator's confidence cannot be relabelled as model epistemic uncertainty.

The audit revealed that these distinctions are material rather than theoretical. The candidate labels and contextual annotations are highly structured: nearly all rows fall into four repeated joint patterns, and every false-positive-labelled candidate occupies the same difficult, ambiguous, partially occluded state. This is operationally informative because it locates the difficult tail of the evidence. At the same time, the strength of that coupling prevents the same fields from being used as an independent uncertainty-validation experiment.

The study therefore asks four questions:

**RQ1.** What quantitative claims are supported by the championship-derived FST candidate annotations after explicit provenance, identity, and duplicate auditing?

**RQ2.** How are the false-positive-labelled candidates distributed across the available human annotations for confidence, difficulty, action type, contact quality, and visibility?

**RQ3.** Which annotation fields are valid contextual evidence, and which cannot be interpreted as FST model uncertainty?

**RQ4.** What benchmark is required to evaluate FST/FST.ai 2.0 as a genuine uncertainty-aware, human-in-the-loop officiating system?

The contribution is not a new headline accuracy value. It is a defensible evidence layer for the next model benchmark. Concretely, we provide: (i) a public de-identified candidate dataset with an immutable raw layer and explicit audit trail; (ii) a canonical candidate population with cluster-aware descriptive inference; (iii) a quantitative audit of annotation dependence; and (iv) a prespecified event-level and selective-prediction protocol that separates ground truth, model outputs, contextual annotations, and derived performance measures.

---

## 2. Related Work

### 2.1 AI and computer vision in sports officiating

Technology-assisted officiating now spans electronic scoring, goal-line and line-calling systems, video assistant systems, and computer-vision decision support. Recent work increasingly treats such systems as socio-technical rather than purely predictive: adoption depends not only on accuracy, but also on workflow fit, transparency, accountability, and the interaction between automated evidence and the official making the final decision [12].

In team sports, computer-vision-based video assistant systems have been investigated as a way to improve decision consistency and reduce review time [13]. Combat sports present additional perception challenges because athletes interact at close range, self-occlusion and mutual occlusion are common, and valid scoring often depends on a short sequence of pose, trajectory, and contact rather than a single static frame.

Related combat-sport research establishes that automated perception is feasible but also shows why officiating should not be reduced to action recognition. Lee and Jung's TUHAD dataset contains 1,936 Taekwondo poomsae samples covering eight unit techniques, ten experts, and two camera views, and their key-frame CNN achieved strong recognition performance under the reported experimental conditions [14]. Quinn and Corcoran combined real-time object detection, tracking, and pose estimation for combat-sport video analysis and discussed automated scoring as an application [15]. Ait-Bennacer et al. studied multiview Karate action recognition using pose estimation and temporal models in a smart-coaching setting [16]. Skeleton-based models such as Spatial Temporal Graph Convolutional Networks provide a natural technical basis for learning action dynamics from human pose sequences [17].

These studies are relevant to FST's perception layer, but officiating imposes a different validity requirement. A system used for review must be evaluated on the decision population that officials actually face, including ambiguous evidence and missed events, and not only on curated action-recognition examples.

### 2.2 AI-assisted Taekwondo video review

FST.ai introduced an AI-assisted Taekwondo officiating framework with emphasis on head-kick review and rapid evidence support [2]. FST.ai 2.0 expanded the system concept toward explainability, pose-based action recognition, and epistemic uncertainty [3]. Its public record reports headline quantities including an 85% reduction in decision-review time and 93% referee trust.

Those values are not re-used here as newly verified results. During the present evidence audit, the public FST.ai 2.0 record was found to contain multiple timing descriptions and differently framed trust/acceptance quantities. The underlying source observations, denominator definitions, timing boundaries, and survey wording have not yet been reconstructed in the current open evidence package. They are therefore treated as prior-public claims with explicit provenance rather than as current-study endpoints.

An independent 2025 Taekwondo study by Zhang, Qu, and Girard analyzed 241 video-review cases from the Paris 2024 Olympic competition [11]. The reported AI judgments showed strong agreement with international video-review referees (Cohen's κ = 0.897), with nine discrepant cases, and the authors reported an approximately 81% reduction in review time. Importantly for the present study, disagreement was concentrated in visually difficult situations involving minimal contact or occlusion, and the authors retained human oversight as part of the proposed workflow.

The two research lines should not be compared numerically as if they used the same model, task, population, or ground truth. Their common relevance is conceptual: difficult visual evidence is not a marginal implementation detail. It is central to how an AI-assisted review system should decide whether to issue a recommendation or defer.

### 2.3 Selective prediction and learning to defer

The reject option has a long history in statistical classification. El-Yaniv and Wiener formalized selective classification in terms of the trade-off between coverage and prediction risk [4]. Geifman and El-Yaniv later demonstrated how deep classifiers can be equipped with a selective mechanism that rejects cases to meet a desired risk level [5].

The distinction is especially useful for officiating. Suppose an uncertainty score \(U(x)\) is available for an eligible review case \(x\), with larger values indicating greater uncertainty. For threshold \(\tau\), an AI-assisted system can issue a recommendation only when \(U(x)\le\tau\). Coverage is then the fraction of cases retained for AI support, while selective risk is the error rate among retained recommendations. A useful uncertainty mechanism should rank cases such that risk decreases as the system becomes more selective.

Learning-to-defer extends this framing by modeling the downstream expert. Madras, Pitassi, and Zemel treat deferral as a decision that accounts for another decision maker [6], while Mozannar and Sontag provide consistent estimators for deciding when a model should predict and when it should hand the case to an expert [7]. Bondi et al. show that human behavior can itself change depending on how the AI's deferral is communicated, which means that system-level evaluation should eventually include the human-AI interaction rather than stopping at a model-only metric [8].

Uncertainty estimation also requires direct validation. Ovadia et al. show that predictive uncertainty can degrade under dataset shift [9]. Galil, Dabbah, and El-Yaniv demonstrate that selective-prediction and uncertainty performance can vary substantially even among strong image classifiers and emphasize metrics such as risk-coverage and AURC [10]. Ding et al. similarly distinguish confidence calibration from selective-prediction quality and caution that common uncertainty metrics capture different properties [18]. For FST, this means that a model score should not be called a reliable uncertainty estimate merely because it appears numerically plausible. It must be tested against errors on an independently defined evaluation population.

---

## 3. Methods

### 3.1 Study design

The present work is a retrospective evidence audit of a championship-derived FST candidate dataset, followed by specification of the stronger benchmark required for event-level and uncertainty-aware evaluation.

The empirical unit in the current analysis is a **candidate clip surfaced for human validation**. This is different from an independently enumerated event opportunity. The distinction governs the estimands that can be reported.

The analysis is restricted to FST.ai and FST.ai 2.0. Broader sport-intelligence platforms and unrelated modules are outside scope.

### 3.2 Source data and annotation semantics

The source annotation table contains 546 candidate records associated with 74 recorded match identifiers. Each row includes:

- match identifier;
- clip name;
- candidate-validation label: True Positive or False Positive;
- human confidence: High or Medium;
- difficulty: Easy, Medium, or Hard;
- action label: turning head kick, non-turning head kick, or uncertain;
- contact annotation: clear, light, or uncertain;
- visibility: good, moderate, or partial occlusion.

The source annotation manual defines a True Positive as a system-detected valid head kick and a False Positive as a system-detected head kick that is not a real head kick. We therefore interpret the table as **human validation of system-proposed candidates**, not as an independent census of all valid head-kick events in the underlying bouts.

This matters statistically. A candidate table can contain TP and FP labels among surfaced detections while containing no direct information about genuine events the model failed to surface. Such missed events are false negatives, and they are required for recall and F1.

Human confidence is also assigned a specific evidential role. It records the annotator/reference confidence associated with a row. It is not a numerical output produced by FST, and it is not treated as epistemic uncertainty.

### 3.3 Evidence layers

To prevent leakage between reference information and model output, the evaluation framework separates four layers:

1. **Reference evidence:** independently adjudicated events or labels.
2. **Model output:** predictions and numerical uncertainty generated by a frozen FST configuration without access to reference labels.
3. **Context annotation:** visibility, difficulty, contact quality, ambiguity, or other independently assigned evidence conditions.
4. **Derived outcomes:** TP, FP, FN, error indicators, risk, coverage, latency differences, and summary metrics computed after the first three layers are frozen.

The current candidate dataset primarily occupies layers 1 and 3 for a selected set of model-proposed candidates. It does not contain the complete event-level reference layer needed for FN enumeration, and it does not contain a verified numerical FST uncertainty output.

### 3.4 Data audit and canonicalization

The raw annotation layer was preserved. Corrections were represented as audit metadata rather than applied destructively.

The audit identified:

- one exact repeated match/clip key: 624-506 / clip_001.mp4;
- a source note indicating that 624-548 and 624-549 correspond to the same bout;
- a note stating that 624-546 does not exist immediately before rows labelled 624-546;
- a later note stating that 624-531 does not exist despite earlier rows carrying that identifier;
- a note that 624-530 is absent;
- repeated heading typo 'MATH' instead of 'MATCH' in part of the 625-series section.

Only the exact repeated row was excluded from the canonical candidate population. Contradictory match-number notes were preserved as audit flags. The two identifiers explicitly described as one bout were assigned a common bout-cluster identifier for dependence-aware inference.

The resulting canonical population contains 545 candidate records grouped into 73 bout clusters.

### 3.5 Primary descriptive estimand

For the canonical candidate population, we define the **candidate-confirmation fraction**

\[
q=\frac{N_{\mathrm{TP}}}{N_{\mathrm{TP}}+N_{\mathrm{FP}}}.
\]

The terminology is deliberate. Numerically, this ratio resembles precision, but we do not label it precision because the complete candidate-generation and sampling protocol has not yet been reconstructed sufficiently to assert that the table is an exhaustive, unbiased set of all emitted FST detections for the target population.

The candidate-confirmation fraction does not estimate recall, because the denominator for recall requires false negatives:

\[
\mathrm{Recall}=\frac{TP}{TP+FN}.
\]

For the same reason, F1 is not reported from the present candidate table.

### 3.6 Dependence-aware interval estimation

Multiple candidate clips can arise from the same bout, so clip observations are not treated as independent tournament-level observations. We therefore report a delete-one-bout cluster jackknife interval for \(q\).

Let \(G\) be the number of bout clusters and \(q_{(-g)}\) the estimate after omitting cluster \(g\). With

\[
\bar q_{(-\cdot)}=\frac{1}{G}\sum_{g=1}^{G}q_{(-g)},
\]

the jackknife standard error is

\[
SE_J=
\sqrt{\frac{G-1}{G}
\sum_{g=1}^{G}
\left(q_{(-g)}-\bar q_{(-\cdot)}\right)^2 }.
\]

We report the normal 95% interval

\[
q\pm1.96SE_J.
\]

This interval addresses within-bout dependence in the descriptive candidate population. It does not change the population definition and does not convert a candidate-only sample into a complete event benchmark.

### 3.7 Annotation-structure audit

To determine whether the contextual fields can be interpreted independently, we tabulate marginal distributions and the full joint pattern across:

\[
(\text{candidate label},\text{human confidence},\text{difficulty},
\text{action label},\text{contact},\text{visibility}).
\]

The purpose is not to fit a predictive model from these annotations. Instead, the audit asks whether they vary independently enough to support statements such as 'partial occlusion causes FST errors' or 'human confidence validates FST uncertainty'. If outcome and context fields are nearly deterministic functions of one another, such interpretations would be circular.

For the same reason, subgroup confirmation fractions are reported descriptively without causal language or null-hypothesis tests.

### 3.8 Prespecified event-level benchmark

The stronger FST efficacy benchmark is defined separately from the current audit.

First, an independent 'ground_truth_events.csv' must enumerate all eligible reference events, including events missed by FST. Second, a frozen 'fst_ssac_predictions.csv' must contain all model predictions generated without access to the reference labels. Third, deterministic one-to-one matching must derive TP, FP, and FN using a declared temporal tolerance and class rule.

Only then are standard event-level metrics reported:

\[
\mathrm{Precision}=\frac{TP}{TP+FP},
\qquad
\mathrm{Recall}=\frac{TP}{TP+FN},
\]

\[
F_1=\frac{2PR}{P+R}.
\]

The matching tolerance and any uncertainty threshold used for a headline test result must be fixed outside the final test population. Sensitivity analysis should repeat evaluation under additional defensible temporal tolerances.

### 3.9 Prespecified selective-prediction benchmark

Let \(U(x)\) denote numerical uncertainty produced by the frozen FST implementation, with larger values indicating greater uncertainty. For threshold \(\tau\),

\[
C(\tau)=P(U(x)\le\tau)
\]

defines coverage, and

\[
R(\tau)=P(\text{error}\mid U(x)\le\tau)
\]

defines selective risk among retained AI-supported cases.

The preferred evaluation unit is an eligible IVR request or decision opportunity if FST produces a score for every such case. This permits the deferral analysis to reflect the operational decision faced by the official.

If FST uncertainty is available only for emitted detections, the interpretation is narrower. Coverage then means the fraction of emitted candidates retained, and risk is the FP fraction among those retained candidates. This **selective candidate-validation** analysis cannot evaluate false-negative deferral because missed events have no emitted candidate uncertainty score.

Human High/Medium confidence is excluded from both formulations.

### 3.10 Reproducibility

The public repository contains the de-identified raw candidate table, the exact-deduplicated canonical table, the audit log, machine-readable summaries, an evidence ledger, the statistical analysis plan, event-matching and evaluation scripts, data validators, a split-leakage policy, and a one-command reproduction entry point.

Automated GitHub Actions checks compile the evaluation scripts, run event-matching and metric smoke tests, test risk-coverage behavior, regenerate the public annotation audit, and compare the reproduced evidence with the checked-in result tables.

Production FST source code and model weights are not required to reproduce the present annotation-audit results. They remain separate from the public research package. Raw championship video is also not redistributed where broadcast, event, privacy, or athlete-likeness rights have not been established.

---

## 4. Results

### 4.1 Population and primary descriptive result

The raw table contains 546 candidate records: 450 TP-labelled and 96 FP-labelled. One exact duplicate TP-labelled record was excluded, producing a canonical population of 545 candidates: 449 TP-labelled and 96 FP-labelled.

**Table 1. Audited candidate population**

| Quantity | Result |
|---|---:|
| Raw candidate records | 546 |
| Recorded match identifiers | 74 |
| Bout clusters after documented ID linkage | 73 |
| Exact duplicate match+clip keys | 1 |
| Canonical candidate records | 545 |
| Canonical TP-labelled candidates | 449 |
| Canonical FP-labelled candidates | 96 |
| Candidate-confirmation fraction | 82.39% |
| Bout-cluster jackknife 95% CI | 81.16%–83.61% |

The canonical candidate-confirmation fraction is therefore

\[
q=\frac{449}{545}=0.8239.
\]

The bout-cluster jackknife standard error is 0.00624, giving a 95% interval of 81.16% to 83.61%.

This result answers a narrow question: among the canonical set of surfaced and annotated FST candidates, 82.39% were human-confirmed as valid according to the source annotation label. It does not estimate the fraction of all true head-kick events detected by FST.

### 4.2 Marginal annotation structure

The raw annotation distributions are shown in Table 2.

**Table 2. Marginal distributions in the raw candidate table (N = 546)**

| Field | Category | n | Share |
|---|---|---:|---:|
| Candidate label | True Positive | 450 | 82.42% |
|  | False Positive | 96 | 17.58% |
| Human confidence | High | 294 | 53.85% |
|  | Medium | 252 | 46.15% |
| Difficulty | Easy | 172 | 31.50% |
|  | Medium | 152 | 27.84% |
|  | Hard | 222 | 40.66% |
| Visibility | Good | 172 | 31.50% |
|  | Moderate | 152 | 27.84% |
|  | Partial occlusion | 222 | 40.66% |
| Action label | Turning head kick | 293 | 53.66% |
|  | Non-turning head kick | 157 | 28.75% |
|  | Uncertain | 96 | 17.58% |
| Contact | Clear | 300 | 54.95% |
|  | Light | 150 | 27.47% |
|  | Uncertain | 96 | 17.58% |

Several counts are identical across conceptually distinct variables. Hard difficulty and partial occlusion each contain 222 rows. The uncertain-action and uncertain-contact categories each contain exactly 96 rows, equal to the number of FP-labelled candidates. These equalities motivate examination of the joint distribution rather than separate interpretation of each annotation field.

### 4.3 Joint annotation patterns

The joint distribution is highly concentrated.

**Table 3. Joint annotation patterns in the raw candidate table**

| Candidate label | Human confidence | Difficulty | Action | Contact | Visibility | n | Share |
|---|---|---|---|---|---|---:|---:|
| TP | High | Easy | turning | clear | good | 164 | 30.04% |
| TP | Medium | Medium | non-turning | light | moderate | 149 | 27.29% |
| TP | High | Hard | turning | clear | partial occlusion | 126 | 23.08% |
| FP | Medium | Hard | uncertain | uncertain | partial occlusion | 96 | 17.58% |
| TP | Medium | Easy | non-turning | clear | good | 7 | 1.28% |
| TP | High | Medium | turning | clear | moderate | 3 | 0.55% |
| TP | High | Easy | non-turning | light | good | 1 | 0.18% |

The four most common patterns account for

\[
\frac{535}{546}=97.99\%
\]

of all raw records.

All 96 FP-labelled candidates have exactly the same combination of contextual annotations:

\[
(\text{Medium human confidence},\text{Hard},
\text{uncertain action},\text{uncertain contact},
\text{partial occlusion}).
\]

The false candidates are therefore not dispersed uniformly across the annotation space. They are concentrated in one difficult evidence state.

### 4.4 Descriptive visibility and difficulty strata

After exact deduplication, the candidate-confirmation fractions by visibility are:

**Table 4. Candidate confirmation by visibility in the canonical population**

| Visibility | n | TP-labelled | FP-labelled | Candidate confirmation |
|---|---:|---:|---:|---:|
| Good | 171 | 171 | 0 | 100.00% |
| Moderate | 152 | 152 | 0 | 100.00% |
| Partial occlusion | 222 | 126 | 96 | 56.76% |

The same numerical split appears for difficulty because Easy is coupled to good visibility, Medium to moderate visibility, and Hard to the two partial-occlusion patterns in this annotation table.

These strata are descriptive. The data do not support a causal statement that partial occlusion alone reduces FST performance from 100% to 56.76%, because the annotations for difficulty, action ambiguity, contact ambiguity, visibility, and correctness are strongly entangled.

### 4.5 Human confidence cannot validate model uncertainty

The canonical human-confidence strata are:

- High: 293 TP-labelled, 0 FP-labelled;
- Medium: 156 TP-labelled, 96 FP-labelled.

The corresponding candidate-confirmation fractions are 100% and 61.90%. Taken without provenance, this pattern could be misread as evidence that 'uncertainty predicts error'. It is not.

The confidence field is a human annotation, and it co-varies almost deterministically with the same fields that define the candidate label. The appropriate interpretation is therefore narrower: the annotation process encodes a strong relationship between perceived evidence difficulty and candidate correctness. It does **not** establish that FST's own epistemic uncertainty is calibrated or useful for deferral.

---

## 5. Discussion

### 5.1 What the 82.39% result means

The candidate-confirmation fraction is a valid descriptive result for the selected candidate population. It quantifies how often candidate detections in the audited table were confirmed by the human label after exact deduplication and bout-level dependence was acknowledged.

The same number should not be promoted into a stronger metric without additional evidence. In particular, it is not an estimate of recall, because false negatives are not observed. It is not F1. It is not a complete measure of match-level or tournament-level accuracy. And although it is algebraically identical to TP/(TP+FP), calling it 'precision' would imply more about the candidate-generation and sampling process than the available provenance currently supports.

This distinction is important for applied sports analytics. Operational data are often collected around system interventions: alerts, reviews, or surfaced events. Such datasets can be highly informative while still being conditioned on the system that generated them. A retrospective evaluation must preserve that conditioning rather than silently treating selected events as if they were a random or complete sample of all event opportunities.

### 5.2 The difficult tail is real, but the current labels cannot calibrate it

The most striking empirical pattern is not the overall 82.39% confirmation fraction. It is the concentration of every FP-labelled candidate in one difficult annotation state involving partial occlusion, uncertain action type, uncertain contact, Hard difficulty, and Medium human confidence.

Operationally, this is exactly the region in which a human-in-the-loop system would want a deferral mechanism to become cautious. The observation is also directionally consistent with the Paris 2024 Taekwondo study, where the small set of AI-referee disagreements was concentrated in minimal-contact and occluded situations [11].

However, the current FST annotations cannot be used to claim that the model already knows this. The contextual variables are too strongly coupled to the candidate outcome. They may have been assigned as a coherent human description of an ambiguous case rather than as independent measurements collected before correctness was known. The correct scientific response is therefore not to discard the fields, but to use them as descriptive context while requiring a separate model-generated uncertainty signal for calibration or selective-prediction analysis.

### 5.3 Why deferral is the correct operational target

A sports-officiating AI does not need to maximize autonomous coverage. In many settings, the cost of a wrong confident recommendation is higher than the cost of explicitly routing a difficult case to the human official.

This creates a natural risk-coverage objective. At 100% coverage the system attempts to support every eligible case. As the uncertainty threshold becomes stricter, coverage falls. The useful question is whether retained error falls fast enough to justify that reduction in coverage.

A strong FST result would therefore look different from a conventional 'accuracy improved' statement. It would show, for example, that a prespecified uncertainty threshold retains a useful share of cases while materially lowering error relative to full coverage, and that deferred cases are enriched for genuinely ambiguous or occluded evidence. Such a result would directly connect epistemic uncertainty to an officiating workflow.

This interpretation also clarifies the role of the human. Deferral is not an AI failure in the same sense as a wrong autonomous decision. It is a routing action. The official remains responsible for the final call, while the AI's responsibility is to provide useful evidence and to avoid overstating certainty when the visual record is weak.

### 5.4 Human-AI evaluation should be composite

The human-in-the-loop literature suggests another implication. A model can have a sensible rejector and still produce a poor overall system if the human interaction is badly designed [6-8]. The final FST evaluation should therefore distinguish:

- model discrimination and event-level performance;
- uncertainty ranking and risk-coverage;
- the frequency and composition of deferrals;
- the human decision after deferral;
- the time cost of escalation;
- the way evidence and uncertainty are displayed to the official.

This is especially relevant in officiating because the human expert is not merely an interchangeable labeler. The referee or review jury operates under formal rules, time pressure, accountability, and a need to explain or defend decisions.

### 5.5 Relation to prior FST claims

The evidence audit also changes how the prior FST.ai 2.0 headline results should be used. The public paper reports strong latency and trust figures [3], but the current repository does not yet contain the raw observations needed to reconstruct all of those claims under one consistent protocol. Rather than repeat them as if independently validated here, we retain them as prior-public evidence and document the unresolved denominators and definitions in the claim ledger.

This is not a rejection of the prior findings. It is a separation of evidence roles. Once the timing records and human-study data are reconstructed, they can become valuable secondary endpoints. Review latency, for example, should be reported with a common start/end definition, sample size, paired or otherwise comparable baseline, and a distribution such as median and IQR rather than only a percentage reduction. Trust or acceptance should similarly report the respondent population, exact question, scale, and distribution.

### 5.6 Implications for sports organizations

The audit leads to five practical design requirements for sports organizations considering AI-assisted review.

**Preserve provenance.** Raw evidence, correction history, model version, thresholds, and decision logs should be retained. Silent relabeling undermines later validation.

**Evaluate the correct denominator.** Candidate confirmation and event recall answer different questions. A federation should know both how many surfaced alerts are useful and how many true review-worthy events the system misses.

**Separate human and model uncertainty.** A referee saying 'I am unsure' does not validate a model's epistemic score. Both signals may be useful, but they should be measured independently.

**Treat deferral as a designed operating mode.** A system that knows when not to recommend can be more useful than one that maximizes autonomous coverage.

**Evaluate the human-AI team.** The relevant endpoint is eventually the quality, speed, transparency, and accountability of the composite review process, not only the classifier in isolation.

These principles extend beyond Taekwondo to other sports in which video review combines uncertain visual evidence with rule-based adjudication.

---

## 6. Limitations

The study has six principal limitations.

First, the source population is candidate based. It does not independently enumerate all true head-kick events and therefore cannot support recall or F1.

Second, the original annotation protocol is not documented in sufficient detail to establish that human confidence, difficulty, action ambiguity, contact ambiguity, and visibility were assigned independently of candidate correctness. Their strong coupling limits inferential interpretation.

Third, the candidate-confirmation fraction is conditional on the mechanism that generated and selected the candidate clips. It should not be generalized to all competition actions without reconstructing that mechanism.

Fourth, model-generated FST uncertainty is not present in the released candidate table. The selective-prediction analysis in this paper is a prespecified benchmark, not a completed uncertainty result.

Fifth, the study does not claim a newly controlled review-latency or referee-trust effect. Prior-public FST.ai 2.0 figures remain separated from the present results until their source observations and definitions are reconciled.

Sixth, raw competition video may be subject to third-party broadcast, event, federation, privacy, or likeness rights. Ownership of the FST implementation does not automatically establish a right to redistribute all source footage.

These limitations narrow the current claims, but they also define the path to a stronger benchmark.

---

## 7. Registered Next Benchmark

The next FST evaluation should freeze three independent artifacts before headline model-performance analysis:

1. an event-level ground-truth census covering all eligible review events in the test population;
2. a frozen FST/FST.ai 2.0 prediction export produced without reference-label access;
3. a numerical model-generated uncertainty or evidence score at a declared evaluation unit.

The benchmark should then report TP, FP, FN, precision, recall, F1, and temporal localization error with bout-level dependence reflected in the uncertainty intervals. Secondary analyses should include turning versus non-turning actions and independently assigned evidence conditions such as visibility and contact quality.

The uncertainty evaluation should report the full risk-coverage curve, risk at prespecified coverage values or coverage at prespecified risk values, and the composition of deferred cases. If the score is emitted only for detected candidates, the result must be labelled candidate-level selective validation rather than full decision-level deferral.

Where comparable timing data are available, review latency should be measured end-to-end using the same timing boundaries for the baseline and AI-assisted workflow. Human-study outcomes should be reported separately from model performance.

Most importantly, the final test split should remain untouched by threshold tuning, event-matching design, calibration, or error-driven model revision. Bout-level split integrity should be verified before inference, and athlete-level or competition-condition sensitivity analysis should be considered where the sample supports it.

---

## 8. Data and Code Availability

The public research package is available at:

https://github.com/KeivanShariatmadar/FST-Uncertainty-Aware-Officiating

The repository contains the data used for the current annotation-audit results in de-identified form, the canonical audited table, provenance and audit logs, machine-readable result summaries, the evidence ledger, the statistical analysis plan, matching and evaluation code, split-validation tools, and automated reproducibility checks.

The current results can be regenerated from the released data with the public reproduction runner. The repository does not represent production FST source code, private model weights, credentials, or uncleared third-party video as open research artifacts.

---

## 9. Conclusion

For AI-assisted officiating, the central question is not simply whether a model can classify an action. It is whether the system can provide useful evidence when the case is well supported and recognize when the evidence is too weak for a confident recommendation.

Our audit of 546 championship-derived FST candidate records produced a canonical set of 545 candidates, of which 449 were TP-labelled and 96 FP-labelled. The resulting candidate-confirmation fraction is 82.39% with a bout-cluster jackknife 95% interval of 81.16%–83.61%. More importantly, 97.99% of the raw records fall into four repeated joint annotation patterns, and all 96 FP-labelled candidates occupy the same difficult, ambiguous, partially occluded state.

That concentration identifies the operationally difficult tail of the candidate evidence, but the same structural regularity prevents the human annotation fields from being used as an independent calibration test for FST epistemic uncertainty. The appropriate next step is therefore not to relabel human confidence as model confidence, nor to infer recall from a candidate-only table. It is to compare independently enumerated reference events with frozen FST outputs and evaluate numerical model uncertainty through a prespecified risk-coverage analysis.

For sports organizations, this reframes trustworthy AI-assisted review as a controlled allocation problem: automate support where the evidence is strong, expose uncertainty where it is not, and preserve the human official as the final authority for ambiguous cases.

---

## References

[1] World Taekwondo. *Competition Rules & Interpretation*. World Taekwondo, rules in force September 30, 2024. Article 21: Instant Video Replay. https://www.worldtaekwondo.org/att_file/documents/WT%20Competition%20Rules%20and%20Interpretation%20%28September%2030%2C%202024%29.pdf

[2] K. Shariatmadar and A. Osman. “AI-Enhanced Precision in Sport Taekwondo: Increasing Fairness, Speed, and Trust in Competition (FST.ai).” arXiv:2507.14657, 2025. https://doi.org/10.48550/arXiv.2507.14657

[3] K. Shariatmadar, A. Osman, R. Ray, U. Dildar, and K. Kim. “FST.ai 2.0: An Explainable AI Ecosystem for Fair, Fast, and Inclusive Decision-Making in Olympic and Paralympic Taekwondo.” arXiv:2510.18193, 2025. https://doi.org/10.48550/arXiv.2510.18193

[4] R. El-Yaniv and Y. Wiener. “On the Foundations of Noise-Free Selective Classification.” *Journal of Machine Learning Research*, 11:1605–1641, 2010.

[5] Y. Geifman and R. El-Yaniv. “Selective Classification for Deep Neural Networks.” *Advances in Neural Information Processing Systems*, 30:4878–4887, 2017.

[6] D. Madras, T. Pitassi, and R. Zemel. “Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer.” *Advances in Neural Information Processing Systems*, 31, 2018.

[7] H. Mozannar and D. Sontag. “Consistent Estimators for Learning to Defer to an Expert.” *Proceedings of the 37th International Conference on Machine Learning*, PMLR 119:7076–7087, 2020.

[8] E. Bondi, R. Koster, H. Sheahan, M. Chadwick, Y. Bachrach, T. Cemgil, U. Paquet, and K. Dvijotham. “Role of Human-AI Interaction in Selective Prediction.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 36(5):5286–5294, 2022. https://doi.org/10.1609/aaai.v36i5.20465

[9] Y. Ovadia, E. Fertig, J. Ren, Z. Nado, D. Sculley, S. Nowozin, J. Dillon, B. Lakshminarayanan, and J. Snoek. “Can You Trust Your Model’s Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift.” *Advances in Neural Information Processing Systems*, 32, 2019.

[10] I. Galil, M. Dabbah, and R. El-Yaniv. “What Can We Learn From the Selective Prediction and Uncertainty Estimation Performance of 523 ImageNet Classifiers?” *International Conference on Learning Representations*, 2023. arXiv:2302.11874.

[11] Y. Zhang, R. Qu, and O. Girard. “Faster, more accurate? A feasibility study on replacing human judges with artificial intelligence in video review for the Paris Olympics Taekwondo competition.” *Frontiers in Sports and Active Living*, 7:1632326, 2025. https://doi.org/10.3389/fspor.2025.1632326

[12] D. Martín Moncunill, D. Sampedro Lirio, and M. Á. Bravo Hijón. “Possibilities of Artificial Intelligence in Sports Refereeing: An Exploratory Study Contrasting the Literature Review with Expert-Perceived Opportunities.” *Multimodal Technologies and Interaction*, 10(3):30, 2026. https://doi.org/10.3390/mti10030030

[13] M. Zhekambayeva, M. Yerekesheva, N. Ramashov, Y. Seidakhmetov, and B. Kulambayev. “Designing an artificial intelligence-powered video assistant referee system for team sports using computer vision.” *Retos*, 61, 2024. https://doi.org/10.47197/retos.v61.110300

[14] J. Lee and H. Jung. “TUHAD: Taekwondo Unit Technique Human Action Dataset with Key Frame-Based CNN Action Recognition.” *Sensors*, 20(17):4871, 2020. https://doi.org/10.3390/s20174871

[15] E. Quinn and N. Corcoran. “Automation of Computer Vision Applications for Real-time Combat Sports Video Analysis.” *European Conference on the Impact of Artificial Intelligence and Robotics*, 4(1), 2022. https://doi.org/10.34190/eciair.4.1.930

[16] F.-E. Ait-Bennacer, A. Aaroud, K. Akodadi, and B. Cherradi. “Applying Deep Learning and Computer Vision Techniques for an e-Sport and Smart Coaching System Using a Multiview Dataset: Case of Shotokan Karate.” *International Journal of Online Engineering*, 18(12), 2022. https://doi.org/10.3991/ijoe.v18i12.30893

[17] S. Yan, Y. Xiong, and D. Lin. “Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1), 2018.

[18] Y. Ding, J. Liu, J. Xiong, and Y. Shi. “Revisiting the Evaluation of Uncertainty Estimation and Its Application to Explore Model Complexity-Uncertainty Trade-Off.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, 2020.

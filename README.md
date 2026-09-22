# FST: Uncertainty-Aware AI-Assisted Officiating in Competitive Taekwondo

This repository accompanies the SSAC27 research submission:

**Uncertainty-Aware AI-Assisted Video Review for Faster and More Reliable Officiating in Competitive Taekwondo**

**Authors:** Keivan Shariatmadar¹ · Ahmad Osman¹ · Ramin Rey²  
¹ htw saar – University of Applied Sciences, Saarbrücken, Germany  
² Austrian Taekwondo Federation (AUT), Austria

## Purpose

FST.ai investigates human-in-the-loop artificial intelligence for assisting video-review decisions in competitive Taekwondo. This SSAC research package is deliberately restricted to the FST.ai / FST.ai 2.0 officiating research line. It focuses on difficult head-kick review, action recognition and classification, review latency, interpretable evidence, and decision-making under epistemic uncertainty.

The central question is not whether AI can replace a referee, but whether AI-assisted review can improve the speed, reliability, transparency, and auditability of difficult officiating decisions while preserving final human authority.

## What is public here

This repository provides research documentation, data-availability information, evaluation definitions, reproducibility information, bibliographic references, and SSAC submission materials. Verified and legally releasable derived evaluation data and reproduction scripts will be added only after provenance, rights, privacy, and statistical checks.

## Human-in-the-loop principle

FST.ai is decision support. AI outputs are evidence and recommendations for authorized human officials; they are not autonomous competition decisions. Ambiguous or insufficient-evidence cases remain subject to human adjudication.

## Open research does not mean open implementation

Public availability of this repository **does not constitute an open-source release of the operational FST.ai system**. Proprietary source code, production models/weights, non-public architecture, deployment configurations, credentials, confidential technical information, and protected implementation know-how are outside this repository.

Third-party competition footage is not redistributed unless the authors have the legal authority and appropriate permissions to do so. See `DATA_STATEMENT.md` and `IP_AND_LICENSING.md`.

## Repository map

- `DATA_STATEMENT.md` — provenance, availability, restrictions, and release plan
- `REPRODUCIBILITY.md` — reproducibility scope and protocol
- `IP_AND_LICENSING.md` — licensing and proprietary-implementation boundary
- `CITATION.cff` — citation metadata for this SSAC research package
- `paper/` — abstract and submission notes
- `data/` — data documentation and, when cleared, derived artifacts
- `evaluation/` — evaluation protocol and metric definitions
- `references/` — FST.ai and FST.ai 2.0 publication record

## Repository status

**Stage 1 — SSAC abstract submission:** documentation, provenance and rights statements, metric definitions, publication references, and abstract.

**Stage 2 — invited full-paper stage, if applicable:** verified and legally releasable derived evaluation data and reproduction scripts after an evidence audit.

No empty or placeholder dataset should be interpreted as evidence for a quantitative claim.

## Contact

Scientific correspondence: Keivan Shariatmadar, htw saar – University of Applied Sciences.

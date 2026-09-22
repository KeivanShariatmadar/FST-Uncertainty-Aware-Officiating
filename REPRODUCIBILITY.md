# Reproducibility Statement

## Objective

The reproducibility objective is to make the SSAC evaluation transparent enough that an independent researcher can understand the experimental population, outcome definitions, aggregation rules, and statistical calculations, and can reproduce released metrics from legally releasable derived artifacts.

This is distinct from reproducing the proprietary operational FST.ai implementation.

## Stage 1: abstract submission

The repository documents:

1. the research question and scope;
2. the status and restrictions of source data;
3. the evaluation dimensions and metric definitions;
4. the public FST.ai / FST.ai 2.0 research record; and
5. the boundary between reproducible research artifacts and proprietary implementation.

## Stage 2: invited full-paper package

Before full-paper submission, the intended reproducibility package will be generated from an evidence audit. For every reported quantitative result, the audit will record:

- source experiment or deployment;
- evaluation unit (for example, review, action, clip, bout, or respondent);
- sample size and denominator;
- inclusion/exclusion rules;
- reference/ground-truth procedure;
- baseline definition;
- point estimate and, where appropriate, uncertainty interval;
- aggregation method;
- missing-data handling;
- provenance of the released artifact; and
- legal/release status.

Where legally permissible, derived data and scripts will be supplied so that reported tables and figures can be regenerated.

## Reproducibility boundary

Reproduction of published evaluation calculations does not require publication of production source code, trained production weights, private deployment configuration, credentials, or protected implementation know-how. Those materials are not part of this public package.

## No synthetic substitution

If an underlying observation cannot legally be released, this repository will not substitute synthetic observations and present them as original evidence. Any simulated or illustrative data, if later included for software demonstration, will be explicitly labelled and will not be used as evidentiary support for empirical claims.

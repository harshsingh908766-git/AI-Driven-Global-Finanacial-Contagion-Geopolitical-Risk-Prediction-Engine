# Model Acceptance Criteria

## 1. Purpose

This document defines the minimum research and validation
requirements that a model must satisfy before it can be
declared successful within the AI Financial Contagion
Research Framework.

A model must not be declared successful solely because
it achieves a high accuracy score.

Model acceptance requires evidence of reliable
out-of-sample performance, information-leakage control,
crisis-event detection, robustness and reproducibility.

## 2. Acceptance Principle

Model acceptance must be based on multiple dimensions
of performance and research integrity.

No single evaluation metric is sufficient to establish
the scientific validity of a financial contagion model.

## 3. Reliable Out-of-Sample Performance

The model must demonstrate reliable performance on
observations that were not used during model fitting
or hyperparameter selection.

Required checks:

- Chronological out-of-sample evaluation
- Appropriate validation design
- Consistent performance across test periods
- Comparison with relevant baseline models
- Evaluation under different market conditions
- Performance uncertainty reporting

Results from training data alone are not sufficient
for model acceptance.

## 4. Information Leakage Prevention

The experimental pipeline must demonstrate that
future information has not entered historical predictions.

Required checks:

- No random temporal mixing of training and test data
- Point-in-time data availability controls
- No future-derived feature values
- No target leakage
- No test-set-driven feature selection
- No test-set hyperparameter tuning
- Correct preprocessing within each training fold
- Appropriate treatment of revised economic data

Any material information leakage must result in
rejection or redesign of the affected experiment.

## 5. Crisis-Event Detection

The model must be evaluated on its ability to identify
financial stress and contagion events.

Required checks:

- Crisis-event recall
- Precision during crisis periods
- False alarm rate
- Missed crisis-event analysis
- Early-warning lead time
- Performance during high-stress regimes
- Crisis and non-crisis comparison

A model with high overall accuracy but poor crisis
detection must not automatically be accepted.

## 6. Robustness Across Periods and Countries

The model must be examined across different
historical periods and geographic settings.

Required checks:

- Different market regimes
- Multiple economic cycles
- Advanced and emerging economies
- Country-held-out validation, where feasible
- Alternative crisis windows
- Alternative feature sets
- Alternative model specifications
- Sensitivity to missing observations

Geographic and temporal generalisation must be
reported with appropriate limitations.

## 7. Statistical Uncertainty Reporting

Performance estimates must include suitable
uncertainty information.

Where appropriate, report:

- Confidence intervals
- Bootstrap uncertainty estimates
- Statistical significance tests
- Model comparison tests
- Calibration uncertainty
- Sample size and event count

A point estimate without uncertainty information
may be insufficient for strong research conclusions.

## 8. Reproducible Experimental Results

Every accepted experiment must provide sufficient
information for independent verification.

Required records:

- Dataset version
- Data extraction date
- Feature definitions
- Training period
- Test period
- Model configuration
- Random seed
- Software versions
- Evaluation metrics
- Experiment identifier
- Git commit hash
- Experiment logs and output references

Refer to `docs/reproducibility.md` and
`experiments/experiment_template.yaml`.

## 9. Baseline Comparison

The proposed model should be compared against
appropriate baseline methods.

Potential baselines include:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost
- Econometric benchmark models

Only models actually implemented and evaluated
may be reported as experimental comparisons.

## 10. Acceptance Decision

Each criterion must be assigned a documented status:

- PASS: Evidence satisfies the defined requirement.
- FAIL: Evidence shows that the requirement is not satisfied.
- NOT TESTED: The requirement has not been evaluated.
- INCONCLUSIVE: Available evidence is insufficient.

A model must not receive final research acceptance
if a critical criterion is marked FAIL or NOT TESTED.

## 11. Acceptance Report

Every final acceptance report should document:

- Model and experiment identifier
- Dataset and test-period details
- Evaluation results
- Crisis-event detection results
- Leakage audit findings
- Robustness findings
- Statistical uncertainty
- Reproducibility evidence
- Known limitations
- Final acceptance decision

## 12. Research Integrity

Acceptance must reflect actual experimental evidence.

No performance score, statistical result, crisis
detection capability or validation outcome may be
invented or presented as completed without evidence.

A proposed criterion is not the same as a demonstrated result.

## 13. Final Acceptance Statement

The model may be considered research-validated only
after the relevant acceptance requirements have been
tested, documented and independently reviewed.

Research validation does not imply guaranteed
forecasting accuracy, investment suitability or
operational readiness.
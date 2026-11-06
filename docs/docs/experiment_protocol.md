# Experimental Research Protocol

## 1. Objective

This protocol establishes a consistent workflow for
conducting, evaluating and documenting experiments
within the AI Financial Contagion Research Framework.

## 2. Experiment Registration

Before running an experiment, create a unique experiment ID.

Example:

EXP-2026-001

Complete the experiment record in:

`experiments/experiment_template.yaml`

## 3. Dataset Preparation

Document the following:

- Dataset name and version
- Data provider
- Extraction date
- Historical coverage
- Country coverage
- Observation frequency
- Data availability timestamps
- Data licensing restrictions

Check missing values, duplicate records,
inconsistent timestamps and data revisions.

## 4. Feature Engineering

For every feature:

- Define its mathematical meaning.
- Record its source.
- Specify its unit.
- Document transformations.
- Record missing-value treatment.
- Check point-in-time availability.

All transformations must be fitted using
training data only where applicable.

## 5. Data Partitioning

Use chronological data partitioning.

Maintain separate datasets for:

- Training
- Validation
- Final testing

The final test period must not be used
for model selection or hyperparameter tuning.

Record the exact start and end dates
of each partition.

## 6. Model Training

Document:

- Model architecture
- Input features
- Target variable
- Hyperparameters
- Random seed
- Software environment
- Training duration
- Model checkpoint

Retain experiment logs and configuration files.

## 7. Model Evaluation

Evaluate the model using appropriate metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Brier score
- Log loss
- False alarm rate
- Crisis-event detection rate
- Early-warning lead time

Select metrics according to the research objective
and the frequency of crisis events.

## 8. Robustness Analysis

Where data availability permits, evaluate:

- Alternative historical periods
- Different countries
- Alternative feature groups
- Different model specifications
- Crisis and non-crisis regimes
- Sensitivity to missing data
- Alternative decision thresholds

## 9. Statistical Analysis

Report suitable confidence intervals,
uncertainty estimates and statistical tests.

Do not interpret a small performance difference
as meaningful without appropriate evidence.

## 10. Experiment Archiving

Store the following:

- Experiment configuration
- Dataset reference
- Feature definitions
- Model checkpoint
- Predictions
- Evaluation metrics
- Execution logs
- Git commit hash
- Final experiment report

Do not commit confidential, restricted or
unlicensed raw datasets.

## 11. Final Review

Review the experiment against:

`docs/acceptance_criteria.md`

Record PASS, FAIL, NOT TESTED or INCONCLUSIVE
for each applicable criterion.

## 12. Research Reporting

Clearly distinguish:

- Proposed methodology
- Implemented methodology
- Completed experiments
- Observed results
- Limitations
- Future research

No experiment should be described as completed
until its execution and results are documented.
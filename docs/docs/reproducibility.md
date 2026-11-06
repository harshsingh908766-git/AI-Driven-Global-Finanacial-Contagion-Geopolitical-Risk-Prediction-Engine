# Research Reproducibility Framework

## 1. Purpose

This document defines the metadata, experimental records and software
environment required to reproduce the experiments conducted within the
AI-Driven Global Financial Contagion and Geopolitical Risk Prediction Engine.

The objective is to make every experiment traceable, auditable and
independently reproducible.

## 2. Dataset Version

Every experiment must record the exact dataset version used.

Required information:

- Dataset name
- Dataset version or release identifier
- Dataset provider
- Data coverage
- Geographic coverage
- Frequency of observations
- Data licensing information
- Dataset checksum, where available

Dataset version must not be assumed or invented.

## 3. Data Extraction Date

Record the date on which the dataset was extracted or downloaded.

Required fields:

- Extraction date
- Extraction time and timezone, where available
- Source publication date
- Data retrieval timestamp
- Data revision or vintage
- Data preprocessing date

For revised economic and financial data, preserve the historical
vintage whenever possible to reduce look-ahead bias.

## 4. Feature Definitions

Every model feature must have a documented definition.

For each feature, record:

- Feature name
- Mathematical or operational definition
- Unit of measurement
- Observation frequency
- Data source
- Transformation method
- Missing-value treatment
- Availability timestamp
- Expected direction of relationship, if theoretically justified

Feature definitions must remain consistent between training,
validation and testing.

## 5. Training Period

Record the exact training period.

Required fields:

- Training start date
- Training end date
- Observation frequency
- Number of observations
- Countries or markets included
- Target variable definition

The training period must contain only information available
at the relevant historical prediction timestamps.

## 6. Test Period

Record the exact out-of-sample test period.

Required fields:

- Test start date
- Test end date
- Number of observations
- Countries or markets included
- Forecast horizon
- Crisis and non-crisis coverage

The final test dataset must remain isolated from model fitting,
feature selection and hyperparameter tuning.

## 7. Model Configuration

Record the complete configuration of each model.

Examples of configuration fields:

- Model architecture
- Input features
- Target variable
- Forecast horizon
- Hyperparameters
- Optimizer
- Learning rate
- Batch size
- Number of epochs
- Regularization settings
- Decision threshold
- Model checkpoint identifier

Only record parameters actually used in an experiment.

## 8. Random Seed

Record all random seeds used by the experiment.

Example:

- Python random seed
- NumPy random seed
- Machine learning framework seed
- Data splitting seed

A fixed random seed improves repeatability but does not guarantee
identical results across all hardware and software environments.

## 9. Software Versions

Record the software environment.

Required information:

- Python version
- Operating system
- NumPy version
- Pandas version
- Scikit-learn version
- PyTorch or TensorFlow version, if used
- NetworkX version, if used
- CUDA version, if applicable
- Git commit hash
- Dependency lockfile or environment specification

Do not report software versions that have not been verified.

## 10. Evaluation Metrics

Record all evaluation metrics used in each experiment.

Recommended metrics:

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
- Calibration error

Metric selection must reflect the research objective,
class imbalance and cost of missed crisis events.

## 11. Experiment Identifier

Every experiment must have a unique identifier.

Example format:

EXP-2026-001

Record:

- Experiment identifier
- Experiment name
- Execution date
- Research objective
- Hypothesis tested
- Dataset version
- Model version
- Git commit hash
- Experiment status
- Output artifact location

## 12. Reproducibility Requirements

An experiment should be considered reproducible only when
its data references, feature definitions, code version,
model configuration and evaluation procedure are documented.

Where data cannot legally or contractually be redistributed,
provide source references, access instructions and data
transformation documentation instead.

## 13. Research Integrity

No dataset version, extraction date, model configuration,
training period, test period or performance result may be
fabricated.

Unknown or unavailable information must be explicitly
labelled as:

- Not yet available
- Not applicable
- Not verified

All reported results must be traceable to an actual experiment.
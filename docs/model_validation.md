# Model Validation Framework

## AI-Driven Global Financial Contagion Prediction Engine

**Version:** 0.1.0  
**Validation Status:** Proposed Experimental Protocol

---

## 1. Purpose

This document specifies the proposed validation
framework for evaluating financial contagion
prediction models.

The objective is to assess predictive performance,
generalisation, stability, robustness and
reproducibility.

## 2. Validation Principles

- Chronological data separation
- Point-in-time data integrity
- No future information leakage
- Out-of-sample evaluation
- Cross-country generalisation
- Crisis-period evaluation
- Statistical significance testing
- Reproducible experiments

## 3. Walk-Forward Validation

Walk-forward validation is the primary proposed
temporal validation methodology.

### Research Specification

Minimum training history:
5 years or approximately 1,260 trading days.

Evaluation step:
21 trading days.

Prediction horizon:
Next 30 calendar days.

At each evaluation step:

1. Use only data available up to the evaluation date.
2. Train or update the model.
3. Generate future predictions.
4. Store predicted probabilities.
5. Compare predictions against actual outcomes.
6. Advance the evaluation window.

### Proposed Hybrid Training Strategy

- Annual full retraining.
- Monthly model fine-tuning.
- Performance monitoring.
- Full retraining when degradation is detected.

### Pseudocode

```python
for evaluation_date in evaluation_dates:

    train_data = data[
        data.date <= evaluation_date
    ]

    model = train_or_update(train_data)

    future_data = get_future_evaluation_window(
        evaluation_date
    )

    predictions = model.predict_proba(
        future_data
    )

    save_predictions(
        evaluation_date,
        predictions
    )
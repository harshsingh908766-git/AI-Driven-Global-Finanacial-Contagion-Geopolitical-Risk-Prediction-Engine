from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


def evaluate_model(y_true, probabilities):

    predictions = (
        probabilities >= 0.5
    ).astype(int)

    metrics = {
        "accuracy": accuracy_score(
            y_true, predictions
        ),
        "precision": precision_score(
            y_true, predictions,
            zero_division=0
        ),
        "recall": recall_score(
            y_true, predictions,
            zero_division=0
        ),
        "f1": f1_score(
            y_true, predictions,
            zero_division=0
        )
    }

    if len(set(y_true)) == 2:
        metrics["roc_auc"] = roc_auc_score(
            y_true, probabilities
        )
    else:
        metrics["roc_auc"] = None

    return metrics
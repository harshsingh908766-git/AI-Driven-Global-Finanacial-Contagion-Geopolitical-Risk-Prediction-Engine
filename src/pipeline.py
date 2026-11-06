from src.data_generator import generate_synthetic_data
from src.features import build_features
from src.model import train_model, predict_risk, FEATURES
from src.evaluation import evaluate_model


def run_pipeline():

    df = generate_synthetic_data()

    df = build_features(df)

    split = int(len(df) * 0.80)

    train = df.iloc[:split]
    test = df.iloc[split:]

    model = train_model(
        train[FEATURES],
        train["contagion"]
    )

    probabilities = predict_risk(
        model,
        test
    )

    results = evaluate_model(
        test["contagion"].values,
        probabilities
    )

    print("\nMODEL EVALUATION")

    for metric, value in results.items():
        print(f"{metric}: {value}")

    return model, results


if __name__ == "__main__":
    run_pipeline()
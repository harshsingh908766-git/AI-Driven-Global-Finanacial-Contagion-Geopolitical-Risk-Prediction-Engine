from src.data_generator import generate_synthetic_data
from src.features import build_features


def test_data_generation():

    df = generate_synthetic_data(
        n_samples=100
    )

    assert len(df) == 100
    assert "contagion" in df.columns
    assert df["contagion"].isin([0, 1]).all()


def test_feature_engineering():

    df = generate_synthetic_data(
        n_samples=100
    )

    features = build_features(df)

    assert "total_stress" in features.columns
    assert "geo_macro_interaction" in features.columns
    assert features.isnull().sum().sum() == 0
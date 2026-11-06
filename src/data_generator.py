import numpy as np
import pandas as pd


def generate_synthetic_data(
    n_samples=1500,
    random_state=42
):
    rng = np.random.default_rng(random_state)

    dates = pd.bdate_range(
        start="2018-01-01",
        periods=n_samples
    )

    volatility = rng.uniform(0.005, 0.05, n_samples)
    geopolitical_risk = rng.uniform(0, 100, n_samples)
    macro_stress = rng.uniform(0, 100, n_samples)
    network_stress = rng.uniform(0, 100, n_samples)

    logit = (
        -4.0
        + 0.035 * geopolitical_risk
        + 0.025 * macro_stress
        + 0.030 * network_stress
        + 8.0 * volatility
    )

    probability = 1 / (1 + np.exp(-logit))

    contagion = rng.binomial(
        1, probability
    )

    return pd.DataFrame({
        "date": dates,
        "volatility": volatility,
        "geopolitical_risk": geopolitical_risk,
        "macro_stress": macro_stress,
        "network_stress": network_stress,
        "contagion": contagion
    })
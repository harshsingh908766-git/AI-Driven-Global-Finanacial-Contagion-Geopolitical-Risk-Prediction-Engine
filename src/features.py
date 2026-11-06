import pandas as pd


def build_features(df):

    data = df.copy()

    data["geo_macro_interaction"] = (
        data["geopolitical_risk"]
        * data["macro_stress"]
    ) / 100

    data["network_geo_interaction"] = (
        data["network_stress"]
        * data["geopolitical_risk"]
    ) / 100

    data["total_stress"] = (
        data["geopolitical_risk"]
        + data["macro_stress"]
        + data["network_stress"]
    ) / 3

    return data
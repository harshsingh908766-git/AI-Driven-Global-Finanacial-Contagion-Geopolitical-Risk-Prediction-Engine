from sklearn.linear_model import LogisticRegression


FEATURES = [
    "volatility",
    "geopolitical_risk",
    "macro_stress",
    "network_stress",
    "geo_macro_interaction",
    "network_geo_interaction",
    "total_stress"
]


def train_model(X_train, y_train):

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train[FEATURES], y_train)

    return model


def predict_risk(model, X):

    return model.predict_proba(
        X[FEATURES]
    )[:, 1]
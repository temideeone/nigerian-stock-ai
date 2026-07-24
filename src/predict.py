from src.train import get_feature_columns


def make_predictions(
    latest_data,
    classifier,
    regressor
):

    results = latest_data.copy()

    feature_columns = get_feature_columns(
    results
)

    results["Probability"] = (
        classifier.predict_proba(
            results[feature_columns]
        )[:, 1]
    )

    results["Predicted_Close"] = (
        regressor.predict(
            results[feature_columns]
        )
    )

    results["Expected_Return"] = (
        (
            results["Predicted_Close"]
            - results["Close"]
        )
        / results["Close"]
    ) * 100

    results["Signal"] = (
    results["Probability"]
    .apply(
        lambda x:
        "BUY"
        if x >= 0.60
        else "HOLD"
    )
)

    return results

def get_latest_data(df):

    return (
        df
        .sort_values("Date")
        .groupby("Ticker")
        .tail(1)
        .reset_index(drop=True)
    )
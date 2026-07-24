from pathlib import Path

from src.data_loader import load_all_data
from src.feature_engineering import engineer_features
from src.model_loader import load_models
from src.predict import make_predictions


BASE_DIR = Path(__file__).resolve().parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH = BASE_DIR / "outputs"


print("Loading stock data...")

df = load_all_data(
    RAW_DATA_PATH
)

print(f"{len(df)} rows loaded")


print("Engineering features...")

df = engineer_features(df)


latest_data = (
    df.sort_values(
        ["Ticker", "Date"]
    )
    .groupby("Ticker")
    .tail(1)
)

print(
    latest_data[
        ["Ticker", "Date", "Close"]
    ]
)


print(
    f"{len(latest_data)} stocks ready"
)


print("Loading models...")

xgb, xgb_reg = load_models()


print("Generating predictions...")

predictions = make_predictions(
    latest_data,
    xgb,
    xgb_reg
)


OUTPUT_PATH.mkdir(
    exist_ok=True
)

predictions.to_csv(
    OUTPUT_PATH / "latest_predictions.csv",
    index=False
)

print("Predictions saved.")



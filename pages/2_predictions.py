import streamlit as st

from src.model_loader import load_models
from src.predict import make_predictions
from src.data_loader import load_all_data

st.image(
    "assets/logo.png",
    width=220
)

st.title("🇳🇬x AI PREDICTION")

st.markdown(
    """
    Powered by XGBoost and Machine Learning.
    Predicting Tier-1 Nigerian Stocks in real time.
    """
)

# Load data
from pathlib import Path

raw_data_path = Path(
    "data/raw"
)

df = load_all_data(
    raw_data_path
) 

from src.feature_engineering import engineer_features

raw_data_path = Path("data/raw")

# Load raw data
df = load_all_data(
    raw_data_path
)

# Create all 56 features
df = engineer_features(df)

# Get the latest row for each stock
latest_data = (
    df.groupby("Ticker")
    .last()
    .reset_index()
)

import time 
with st.spinner(
    "Loading AI models..."
):


# Load models
 xgb, xgb_reg = load_models()

# Make predictions
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

predictions = pd.read_csv(
    BASE_DIR / "outputs" / "latest_predictions.csv"
)
st.success(
    "Prediction generated successfully."
)
st.info(
    "Data updated: July 2026"
)

# Display results
st.subheader("Today's AI Predictions")

st.dataframe(
    predictions[
        [
            "Ticker",
            "Probability",
            "Predicted_Close",
            "Expected_Return",
            "Signal"
        ]
    ].sort_values(
        "Probability",
        ascending=False
    ),
    use_container_width=True
)
with st.expander(
    "View Technical Indicators"
):

    st.dataframe(predictions)

st.subheader("Prediction Confidence")

st.bar_chart(
    predictions.set_index(
        "Ticker"
    )["Probability"]
)




import streamlit as st
from pathlib import Path
import pandas as pd
from src.data_loader import load_all_data
from src.feature_engineering import engineer_features
from src.model_loader import load_models
from src.predict import make_predictions

st.image(
    "assets/logo.png",
    width=220
)

st.title("💼 AI Portfolio Builder")

st.write(
    "Build an optimized Nigerian stock portfolio using AI predictions."
)


# Add users input
amount = st.number_input(
    "Investment Amount (₦)",
    min_value=10000,
    max_value=10000000,
    value=100000
)

risk = st.selectbox(
    "Risk Level",
    [
        "Conservative",
        "Moderate",
        "Aggressive"
    ]
)


#load data
raw_data_path = Path("data/raw")

df = load_all_data(
    raw_data_path
)

df = engineer_features(df)

latest_data = (
    df.groupby("Ticker")
    .last()
    .reset_index()
)

# load models
BASE_DIR = Path(__file__).resolve().parent.parent

predictions = pd.read_csv(
    BASE_DIR / "outputs" / "latest_predictions.csv"
)

# user select stock
selected_stock = st.selectbox(
    "Select a Stock",
    predictions["Ticker"].tolist()
)

# filter selected stock
stock = predictions[
    predictions["Ticker"] == selected_stock
]



# Get the values
current_price = stock["Close"].iloc[0]

predicted_price = stock["Predicted_Close"].iloc[0]

expected_return = stock["Expected_Return"].iloc[0]

signal = stock["Signal"].iloc[0]

# show metrix
col1, col2 = st.columns(2)

col1.metric(
    "Current Price",
    f"₦{current_price:.2f}"
)

col2.metric(
    "Predicted Price",
    f"₦{predicted_price:.2f}"
)

col3, col4 = st.columns(2)

col3.metric(
    "Expected Return",
    f"{expected_return:.2f}%"
)

col4.metric(
    "Signal",
    signal
)

# profit/loss calculator
investment = st.number_input(
    "Amount to Invest",
    min_value=1000,
    value=10000
)

profit = (
    investment
    * expected_return
    / 100
)

st.metric(
    "Expected Profit/Loss",
    f"₦{profit:,.2f}"
)


# Portfolio Optimizer
# Portfolio optimizer

if risk == "Conservative":

    portfolio = predictions[
        predictions["Probability"] >= 0.75
    ]

elif risk == "Moderate":

    portfolio = predictions[
        predictions["Probability"] >= 0.55
    ]

else:

    portfolio = predictions[
        predictions["Probability"] >= 0.40
    ]


# No qualifying stocks
if len(portfolio) == 0:

    st.warning(
        f"No stocks match the {risk} strategy today."
    )

    st.stop()


# Divide money equally
allocation = amount / len(portfolio)

portfolio["Allocation"] = allocation


# Expected profit
portfolio["Expected_Profit"] = (

    portfolio["Allocation"]

    * portfolio["Expected_Return"]

    / 100
)
    #else:

       #st.warning(
        #"No stocks match the selected risk level."
        #)


# Calculated expected profit
portfolio["Expected_Profit"] = (

    portfolio["Allocation"]

    * portfolio["Expected_Return"]

    / 100
)

#Display totals
st.metric(
    "Portfolio Capital",
    f"₦{amount:,.0f}"
)

st.metric(
    "Expected Profit",
    f"₦{portfolio['Expected_Profit'].sum():,.0f}"
)

# Display portfolio
st.dataframe(

    portfolio[
        [
            "Ticker",
            "Signal",
            "Probability",
            "Allocation",
            "Expected_Profit"
        ]
    ],

    use_container_width=True
)

# the graph
import plotly.express as px
fig = px.pie(

    portfolio,

    names="Ticker",

    values="Allocation",

    title="Portfolio Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# profit graph
fig = px.bar(

    portfolio,

    x="Ticker",

    y="Expected_Profit",

    title="Expected Profit by Stock"
)

st.plotly_chart(
    fig,
    use_container_width=True
)




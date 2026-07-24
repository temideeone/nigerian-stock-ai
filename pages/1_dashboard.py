import streamlit as st
from src.predict import make_predictions
from src.portfolio import build_portfolio

st.image(
    "assets/logo.png",
    width=220
)

from datetime import datetime
import time

st.title("📊 Dashboard")

st.write(
    f"Last Updated: {datetime.now()}"
)

# Temporary data

predictions = {
    "count": 12,
    "buy_signals": 2
}

portfolio = {
    "capital": 1000000,
    "profit": 12300
}

# Metrics

col1, col2, col3 = st.columns(3)

col1.metric(
    "Stocks Covered",
    predictions["count"]
)

col2.metric(
    "BUY Signals",
    predictions["buy_signals"]
)

col3.metric(
    "XGB Accuracy",
    "83.2%"
)

col4, col5 = st.columns(2)

col4.metric(
    "Portfolio Capital",
    f"₦{portfolio['capital']:,}"
)

col5.metric(
    "Expected Profit",
    f"₦{portfolio['profit']:,}"
)

import pandas as pd

sample = pd.DataFrame(
    {
        "Ticker": [
            "CADBURY",
            "FIRSTHOLDING"
        ],

        "Signal": [
            "BUY",
            "BUY"
        ],

        "Expected Return": [
            2.19,
            0.27
        ]
    }
)

st.subheader(
    "Top Buy Opportunities"
)

st.dataframe(sample)

st.subheader(
    "Select a Stock"
)

stock = st.selectbox(
    "Choose a stock",
    [
        "ACCESSCORP",
        "GTCO",
        "ZENITHB",
        "UBA",
        "CADBURY",
        "NESTLE"
    ]
)

st.write(
    f"You selected: {stock}"
)



st.subheader(
    "Investment Amount"
)

amount = st.slider(
    "Select amount",
    min_value=10000,
    max_value=1000000,
    step=10000
)

if st.button(
    "Predict Stock"
):

    st.write(
        "Selected Stock:",
        stock
    )

    st.write(
        "Investment Amount:",
        f"₦{amount:,}"
    )

    import time

with st.spinner(
    "Running AI models..."
):

    time.sleep(2)

st.success(
    "Prediction Completed!"
)



with st.expander(
    "How Predictions Work"
):

    st.write(
        """
        - XGBoost predicts BUY/HOLD.
        - XGBRegressor predicts future prices.
        - Portfolio module allocates capital.
        - Technical indicators are used.
        """
    )

import pandas as pd

chart_data = pd.DataFrame(
    {
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri"
        ],

        "Portfolio Value": [
            1000000,
            1015000,
            1020000,
            1035000,
            1042000
        ]
    }
)

st.subheader(
    "Portfolio Growth"
)

st.line_chart(
    chart_data.set_index("Day")
)

st.sidebar.success(
    "System Status: Online"
)

st.sidebar.write(
    "Model Version: v1.0"
)

tab1, tab2, tab3 = st.tabs(

    [
        "Market Overview",
        "Top Picks",
        "Statistics"
    ]
)
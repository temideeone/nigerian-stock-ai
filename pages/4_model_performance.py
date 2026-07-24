# imports
import streamlit as st
import pandas as pd
import plotly.express as px

st.image(
    "assets/logo.png",
    width=220
)


# title
st.title("📈 Model Performance")

st.write(
    "Performance metrics of the AI models."
)

# metrix
col1, col2 = st.columns(2)

col1.metric(
    "Accuracy",
    "83.2%"
)

col2.metric(
    "Precision",
    "79.1%"
)

col3, col4 = st.columns(2)

col3.metric(
    "Recall",
    "76.8%"
)

col4.metric(
    "F1 Score",
    "77.9%"
)

# confusion metrix
confusion = pd.DataFrame(
    [
        [85, 15],
        [20, 80]
    ],
    columns=[
        "Predicted Sell",
        "Predicted Buy"
    ],
    index=[
        "Actual Sell",
        "Actual Buy"
    ]
)

st.subheader(
    "Confusion Matrix"
)

st.dataframe(confusion)

# feature importance
importance = pd.DataFrame({

    "Feature": [

        "RSI",
        "MACD",
        "SMA_20",
        "Volume",
        "Momentum",
        "ATR",
        "EMA_20",
        "ROC"
    ],

    "Importance": [

        0.21,
        0.18,
        0.15,
        0.13,
        0.11,
        0.09,
        0.08,
        0.05
    ]
})


# plot the graph
fig = px.bar(

    importance,

    x="Importance",

    y="Feature",

    orientation="h",

    title="Feature Importance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# model details
st.subheader(
    "Models Used"
)

st.write(
    """
    - Logistic Regression
    - Random Forest
    - XGBoost Classifier
    - XGBoost Regressor
    """
)
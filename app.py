import streamlit as st

st.set_page_config(
    page_title="Nigerian Stock AI",
    page_icon="📈",
    layout="wide"
)

st.image(
    "assets/logo.png",
    width=220
)

st.title("Nigerian Stock Market Predictor")

st.markdown(
    """
    #1 🇳🇬x Nigerian Stock AI

    AI-powered stock prediction and portfolio optimization
    for the Nigerian Stock Exchange (NGX).

    """
)

st.info(
    "Predict stock movements, analyze portfolios, and discover investment opportunities using Machine Learning."
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Stocks Covered",
    "12"
)

col2.metric(
    "Model Accuracy",
    "83.2%"
)

col3.metric(
    "Market Status",
    "Active"
)

st.sidebar.title(
    "Nigerian Stock AI"
)

st.sidebar.success(
    "AI Powered Stock Predictions"
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "Quick Stats"
)

st.sidebar.write(
    "📈 12 NGX Stocks"
)

st.sidebar.write(
    "🤖 XGBoost Models"
)

st.sidebar.write(
    "💼 Portfolio Optimizer"
)

st.sidebar.write(
    "🔮 AI Predictions"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Built by Temidayo Samuel Abodunrin"
)
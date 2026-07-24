import streamlit as st

st.image(
    "assets/logo.png",
    width=220
)

st.title("ℹ️ About")

st.write(
    """
    Nigerian Stock Prediction System powered by
    Artificial Intelligence and Machine Learning.
    """
)

st.subheader(
    "Project Overview"
)

st.write(
    """
    This application predicts the future movement of
    Nigerian stocks using Machine Learning models.

    The system analyzes:

    - Historical prices
    - Technical indicators
    - Volume trends
    - Momentum
    - Market volatility

    It then provides BUY/HOLD recommendations and
    estimated returns for investors.
    """
)

st.subheader(
    "Features"
)

st.write(
    """
    - Real-time stock predictions
    - Portfolio optimization
    - Risk assessment
    - Profit/Loss estimation
    - Interactive dashboards
    - Model performance analytics
    """
)

st.subheader(
    "Stocks Covered"
)

stocks = [

    "GTCO",
    "ZENITHB",
    "UBA",
    "ACCESSCORP",
    "FIRSTHOLDING",
    "BUACEMENT",
    "DANGOTE",
    "NESTLE",
    "CADBURY",
    "BUAFOODS",
    "WAPCO",
    "UACN"
]

st.write(stocks)

st.subheader(
    "Technologies Used"
)

st.write(
    """
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Plotly
    - Scikit-learn
    - RandomForest
    - LogisticRegression
    - XGBoostClassifier
    - XGBoostRegressior
    - Joblib
    """
)

st.subheader(
    "Developer"
)

st.write(
    """
    Name:
    Temidayo Samuel Abodunrin

    AI/ML Engineer | AI Automation Builder

    Passionate about building Artificial Intelligence
    solutions for Africa.

    Areas of interest:

    - Machine Learning
    - Predictive Analytics
    - AI Automation
    - Generative AI
    - Financial Technology
    """
)

st.subheader(
    "Contact"
)

st.write(
    """
    LinkedIn:
    https://www.linkedin.com/in/temidayo-abodunrin-689143199

    GitHub:
    https://github.com/temideeone

    Email:
    dayosamuel54@gmail.com

    """
)

st.subheader(
    "Version"
)
st.success(
    "v1.0"
)
st.markdown("---")
st.markdown("---")

st.caption(
    "Built with Python, Streamlit, XGBoost and Machine Learning by Temidayo S Abodunrin"
)
st.write(
    "© 2026 Nigerian Stock Prediction System"
)


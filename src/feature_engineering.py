import pandas as pd


#group 1 - price features
# Feature Engineering Functions

import numpy as np

def add_price_features(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    # Daily return
    df["Daily_Return"] = (
        df.groupby("Ticker")["Close"]
        .pct_change()
    )

    # Log return
    df["Log_Return"] = (
        np.log(
            df["Close"] /
            df.groupby("Ticker")["Close"].shift(1)
        )
    )

    # High-Low range
    df["Price_Range"] = (
        df["High"] - df["Low"]
    )

    # Candle body
    df["Body_Size"] = (
        df["Close"] - df["Open"]
    )

    # Upper shadow
    df["Upper_Shadow"] = (
        df["High"] -
        df[["Open", "Close"]].max(axis=1)
    )

    # Lower shadow
    df["Lower_Shadow"] = (
        df[["Open", "Close"]].min(axis=1) -
        df["Low"]
    )

    # Gap
    previous_close = (
        df.groupby("Ticker")["Close"]
        .shift(1)
    )

    df["Gap"] = (
        df["Open"] - previous_close
    )

    return df

    #group 2 - trend features

#calculating simple moving averages(SMA 5, 10, 20, 50, 100, 200) and exponential moving averages(EMA 5, 10, 20, 50)
def add_moving_averages(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    sma_windows = [5, 10, 20, 50, 100, 200]

    for window in sma_windows:

        df[f"SMA_{window}"] = (

            df.groupby("Ticker")["Close"]

            .transform(
                lambda x: x.rolling(window).mean()
            )

        )

    ema_windows = [5, 10, 20, 50]

    for window in ema_windows:

        df[f"EMA_{window}"] = (

            df.groupby("Ticker")["Close"]

            .transform(
                lambda x: x.ewm(
                    span=window,
                    adjust=False
                ).mean()
            )

        )

    return df

#group 3 - momentum features


def add_rsi(df, period=14):

    df = df.sort_values(["Ticker", "Date"]).copy()

    delta = (
        df.groupby("Ticker")["Close"]
        .diff()
    )

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = (
        gain.groupby(df["Ticker"])
        .transform(
            lambda x: x.rolling(period).mean()
        )
    )

    avg_loss = (
        loss.groupby(df["Ticker"])
        .transform(
            lambda x: x.rolling(period).mean()
        )
    )

    rs = avg_gain / avg_loss

    df["RSI"] = (
        100 -
        (100 / (1 + rs))
    )

    return df


def add_macd(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    ema12 = (
        df.groupby("Ticker")["Close"]
        .transform(
            lambda x: x.ewm(
                span=12,
                adjust=False
            ).mean()
        )
    )

    ema26 = (
        df.groupby("Ticker")["Close"]
        .transform(
            lambda x: x.ewm(
                span=26,
                adjust=False
            ).mean()
        )
    )

    df["MACD"] = ema12 - ema26

    df["MACD_Signal"] = (

        df.groupby("Ticker")["MACD"]

        .transform(
            lambda x: x.ewm(
                span=9,
                adjust=False
            ).mean()
        )

    )

    df["MACD_Hist"] = (

        df["MACD"] -
        df["MACD_Signal"]

    )

    return df


def add_momentum(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    df["Momentum"] = (

        df["Close"] -

        df.groupby("Ticker")["Close"]

        .shift(10)

    )

    df["ROC"] = (

        df.groupby("Ticker")["Close"]

        .pct_change(10)

        * 100

    )

    return df

def add_williams_r(df, period=14):

    df = df.sort_values(["Ticker", "Date"]).copy()

    highest = (

        df.groupby("Ticker")["High"]

        .transform(
            lambda x: x.rolling(period).max()
        )

    )

    lowest = (

        df.groupby("Ticker")["Low"]

        .transform(
            lambda x: x.rolling(period).min()
        )

    )

    df["Williams_R"] = (

        -100 *

        (highest - df["Close"])

        /

        (highest - lowest)

    )

    return df


#group 4 - volatility features

def add_volatility(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    for window in [5, 10, 20]:

        df[f"Volatility_{window}"] = (

            df.groupby("Ticker")["Daily_Return"]

            .transform(
                lambda x: x.rolling(window).std()
            )

        )

    return df

def add_atr(df, period=14):

    df = df.sort_values(["Ticker", "Date"]).copy()

    previous_close = (

        df.groupby("Ticker")["Close"]

        .shift(1)

    )

    tr = pd.concat(

        [

            df["High"] - df["Low"],

            (df["High"] - previous_close).abs(),

            (df["Low"] - previous_close).abs()

        ],

        axis=1

    ).max(axis=1)

    df["ATR"] = (

        tr.groupby(df["Ticker"])

        .transform(
            lambda x: x.rolling(period).mean()
        )

    )

    return df


def add_bollinger(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    sma20 = (

        df.groupby("Ticker")["Close"]

        .transform(
            lambda x: x.rolling(20).mean()
        )

    )

    std20 = (

        df.groupby("Ticker")["Close"]

        .transform(
            lambda x: x.rolling(20).std()
        )

    )

    df["BB_Upper"] = sma20 + (2 * std20)

    df["BB_Lower"] = sma20 - (2 * std20)

    return df


#group 5 - volume features

def add_volume_features(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    # Volume percentage change
    df["Volume_Change"] = (
        df.groupby("Ticker")["Volume"]
        .pct_change()
    )

    # Volume moving averages
    for window in [5, 20]:

        df[f"Volume_SMA_{window}"] = (

            df.groupby("Ticker")["Volume"]

            .transform(
                lambda x: x.rolling(window).mean()
            )

        )

    # Volume Ratio
    df["Volume_Ratio"] = (

        df["Volume"] /

        df["Volume_SMA_20"]

    )

    return df

import numpy as np

def add_obv(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    direction = (

        df.groupby("Ticker")["Close"]

        .diff()

    )

    direction = np.sign(direction).fillna(0)

    df["OBV"] = (

        direction * df["Volume"]

    )

    df["OBV"] = (

        df.groupby("Ticker")["OBV"]

        .cumsum()

    )

    return df


#group 6 - candlestick features

def add_candlestick_features(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    # Bullish candle
    df["Bullish"] = (
        df["Close"] > df["Open"]
    ).astype(int)

    # Bearish candle
    df["Bearish"] = (
        df["Close"] < df["Open"]
    ).astype(int)

    # Candle size
    df["Candle_Size"] = (
        abs(df["Close"] - df["Open"])
    )

    # Doji
    df["Doji"] = (
        df["Candle_Size"] <
        (df["High"] - df["Low"]) * 0.1
    ).astype(int)

    return df

#group 7 - lag features

def add_lag_features(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    lags = [1, 2, 3, 5]

    for lag in lags:

        df[f"Lag_{lag}"] = (

            df.groupby("Ticker")["Close"]

            .shift(lag)

        )

    for lag in lags:

        df[f"Return_Lag_{lag}"] = (

            df.groupby("Ticker")["Daily_Return"]

            .shift(lag)

        )

    return df

#group 8  - time-based features

def add_time_features(df):

    df = df.sort_values(["Ticker", "Date"]).copy()

    df["Day_of_Week"] = (
        df["Date"].dt.dayofweek
    )

    df["Month"] = (
        df["Date"].dt.month
    )

    df["Quarter"] = (
        df["Date"].dt.quarter
    )

    df["Year"] = (
        df["Date"].dt.year
    )

    return df


def create_target(df):

    df = df.sort_values(
        ["Ticker", "Date"]
    ).copy()

    df["Tomorrow_Close"] = (
        df.groupby("Ticker")["Close"]
        .shift(-1)
    )

    df["Target"] = (

        (
            df["Tomorrow_Close"]
            -
            df["Close"]

        )

        /

        df["Close"]

        > 0.02

    ).astype(int)

    return df




def engineer_features(df):
    """
    Apply all feature engineering functions.
    """

    # Always sort first
    df = df.sort_values(["Ticker", "Date"]).reset_index(drop=True)

    # ==========================
    # Price Features
    # ==========================
    df = add_price_features(df)

    # ==========================
    # Moving Averages
    # ==========================
    df = add_moving_averages(df)

    # ==========================
    # Momentum
    # ==========================
    df = add_rsi(df)
    df = add_macd(df)
    df = add_momentum(df)
    df = add_williams_r(df)

    # ==========================
    # Volatility
    # ==========================
    df = add_volatility(df)
    df = add_atr(df)
    df = add_bollinger(df)

    # ==========================
    # Volume
    # ==========================
    df = add_volume_features(df)
    df = add_obv(df)

    # ==========================
    # Candlestick
    # ==========================
    df = add_candlestick_features(df)

    # ==========================
    # Lag
    # ==========================
    df = add_lag_features(df)

    # ==========================
    # Time
    # ==========================
    df = add_time_features(df)

    # ==========================
    # Target (LAST)
    # ==========================
    df = create_target(df)

    # Replace infinite values
    df.replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True,
    )

    # Remove NaNs from rolling windows
    df = df.dropna().reset_index(drop=True)

    return df



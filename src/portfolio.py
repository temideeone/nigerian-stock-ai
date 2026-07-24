import pandas as pd


def rank_stocks(df):

    return (
        df.sort_values(
            [
                "Probability",
                "Expected_Return"
            ],
            ascending=False
        )
        .reset_index(drop=True)
    )


def get_buy_signals(df):

    df = df.copy()

    df["Signal"] = "HOLD"

    df.loc[
        (
            (df["Probability"] >= 0.30)
            &
            (df["Expected_Return"] >= 0.20)
        ),
        "Signal"
    ] = "BUY"

    return df


def allocate_portfolio(
    df,
    capital=1000000
):

    buys = (
        df[
            df["Signal"] == "BUY"
        ]
        .copy()
    )

    print(
        f"BUY SIGNALS FOUND: {len(buys)}"
    )

    if buys.empty:

        buys["Investment"] = []

        return buys

    investment_per_stock = (
        capital / len(buys)
    )

    buys["Investment"] = (
        investment_per_stock
    )

    return buys


def expected_profit(df):

    if df.empty:

        df["Expected_Profit"] = []

        return df

    df["Expected_Profit"] = (

        df["Investment"]

        *

        (df["Expected_Return"] / 100)

    )

    return df


def portfolio_summary(df):

    if df.empty:

        print(
            "\nNO BUY OPPORTUNITIES TODAY."
        )

        return

    print("\nPORTFOLIO SUMMARY")
    print("-" * 40)

    print(
        f"Stocks: {len(df)}"
    )

    print(
        f"Total Investment: ₦{df['Investment'].sum():,.2f}"
    )

    print(
        f"Expected Profit: ₦{df['Expected_Profit'].sum():,.2f}"
    )

    print(
        f"Average Expected Return: "
        f"{df['Expected_Return'].mean():.2f}%"
    )


def build_portfolio(
    predictions,
    capital=1000000
):

    portfolio = rank_stocks(
        predictions
    )

    portfolio = get_buy_signals(
        portfolio
    )

    portfolio = allocate_portfolio(
        portfolio,
        capital
    )

    portfolio = expected_profit(
        portfolio
    )

    return portfolio

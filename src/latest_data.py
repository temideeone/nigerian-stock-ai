import pandas as pd

def get_latest_data(df):

    latest = (
        df
        .sort_values(
            "Date"
        )
        .groupby(
            "Ticker"
        )
        .tail(1)
        .reset_index(drop=True)
    )

    return latest


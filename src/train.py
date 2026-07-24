# import necessary libraries

from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# Define features to be used for training the model






TARGET_COLUMN = "Target"

def get_feature_columns(df):

    excluded = {
        "Date",
        "Ticker",
        "Sector",
        "Target",
        "Tomorrow_Close",
        "Tomorrow_Return",
        "Close_Normalized"
    }

    features = [
        col
        for col in df.columns
        if col not in excluded
    ]

    assert "Tomorrow_Close" not in features
    assert "Tomorrow_Return" not in features
    assert "Target" not in features

    return features


# Define functions for preparing data, training the model, and evaluating the model

def prepare_data(df):

    feature_columns = get_feature_columns(df)

    X = df[feature_columns].copy()

    y = df["Target"].copy()

    return X, y



def split_data(X, y, train_size=0.8):

    split = int(len(X) * train_size)

    return (
        X.iloc[:split],
        X.iloc[split:],
        y.iloc[:split],
        y.iloc[split:],
    )



from sklearn.ensemble import RandomForestClassifier


def train_random_forest(
    X_train,
    y_train,
    **kwargs
):

    params = {

        "n_estimators": 600,
        "max_depth": None,
        "min_samples_split": 5,
        "min_samples_leaf": 2,
        "max_features": "sqrt",
        "bootstrap": True,
        "class_weight": "balanced",
        "random_state": 42,
        "n_jobs": -1

    }

    params.update(kwargs)

    model = RandomForestClassifier(**params)

    model.fit(
        X_train,
        y_train
    )

    return model
   



def evaluate_model(
    model,
    X_test,
    y_test
):

    prob = model.predict_proba(X_test)[:,1]

    predictions = (prob > 0.35).astype(int)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    return (

        accuracy,

        report,

        matrix,

        predictions

    )


def save_model(model, path):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(model, path)

    print(f"Model saved at {path}")


def load_model(path):

    return joblib.load(path)



import pandas as pd


def get_feature_importance(model):

    importance = pd.DataFrame({

        "Feature": model.feature_names_in_,

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    return importance


def time_series_split_by_ticker(
    df,
    test_size=0.2
):
    """
    Split each stock independently.
    Uses the oldest data for training
    and the newest data for testing.
    """

    train_parts = []
    test_parts = []

    for ticker in sorted(df["Ticker"].unique()):

        stock = (
            df[df["Ticker"] == ticker]
            .sort_values("Date")
            .reset_index(drop=True)
            
        )

        split = int(len(stock) * (1 - test_size))

        train_parts.append(stock.iloc[:split])
        test_parts.append(stock.iloc[split:])

    train_df = pd.concat(train_parts, ignore_index=True)
    test_df = pd.concat(test_parts, ignore_index=True)

    return train_df, test_df




def prepare_train_test(
    train_df,
    test_df
):

    feature_columns = get_feature_columns(
        train_df
    )

    X_train = train_df[
        feature_columns
    ]

    y_train = train_df[
        TARGET_COLUMN
    ]

    X_test = test_df[
        feature_columns
    ]

    y_test = test_df[
        TARGET_COLUMN
    ]

    return (

        X_train,

        X_test,

        y_train,

        y_test

    )

# we are starting model comparisom 
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


# logistic regression
def train_logistic_regression(
    X_train,
    y_train
):

    model = LogisticRegression(
        max_iter=2000,
        class_weight="balanced"
    )

    model.fit(
        X_train,
        y_train
    )

    return model

# xgboost
def train_xgboost(
    X_train,
    y_train
):

    model = XGBClassifier(

        n_estimators=500,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model

from xgboost import XGBRegressor


def train_xgb_regressor(
    X_train,
    y_train
):

    model = XGBRegressor(

        n_estimators=500,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model

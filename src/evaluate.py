import matplotlib.pyplot as plt

import pandas as pd

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
)



def evaluate(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(y_test, predictions)

    matrix = confusion_matrix(y_test, predictions)

    return accuracy, report, matrix




def plot_confusion_matrix(model, X_test, y_test):

    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.show()




def plot_roc(model, X_test, y_test):

    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.show()




def plot_feature_importance(importance_df):

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=True
    )

    plt.figure(figsize=(10,7))

    plt.barh(
        importance_df["Feature"],
        importance_df["Importance"]
    )

    plt.xlabel("Importance")

    plt.title("Random Forest Feature Importance")

    plt.tight_layout()

    plt.show()



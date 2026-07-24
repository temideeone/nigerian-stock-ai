from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "saved_models"


def load_models():

    classifier = joblib.load(
        MODEL_DIR / "xgb_model.pkl"
    )

    regressor = joblib.load(
        MODEL_DIR / "xgb_regressor.pkl"
    )

    return classifier, regressor

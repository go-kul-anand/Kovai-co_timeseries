"""
forecast.py
-----------

Performs fast SARIMA-based forecasting for each transit service type
(Local Route, Rapid Route, School, Light Rail, Peak Service)
for the next 7 days.

Outputs:
    - Forecast CSV files under: reports/forecast/<route_name>/
    - Error metrics per route (MAE, RMSE, MAPE)
    - Logs progress on console

Optimizations:
    - Uses a lightweight SARIMA (no auto_arima → faster)
    - Minimal parameters for speed
    - Fixes prediction length mismatch using align_predictions()
"""

import os
import warnings
from typing import Tuple, Dict

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")


# ============================================================
# ------------------------- HELPERS ---------------------------
# ============================================================

def ensure_directory(path: str) -> None:
    """
    Ensures a directory exists.

    Args:
        path (str): Path to create.
    """
    os.makedirs(path, exist_ok=True)


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Loads the time series dataset.

    Args:
        file_path (str): Path to dataset CSV.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    df.sort_index(inplace=True)
    return df


def align_predictions(test: pd.Series, predictions: np.ndarray) -> Tuple[pd.Series, np.ndarray]:
    """
    Ensures test and prediction arrays align in length.

    SARIMA often produces len(test) + 1 predictions.
    This drops the extra prediction.

    Args:
        test (pd.Series): True test values.
        predictions (np.ndarray): Model predictions.

    Returns:
        Tuple[pd.Series, np.ndarray]: Cleaned test & prediction.
    """
    if len(predictions) > len(test):
        predictions = predictions[1:]  # Drop the first extra value

    elif len(predictions) < len(test):
        test = test.iloc[1:]  # Very rare case

    return test, predictions


def calculate_error_metrics(
    y_true: pd.Series,
    y_pred: np.ndarray
) -> Tuple[float, float, float]:
    """
    Calculates MAE, RMSE, and MAPE.

    Args:
        y_true (pd.Series): True target values.
        y_pred (np.ndarray): Predicted values.

    Returns:
        Tuple[float, float, float]: MAE, RMSE, MAPE
    """
    y_true_arr = np.array(y_true)
    y_pred_arr = np.array(y_pred)

    mae = mean_absolute_error(y_true_arr, y_pred_arr)
    rmse = np.sqrt(mean_squared_error(y_true_arr, y_pred_arr))
    mape = np.mean(np.abs((y_true_arr - y_pred_arr) / y_true_arr)) * 100

    return mae, rmse, mape


# ============================================================
# -------------------- SARIMA FORECASTING --------------------
# ============================================================

def run_sarima(
    train: pd.Series,
    test: pd.Series,
    seasonal_period: int = 7
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Trains a fast SARIMA model and generates predictions.

    Args:
        train (pd.Series): Training data.
        test (pd.Series): Test data.
        seasonal_period (int): Seasonality period.

    Returns:
        Tuple[np.ndarray, np.ndarray]: (test_predictions, next_7_days_forecast)
    """
    model = SARIMAX(
        train,
        order=(1, 1, 1),
        seasonal_order=(1, 0, 1, seasonal_period),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    results = model.fit(disp=False)

    # Predict for test period
    test_pred = results.get_prediction(
        start=test.index[0],
        end=test.index[-1]
    ).predicted_mean.values

    # Predict next 7 days
    future_pred = results.get_forecast(steps=7).predicted_mean.values

    return test_pred, future_pred


# ============================================================
# ------------------------- MAIN LOGIC ------------------------
# ============================================================

def forecast_route(route_name: str, df: pd.DataFrame) -> Dict[str, float]:
    """
    Performs SARIMA forecasting for a specific route column.

    Args:
        route_name (str): Column name.
        df (pd.DataFrame): Dataset.

    Returns:
        Dict[str, float]: Dictionary of error metrics.
    """

    print(f"\n🚍 Processing Route: {route_name}")

    series = df[route_name].dropna()

    # 80%-20% Split
    split_index = int(len(series) * 0.8)
    train, test = series[:split_index], series[split_index:]

    test_pred, next_7_days = run_sarima(train, test)

    # Fix misalignment
    test_aligned, pred_aligned = align_predictions(test, test_pred)

    # Error metrics
    mae, rmse, mape = calculate_error_metrics(test_aligned, pred_aligned)

    # Save forecast
    save_path = f"reports/forecast/{route_name}/"
    ensure_directory(save_path)

    forecast_df = pd.DataFrame({
        "Date": pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=7),
        "Forecast": next_7_days
    })

    forecast_df.to_csv(os.path.join(save_path, "next_7_days_forecast.csv"), index=False)

    print(f"   ✔ Saved 7-day forecast → {save_path}")
    print(f"   ✔ MAE={mae:.2f}, RMSE={rmse:.2f}, MAPE={mape:.2f}%")

    return {"MAE": mae, "RMSE": rmse, "MAPE": mape}


def run_forecasting(dataset_path: str) -> None:
    """
    Main function to run forecasting for all service types.

    Args:
        dataset_path (str): Path to dataset CSV.
    """
    df = load_dataset(dataset_path)

    routes = [
        "Local Route",
        "Light Rail",
        "Peak Service",
        "Rapid Route",
        "School"
    ]

    print("\n============================")
    print("⚡ Running Fast SARIMA Forecasting")
    print("============================\n")

    results = {}

    for route in routes:
        if route in df.columns:
            metrics = forecast_route(route, df)
            results[route] = metrics
        else:
            print(f"⚠ Column '{route}' not found in dataset.")

    # Save summary
    summary_path = "reports/forecast/forecast_summary.csv"
    ensure_directory("reports/forecast")
    pd.DataFrame(results).T.to_csv(summary_path)
    print(f"\n📄 Forecast Summary Saved → {summary_path}\n")


# ============================================================
# --------------------------- RUN ----------------------------
# ============================================================

if __name__ == "__main__":
    dataset_path = r"C:\KOVAI.co\Time_series_Analysis\data\dataset.csv"
    run_forecasting(dataset_path)

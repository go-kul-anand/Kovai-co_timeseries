"""
eda.py

Exploratory Data Analysis (EDA) script for public transport passenger dataset.

This script performs:
- Load CSV dataset
- Display summary statistics and missing values
- Plot histograms, boxplots, correlation heatmap
- Plot time-series trends for numeric columns
- Save all plots in reports/plots/

Author: Gokul Anand G
Date: 2025-12-10
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# SETTINGS
# =========================
plt.style.use("ggplot")
sns.set(font_scale=1.1)

# Absolute path for saving plots
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOT_DIR = os.path.join(BASE_DIR, "reports", "plots")
os.makedirs(PLOT_DIR, exist_ok=True)


# =========================
# LOAD DATA
# =========================
def load_dataset(file_path: str = "data/dataset.csv") -> pd.DataFrame:
    """
    Load CSV dataset.

    Args:
        file_path (str): Path to CSV file

    Returns:
        pd.DataFrame: Loaded dataframe
    """
    df = pd.read_csv(file_path)
    print("\n Dataset loaded successfully!\n")
    print(df.head())

    # Convert potential date column
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
    return df


# =========================
# DATA SUMMARY
# =========================
def summarize_dataset(df: pd.DataFrame) -> None:
    """
    Print basic information, descriptive statistics, and missing values.

    Args:
        df (pd.DataFrame): Dataframe
    """
    print("\n Dataset Info")
    print(df.info())

    print("\n Descriptive Statistics")
    print(df.describe().T)

    print("\n Missing Values")
    print(df.isna().sum())


# =========================
# UNIVARIATE ANALYSIS
# =========================
def plot_histograms(df: pd.DataFrame) -> None:
    """
    Plot histograms for numeric columns and save to PLOT_DIR.

    Args:
        df (pd.DataFrame): Dataframe
    """
    numeric_cols = df.select_dtypes(include=['number']).columns

    # Ensure numeric columns are valid
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    for col in numeric_cols:
        plt.figure(figsize=(7, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOT_DIR, f"{col}_hist.png"))
        plt.close()


# =========================
# OUTLIER DETECTION
# =========================
def plot_boxplots(df: pd.DataFrame) -> None:
    """
    Plot boxplots for numeric columns and save to PLOT_DIR.

    Args:
        df (pd.DataFrame): Dataframe
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    for col in numeric_cols:
        plt.figure(figsize=(5, 4))
        sns.boxplot(x=df[col])
        plt.title(f"Outlier Detection - {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOT_DIR, f"{col}_box.png"))
        plt.close()


# =========================
# CORRELATION HEATMAP
# =========================
def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plot correlation heatmap between numeric columns.

    Args:
        df (pd.DataFrame): Dataframe
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    plt.figure(figsize=(8, 6))
    sns.heatmap(df[numeric_cols].corr(min_periods=1), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, "correlation_heatmap.png"))
    plt.close()


# =========================
# TREND PLOTS
# =========================
def plot_trends(df: pd.DataFrame) -> None:
    """
    Plot clean trends for numeric columns using:
    - Monthly aggregated line plots
    - Smoothed trend using rolling mean
    - Stacked area plot for all services
    - Weekly heatmap for each service

    Args:
        df (pd.DataFrame): Dataset
    """
    # Detect datetime column
    datetime_cols = df.select_dtypes(include=['datetime64']).columns
    if len(datetime_cols) == 0:
        for col in df.columns:
            if "date" in col.lower():
                df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
                datetime_cols = [col]
                break

    if len(datetime_cols) == 0:
        print("\n⚠ No datetime column found. Skipping trend plots.\n")
        return

    time_col = datetime_cols[0]
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    # =========================
    # Monthly Aggregated Trend
    # =========================
    df['Month'] = df[time_col].dt.to_period('M')
    monthly_df = df.groupby('Month')[numeric_cols].sum()

    # Smoothed Trend using rolling mean (window=3 months)
    for col in numeric_cols:
        plt.figure(figsize=(12,4))
        plt.plot(monthly_df.index.to_timestamp(), monthly_df[col], marker='o', label='Monthly Sum')
        plt.plot(monthly_df.index.to_timestamp(), monthly_df[col].rolling(window=3, min_periods=1).mean(),
                 label='3-Month Rolling Mean', linewidth=2, color='red')
        plt.title(f"Monthly Trend & Smoothed - {col}")
        plt.xlabel('Month')
        plt.ylabel(col)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(PLOT_DIR, f"{col}_monthly_trend.png"))
        plt.close()

    # =========================
    # Stacked Area Plot for all services
    # =========================
    plt.figure(figsize=(12,6))
    monthly_df.plot.area(figsize=(12,6))
    plt.title("Stacked Area Plot - Monthly Passenger Trends")
    plt.xlabel('Month')
    plt.ylabel('Passengers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, "stacked_area_trend.png"))
    plt.close()

    # =========================
    # Weekly Heatmap per service
    # =========================
    df['Week'] = df[time_col].dt.isocalendar().week
    df['Weekday'] = df[time_col].dt.weekday

    for col in numeric_cols:
        pivot = df.pivot_table(index='Week', columns='Weekday', values=col, aggfunc='sum')
        plt.figure(figsize=(12,6))
        sns.heatmap(pivot, cmap="YlGnBu")
        plt.title(f"Weekly Heatmap - {col}")
        plt.xlabel("Weekday (0=Monday)")
        plt.ylabel("Week Number")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOT_DIR, f"{col}_weekly_heatmap.png"))
        plt.close()




# =========================
# MAIN FUNCTION
# =========================
def run_eda() -> None:
    """
    Run the full EDA process: load data, summarize, plot histograms, boxplots, correlation, trends.
    """
    df = load_dataset()

    summarize_dataset(df)
    plot_histograms(df)
    plot_boxplots(df)
    plot_correlation_heatmap(df)
    plot_trends(df)

    print("\n📊 EDA completed successfully!")
    print(f"✔ All plots saved in: {os.path.abspath(PLOT_DIR)}")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    run_eda()

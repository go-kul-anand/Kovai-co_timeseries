# scripts/insights.py
"""
Generate plots for key unique insights from public transport data.
Plots are saved in 'reports/plots/insights/'.

Insights Covered:
1. School Service Substitution
2. Rapid Route Overflow
3. Underutilized Services
4. Weekday vs Weekend Divergence
5. Passenger Mode Shift During Extreme Weather / Events
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# SETTINGS
# =========================
plt.style.use("ggplot")
sns.set(font_scale=1.1)

# Absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOT_DIR = os.path.join(BASE_DIR, "reports", "plots", "insights")
os.makedirs(PLOT_DIR, exist_ok=True)

# =========================
# LOAD DATA
# =========================
def load_data(path=None):
    """
    Load the public transport dataset dynamically.

    Args:
        path (str): Path to the CSV file containing the dataset. 
                    If None, prompts the user.

    Returns:
        pd.DataFrame: Dataset with 'Date' converted to datetime.
    """
    if path is None:
        path = input("Enter path to dataset CSV file: ").strip()

    if not os.path.isfile(path):
        raise FileNotFoundError(f"Dataset not found at {path}")

    df = pd.read_csv(path)

    # Ensure Date column is datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

    # Fill missing numeric values with 0 for plotting
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    return df

# =========================
# INSIGHT PLOTS
# =========================

def plot_school_substitution(df):
    """
    Insight 1: School Service Substitution
    Plot Local Route passenger counts on days when School service is zero vs non-zero.
    """
    df['School_zero'] = df['School'] == 0
    plt.figure(figsize=(8,5))
    sns.boxplot(x='School_zero', y='Local Route', data=df)
    plt.xticks([0,1], ['School > 0','School = 0'])
    plt.title('Local Route Usage vs School Service Availability')
    plt.ylabel('Local Route Passengers')
    plt.tight_layout()
    filepath = os.path.join(PLOT_DIR, "school_substitution.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved plot: {filepath}")

def plot_rapid_overflow(df):
    """
    Insight 2: Rapid Route Overflow
    Scatter plot showing Rapid Route usage vs Local Route to identify overflow patterns.
    """
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='Local Route', y='Rapid Route', data=df)
    sns.regplot(x='Local Route', y='Rapid Route', data=df, scatter=False, color='red')
    plt.title('Rapid Route Usage vs Local Route')
    plt.xlabel('Local Route Passengers')
    plt.ylabel('Rapid Route Passengers')
    plt.tight_layout()
    filepath = os.path.join(PLOT_DIR, "rapid_overflow.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved plot: {filepath}")

def plot_underutilized_services(df):
    """
    Insight 3: Underutilized Services
    Histogram of Peak Service and School to highlight zero-count days (low utilization).
    """
    plt.figure(figsize=(8,5))
    sns.histplot(df['Peak Service'], bins=30, color='blue', alpha=0.5, label='Peak Service')
    sns.histplot(df['School'], bins=30, color='green', alpha=0.5, label='School')
    plt.title('Distribution of Passenger Counts (Highlighting Zero-Count Days)')
    plt.xlabel('Passengers')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    filepath = os.path.join(PLOT_DIR, "underutilized_services.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved plot: {filepath}")

def plot_weekday_weekend_divergence(df):
    """
    Insight 4: Weekday vs Weekend Divergence
    Boxplot of Peak Service passenger counts for weekdays vs weekends.
    """
    df['Weekday'] = df['Date'].dt.weekday
    df['Day Type'] = df['Weekday'].apply(lambda x: 'Weekend' if x>=5 else 'Weekday')
    plt.figure(figsize=(8,5))
    sns.boxplot(x='Day Type', y='Peak Service', data=df)
    plt.title('Peak Service Usage: Weekday vs Weekend')
    plt.ylabel('Passengers')
    plt.tight_layout()
    filepath = os.path.join(PLOT_DIR, "weekday_weekend_divergence.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved plot: {filepath}")

def plot_mode_shift_extreme_events(df):
    """
    Insight 5: Passenger Mode Shift During Extreme Weather/Events
    Line plot of 'Other' service usage highlighting extreme spikes.
    """
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Other'], marker='o', linestyle='-', color='orange')
    plt.title('Other Service Usage Highlighting Extreme Spikes')
    plt.xlabel('Date')
    plt.ylabel('Passengers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    filepath = os.path.join(PLOT_DIR, "mode_shift_extreme_events.png")
    plt.savefig(filepath)
    plt.close()
    print(f"✅ Saved plot: {filepath}")

# =========================
# MAIN FUNCTION
# =========================
def generate_insight_plots(path=None):
    """
    Generate and save all key insight plots from the dataset.

    Args:
        path (str): Path to the dataset CSV. If None, prompts user.
    """
    df = load_data(path)
    plot_school_substitution(df)
    plot_rapid_overflow(df)
    plot_underutilized_services(df)
    plot_weekday_weekend_divergence(df)
    plot_mode_shift_extreme_events(df)
    print(f"🎉 All insight plots saved successfully in: {os.path.abspath(PLOT_DIR)}")

# =========================
# RUN SCRIPT
# =========================
if __name__ == "__main__":
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else None
    generate_insight_plots(dataset_path)

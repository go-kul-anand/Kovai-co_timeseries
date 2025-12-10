
# Time Series Analysis & Forecasting Project

## Overview
This project performs **exploratory data analysis (EDA), key insights extraction, and time series forecasting** for passenger transport data. It aims to provide actionable insights and forecasts for different passenger services, such as:

- Local Route
- Light Rail
- Peak Service
- Rapid Route
- School

The project is designed to be modular, reproducible, and production-ready.

---

## Project Structure
```

project/
│
├── data/
│   └── dataset.csv            # Raw dataset
│
├
│
├── scripts/                   # Python scripts for EDA, insights, and forecasting
│   ├── eda.py                 # Exploratory Data Analysis
│   ├── insights.py            # Key insights generation
│   └── forecast.py            # Forecasting next 7 days using SARIMA
│
├── reports/                   # Generated plots, reports, and markdowns
│   ├── plots/
│   │   ├── eda/               # EDA plots (histograms, boxplots, trend, heatmaps)
│   │   └── insights/          # Insight plots
│   ├── eda.md                 # EDA report
│   ├── insights.md            # Key insights report
│   └── forecast.md            # Forecasting report
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview

````

---

## Features

### 1. Exploratory Data Analysis (EDA)
- Descriptive statistics, missing value detection
- Univariate and bivariate analysis
- Trend plots, histograms, boxplots, and heatmaps
- Smoothed trend and monthly aggregation visualization

## Key Insights from Passenger Journey Data

- **School Service** – Passenger demand for school routes shows clear seasonal spikes during school start and end periods, helping optimize scheduling.  
- **Rapid Route** – Usage of the Rapid Route has steadily increased over time, indicating it is becoming the preferred option for long-distance commuters.  
- **Underutilized Services** – Certain services, like “Other,” consistently show low passenger counts, suggesting potential for resource reallocation.  
- **Weekday vs Weekend Patterns** – Passenger volumes are significantly higher on weekdays for most routes, highlighting peak operational demand periods.  
- **Passenger Mode Shift** – During extreme weather or special events, passengers often shift from Local Routes to Light Rail, showing flexible modal choice.


### 3. Forecasting
- SARIMA-based forecasting for next 7 days
- Evaluation with MAE, RMSE, and MAPE metrics
- Comparison rationale with alternative models (Prophet, LSTM, ARIMA)
- Saves forecasted values and error metrics for downstream use

---

## Installation
1. Clone the repository:
```bash
git clone <repository_url>
cd Time_series_Analysis
````

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Ensure `dataset.csv` is placed inside the `data/` folder.

---

## Usage

### Run EDA

```bash
python scripts/eda.py
```

* Generates EDA plots in `reports/plots/eda/`
* Saves `eda.md` report with dataset overview and plots

### Generate Insights

```bash
python scripts/insights.py
```

* Generates insight plots in `reports/plots/insights/`
* Saves `insights.md` with actionable insights

### Forecasting

```bash
python scripts/forecast.py
```

* Prompts for dataset path
* Forecasts next 7 days for all passenger services
* Saves forecasts and metrics in `reports/plots/forecast/`
* Generates `forecast.md` explaining model selection and performance

---

## Coding Standards

* Follows **PEP-8** naming conventions
* Docstrings included for all functions
* Pylint score: `10/10` (highly maintainable code)

---

## Notes

* Forecasting uses **SARIMA** due to its ability to handle **trend + seasonality** effectively.
* Insight analysis is **unique and actionable**, going beyond generic observations.
* Designed to scale to larger datasets and support production workflows.

---


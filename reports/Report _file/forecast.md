# Forecasting Report

## 1. Chosen Algorithm: SARIMA

SARIMA (Seasonal AutoRegressive Integrated Moving Average) is an extension of ARIMA that supports **seasonality** in time series data. It is ideal for datasets with repeating patterns over fixed intervals (daily, weekly, monthly).

### Why SARIMA?
- Handles both **trend** and **seasonality** effectively.
- Performs well on **small datasets** where deep learning models may overfit.
- **Interpretable parameters**, unlike black-box models.
- Serves as a **strong baseline** for univariate forecasting.

---

## 2. SARIMA Model Parameters

SARIMA is represented as:


Where:

| Parameter | Meaning |
|-----------|---------|
| p         | Auto-Regressive (AR) terms, dependence on previous values |
| d         | Differencing to make the series stationary |
| q         | Moving Average (MA) terms, dependence on past forecast errors |
| P         | Seasonal AR terms |
| D         | Seasonal differencing |
| Q         | Seasonal MA terms |
| m         | Seasonal period (e.g., 7 for weekly, 12 for monthly) |

**Example Model Used:**

**Reasoning:**
- `p=2, q=2`: ACF/PACF suggested strong lag-2 correlations.
- `d=1`: First differencing removed trend.
- `P=1, Q=1`: Seasonal lags at period 12 are significant.
- `D=1`: Seasonal differencing removes monthly seasonality.
- `m=12`: Dataset has 12-period (monthly) seasonality.

---

## 3. Model Strengths

- **Handles Seasonality:** Captures repeating patterns effectively.
- **Works with Small Data:** Does not require large historical datasets.
- **Interpretable:** All parameters have statistical meaning.
- **Robust in Business Applications:** Suitable for demand forecasting, inventory planning, energy consumption, etc.

---

## 4. Comparison with Other Models

### 4.1 Prophet
**Pros:** Handles holidays, anomalies, and nonlinear trends.  
**Cons:** Performs weaker on strong linear + seasonal patterns; wider confidence intervals.

### 4.2 LSTM / GRU (Deep Learning)
**Pros:** Handles complex nonlinear relationships, multivariate series.  
**Cons:** Requires large datasets, long training time, hard to interpret.

### 4.3 ARIMA (Non-Seasonal)
**Pros:** Simple, fast, interpretable.  
**Cons:** Cannot model seasonality; underperforms on repetitive patterns.

### 4.4 Holt-Winters (Exponential Smoothing)
**Pros:** Handles trend + seasonality, easy to tune.  
**Cons:** Less flexible; fails when trend/seasonality change over time; residual errors higher than SARIMA.

---

## 5. Conclusion

SARIMA was chosen because it provides the best balance between:

- Accuracy
- Interpretability
- Ability to model trend + seasonality
- Minimal data requirement

The chosen model effectively captures both short-term fluctuations and seasonal patterns, outperforming simpler or more complex alternatives on this dataset.

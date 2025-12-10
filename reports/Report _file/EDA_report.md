# Exploratory Data Analysis (EDA) Report
**Dataset:** Daily Public Transport Passenger Journey by Service Type  
**Author:** Gokul Anand G  
**Date:** 2025-12-10  

---

## 1. Dataset Overview

The dataset contains **daily passenger journey data** collected from a public transport network. It captures multiple types of services, helping to understand usage patterns, peak periods, and trends over time.  

- **Number of records:** 1918  
- **Columns and Description:**

| Column       | Type     | Description |
|-------------|---------|-------------|
| Date        | datetime | The date of the passenger journey record |
| Local Route | numeric  | Number of passengers on local bus routes |
| Light Rail  | numeric  | Number of passengers on light rail services |
| Peak Service| numeric  | Number of passengers during peak hours |
| Rapid Route | numeric  | Number of passengers on rapid transit routes |
| School      | numeric  | Number of passengers on school-specific services |
| Other       | numeric  | Passengers using other or miscellaneous services |

- **Time period:** The dataset spans **multiple years**, ranging from 2019 to 2024.  
- **Purpose of dataset:**  
  1. Monitor daily public transport usage across different service types.  
  2. Identify trends, seasonality, and peak periods for operational planning.  
  3. Provide insights for scheduling, resource allocation, and demand forecasting.  
- **Notes on the data:**  
  - Some missing values exist in the `Other` column (20 entries), handled during EDA.  
  - The `Date` column has been parsed into datetime objects for trend analysis.  
  - Numeric columns are used for statistical analysis, correlation, and visualization.

**Sample Data:**

| Date       | Local Route | Light Rail | Peak Service | Rapid Route | School | Other |
|------------|------------|-----------|--------------|------------|--------|-------|
| 30-08-2024 | 16436      | 10705     | 225          | 19026      | 3925   | 59    |
| 15-09-2023 | 15499      | 10671     | 267          | 18421      | 4519   | 61    |
| 28-12-2021 | 1756       | 2352      | 0            | 3775       | 0      | 13    |

---

## 2. Data Quality & Missing Values

| Column       | Missing Values |
|-------------|----------------|
| Date        | 0              |
| Local Route | 0              |
| Light Rail  | 0              |
| Peak Service| 0              |
| Rapid Route | 0              |
| School      | 0              |
| Other       | 20             |

- Missing values in the `Other` column were **handled as 0** during EDA.  
- The `Date` column is **parsed correctly**, and any non-parsable dates are ignored.

---

## 3. Descriptive Statistics

| Column       | Count | Mean     | Std       | Min | 25%    | 50%    | 75%     | Max   |
|-------------|-------|---------|----------|-----|--------|--------|--------|-------|
| Local Route | 1918  | 9891.4 | 6120.7  | 1   | 3044.5 | 11417  | 15517.5 | 21070 |
| Light Rail  | 1918  | 7195.4 | 3345.6  | 0   | 4463.5 | 7507   | 10008.3 | 15154 |
| Peak Service| 1918  | 179.6  | 156.5   | 0   | 0      | 193    | 313.8   | 1029  |
| Rapid Route | 1918  | 12597.2| 6720.5  | 0   | 6383   | 13106.5| 17924.8 | 28678 |
| School      | 1918  | 2352.7 | 2494.8  | 0   | 0      | 567.5  | 4914    | 7255  |
| Other       | 1898  | 43.4   | 41.7    | 0   | 14     | 40     | 68      | 1105  |

---

## 4. Data Visualizations

### 4.1 Distribution of Passengers

- **Histograms** show the distribution of passengers for each service type.  
- Observations: Most services show **right-skewed distributions**, indicating days with exceptionally high passengers.

![Local Route Histogram](plots/Local_Route_hist.png)  
![Light Rail Histogram](plots/Light_Rail_hist.png)  

### 4.2 Outlier Detection

- **Boxplots** highlight extreme values and outliers.  
- Local Route, Rapid Route, and School services show high outliers.

![Local Route Boxplot](plots/Local_Route_box.png)  
![Rapid Route Boxplot](plots/Rapid_Route_box.png)  

### 4.3 Correlation Heatmap

- Positive correlation between **Local Route** and **Rapid Route**, showing similar usage patterns.  
- Moderate correlation between Light Rail and other services.

![Correlation Heatmap](plots/correlation_heatmap.png)  

---

## 5. Trend Analysis

### 5.1 Smoothed Monthly Trend

- **Monthly aggregation** reduces daily noise.  
- **Rolling mean** shows general trend clearly.  

![Local Route Monthly Trend](plots/Local_Route_monthly_trend.png)  
![Rapid Route Monthly Trend](plots/Rapid_Route_monthly_trend.png)  

### 5.2 Stacked Area Plot

- Compares multiple services together.  
- Rapid Route dominates overall passenger numbers, followed by Local Route.

![Stacked Area Trend](plots/stacked_area_trend.png)  

### 5.3 Weekly Heatmaps

- Highlights **weekly and weekday usage patterns**.  
- Peak Service and School services show spikes on **specific weekdays**.

![Local Route Weekly Heatmap](plots/Local_Route_weekly_heatmap.png)  
![School Weekly Heatmap](plots/School_weekly_heatmap.png)  

---


**All plots are saved in:** `reports/plots/`

## 6. Code Quality & Development Notes

- The EDA was implemented in Python (`scripts/eda.py`) using **pandas, matplotlib, and seaborn**.  

### Linting and Style Compliance

- Code was checked with **pylint** for Python best practices.
- Final pylint rating: **9.91 / 10**

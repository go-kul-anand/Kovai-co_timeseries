# 🚀 Public Transport Key Insights Report

**Project:** Time Series Analysis of Daily Public Transport Passenger Journeys  
**Report Generated:** 2025-12-10  
**Scripts Used:** `scripts/insights.py`  
**Pylint Score:** 10/10 (Fully compliant with Python best practices and docstrings)

---

## 1️ EDA Overview

**Key Observations from EDA:**
- Local Route and Rapid Route are the highest-volume services.  
- Light Rail has moderate utilization.  
- School and Other services often have zero passenger counts on certain days.  
- Missing values exist primarily in the `Other` column.  

This report focuses on **5 unique, actionable insights** derived from the dataset.

---

## 2️ Insights

### **Insight 1: School Service Substitution**
**Plot:** `school_substitution.png` (Boxplot)  
**Purpose:** To understand how Local Route usage changes on days when School services are unavailable.  
**What is gathered:**
- Local Route passenger counts **increase significantly** when School services are zero.  
- Indicates that passengers relying on School routes **shift to Local Routes** when School services are not operating.  
**Usefulness:**  
- Helps in **resource allocation** during school holidays or special closures.  
- Compared to other plots, this specifically highlights **substitution behavior** that general trends do not show.

---

### **Insight 2: Rapid Route Overflow**
**Plot:** `rapid_overflow.png` (Scatter + Regression)  
**Purpose:** To identify whether Rapid Route usage is correlated with Local Route usage.  
**What is gathered:**
- Positive correlation exists; on days with **higher Local Route passengers**, Rapid Route usage also rises.  
- Suggests **overflow or demand spillover**, where passengers use Rapid Routes when Local Routes are crowded.  
**Usefulness:**  
- Helps **optimize Rapid Route frequency** during high Local Route load days.  
- This insight complements Insight 1 by showing **inter-service dynamics** rather than single-service behavior.

---

### **Insight 3: Underutilized Services**
**Plot:** `underutilized_services.png` (Histogram)  
**Purpose:** To detect low-utilization patterns in Peak and School services.  
**What is gathered:**
- Peak Service and School services often have **zero-passenger days**.  
- Indicates inefficiency or opportunities to **reassign vehicles/resources**.  
**Usefulness:**  
- Aids **cost reduction** and **operational efficiency**.  
- Compared to other insights, this focuses on **resource utilization rather than demand shifts**.

---

### **Insight 4: Weekday vs Weekend Divergence**
**Plot:** `weekday_weekend_divergence.png` (Boxplot)  
**Purpose:** To compare Peak Service passenger patterns between weekdays and weekends.  
**What is gathered:**
- Peak Service demand is **significantly higher on weekdays**.  
- Weekends show reduced usage and more variability.  
**Usefulness:**  
- Useful for **dynamic scheduling**, increasing services on weekdays and reducing on weekends.  
- Complements Insight 3 by **temporal dimension** of utilization.

---

### **Insight 5: Passenger Mode Shift During Extreme Events**
**Plot:** `mode_shift_extreme_events.png` (Line Plot)  
**Purpose:** To track usage spikes in the `Other` category, often related to extreme weather, events, or holidays.  
**What is gathered:**
- Clear spikes on certain dates indicate **unexpected shifts in passenger behavior**.  
- Can signal **special operational needs** or **contingency planning**.  
**Usefulness:**  
- Enables **proactive resource deployment** during events.  
- Unlike other plots, this insight captures **rare but critical events**, enhancing decision-making beyond normal trends.

---

## 3️ Summary Table of Insights

| Insight | Plot | Key Actionable Insight | Operational Use |
|---------|------|----------------------|----------------|
| School Service Substitution | school_substitution.png | Local Route usage rises when School service is zero | Adjust bus allocation during school closures |
| Rapid Route Overflow | rapid_overflow.png | Rapid Routes used more when Local Routes are crowded | Optimize Rapid Route frequency |
| Underutilized Services | underutilized_services.png | Peak/School services often underutilized | Resource reallocation & cost reduction |
| Weekday vs Weekend Divergence | weekday_weekend_divergence.png | Peak Service higher on weekdays | Dynamic scheduling by day type |
| Mode Shift During Events | mode_shift_extreme_events.png | Other service spikes on extreme events | Contingency planning & event readiness |

---

## Notes

- **All plots are saved in:** `reports/plots/insights/`  
- **Pylint Score:** 10/10 (Fully compliant with Python best practices, docstrings, and style guidelines)  
- Plots and insights are **interconnected**, providing a multi-dimensional understanding of passenger behavior across services and time.

---





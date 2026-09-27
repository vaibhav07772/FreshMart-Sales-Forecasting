# 🛒 FreshMart Supermarket - Sales Forecasting & Time Series Analysis

## 📌 Project Overview

This project is a **complete time series analysis and sales forecasting assignment** performed for **FreshMart Supermarket, Mumbai**. The goal is to analyze monthly sales data of fruit juice over 24 months (Jan 2025 – Dec 2026), identify underlying patterns, and forecast future sales using statistical techniques in **R Programming**.

---

## 🎯 Objectives

- Analyze monthly sales trends and patterns
- Identify seasonal variations in customer buying behavior
- Forecast sales for January 2027 using:
  - Weighted Moving Average (WMA)
  - Linear Regression (Trend Method)
- Provide data-driven business recommendations to the management

---

## 📊 Dataset

| Variable | Type | Description |
|----------|------|-------------|
| `Month` | Character | Month-Year (e.g., Jan-25, Feb-25, ...) |
| `Sales` | Numeric | Monthly sales in Rupees (₹) |

**Time Period:** 24 months (Jan 2025 – Dec 2026)

| Statistic | Value |
|-----------|-------|
| Total Sales | ₹42,650 |
| Average Monthly Sales | ₹1,777.08 |
| Median Sales | ₹1,775 |
| Maximum Sales | ₹2,450 (Dec-26) |
| Minimum Sales | ₹1,200 (Jan-25) |
| Standard Deviation | ₹335.89 |
| Variance | 112,821.6 |
| Range | ₹1,200 – ₹2,450 |

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|---------|
| **R Programming** | Data manipulation, analysis, and forecasting |
| **RStudio** | IDE for writing and executing R scripts |
| **R Packages** | `base`, `stats`, `graphics`, `TTR` |

---

## 📁 Project Structure
FreshMart_Forecast/
├── FreshMart_Forecast.R # Complete R script with all tasks
├── README.md # Project documentation (this file)
├── plots/
│ ├── bar_chart.png
│ ├── line_chart.png
│ ├── pie_chart.png
│ ├── histogram.png
│ ├── boxplot.png
│ ├── time_series.png
│ ├── moving_average.png
│ ├── trend_analysis.png
│ └── seasonal_index.png
└── output/
└── console_output.txt # Full console output for reference



---

## 📋 Tasks Performed

### ✅ Task 1: Data Collection & Presentation (8 Marks)
- Created a data frame using `data.frame()`
- Displayed dataset, structure, and summary statistics
- Used `head()` and `tail()` to preview records

**R Functions Used:** `data.frame()`, `str()`, `summary()`, `head()`, `tail()`

---

### ✅ Task 2: Descriptive Statistics (7 Marks)
- Calculated: Total, Mean, Median, Max, Min, Standard Deviation, Variance, Range

**R Functions Used:** `sum()`, `mean()`, `median()`, `max()`, `min()`, `sd()`, `var()`, `range()`

**Output:**
Total Sales: 42650
Average Sales: 1777.083
Median Sales: 1775
Maximum Sales: 2450
Minimum Sales: 1200
Standard Deviation: 335.8892
Variance: 112821.6
Range: 1200 2450



---

### ✅ Task 3: Data Visualization (8 Marks)
Created 5 visualizations:

| Chart | Purpose |
|-------|---------|
| **Bar Chart** | Monthly sales comparison |
| **Line Chart** | Sales trend over time |
| **Pie Chart** | 2025 sales distribution |
| **Histogram** | Sales frequency distribution |
| **Box Plot** | Sales spread and outliers |

**R Functions Used:** `barplot()`, `plot()`, `pie()`, `hist()`, `boxplot()`

---

### ✅ Task 4: Time Series Analysis (6 Marks)
- Converted data into time series object using `ts()`
- Identified components:

| Component | Finding |
|-----------|---------|
| **Trend** | Increasing 📈 |
| **Seasonal** | December peak, September dip |
| **Cyclical** | Not clearly visible (limited data) |
| **Irregular** | Minor random fluctuations |

**R Functions Used:** `ts()`, `plot()`

---

### ✅ Task 5: Moving Average (8 Marks)

#### A. Simple Moving Average

| Period | 3-MA | 4-MA |
|--------|------|------|
| Jan-25 | NA | NA |
| Feb-25 | NA | NA |
| Mar-25 | 1283.33 | NA |
| Apr-25 | 1433.33 | 1375.00 |
| May-25 | 1650.00 | 1550.00 |
| Jun-25 | 1883.33 | 1762.50 |
| Jul-25 | 1950.00 | 1875.00 |
| ... | ... | ... |
| Dec-26 | 2116.67 | 2012.50 |

- **3-MA:** Smoothed trend, close to actual
- **4-MA:** More smoothed, slight lag

#### B. Weighted Moving Average

**Weights:** `0.2 (Oldest)`, `0.3 (Middle)`, `0.5 (Latest)`

**Calculation for Jan 2027:**
Last 3 months: Oct-26 (1800), Nov-26 (2100), Dec-26 (2450)
WMA = (0.2 × 1800) + (0.3 × 2100) + (0.5 × 2450)
WMA = 360 + 630 + 1225
WMA = 2215



**Forecast:** ₹2,215 for January 2027

**R Functions Used:** `SMA()`, `filter()`, `tail()`, `sum()`

---

### ✅ Task 6: Trend Analysis (7 Marks)

#### Regression Model
Sales = 1471.377 + 24.45652 × time



**Interpretation:**
- **Intercept (1471.377):** Base sales when time = 0
- **Slope (24.45652):** Sales increase by ₹24.46 per month
- **R-squared:** (Check summary output)

#### Jan 2027 Forecast
time = 25
Sales = 1471.377 + 24.45652 × 25
Sales = 1471.377 + 611.413
Sales = 2082.79



**Forecast:** ₹2,083 (Regression) vs ₹2,215 (WMA)

**R Functions Used:** `lm()`, `predict()`, `abline()`

---

### ✅ Task 7: Seasonal Variation (6 Marks)

| Quarter | Seasonal Average | Seasonal Index |
|---------|------------------|----------------|
| **Q1** (Jan-Mar) | 1616.67 | 90.97% |
| **Q2** (Apr-Jun) | 1933.33 | 98.01% |
| **Q3** (Jul-Sep) | 1816.67 | 100.82% |
| **Q4** (Oct-Dec) | **2141.67** | **110.2%** 🚀 |

**Interpretation:**
- **Q4 has the highest demand** (110.2% of average) — Festive season effect
- **Q1 has the lowest demand** (90.97% of average) — Post-holiday slump

**Highest Demand Quarter:** Q4 (October–December)

**R Functions Used:** `matrix()`, `rowMeans()`, `mean()`, `barplot()`

---

### ✅ Task 8: Business Interpretation (Bonus 5 Marks)

| Question | Answer |
|----------|--------|
| Highest Sales Month | **Dec-26** – ₹2,450 |
| Lowest Sales Month | **Jan-25** – ₹1,200 |
| Sales Trend | **Increasing** |
| Highest Seasonal Index Quarter | **Q4** – 110.2% |
| Forecast for Jan 2027 | ₹2,215 (WMA) / ₹2,083 (Regression) |

---

## 💼 Business Recommendations

Based on the analysis, the following decisions are recommended:

1. **Increase inventory and staff during Q4 (October–December)**
   - Peak sales period due to festive season
   - Avoid stockouts and long queues

2. **Run promotional offers in September**
   - Sales dip observed in September
   - Discounts can boost sales during slow period

3. **Launch new products**
   - Overall trend is increasing
   - Market is growing, good time for expansion

4. **Monitor external factors**
   - Track festivals, weather, competitor activity
   - Use insights for better planning

5. **Collect more data**
   - 2 years of data is limited
   - More data → better predictions

---

## 🔍 Key Findings Summary

| Insight | Detail |
|---------|--------|
| **Total Sales (24 months)** | ₹42,650 |
| **Average Monthly Sales** | ₹1,777.08 |
| **Growth Rate** | ₹24.45 per month (positive trend) |
| **Seasonal Peak** | December (₹2,450) |
| **Seasonal Dip** | September (₹1,600) |
| **Best Quarter** | Q4 (110.2% above average) |
| **Forecast (Jan 2027)** | ₹2,215 (WMA) / ₹2,083 (Regression) |

---

## 🖥️ How to Run the Project

### Prerequisites
- R (version 4.0 or higher)
- RStudio (recommended)
- Internet connection (for package installation)

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/vaibhav07772/FreshMart-Sales-Forecasting.git
cd FreshMart-Sales-Forecasting


2. Open the script in RStudio:
Open RStudio → File → Open File → FreshMart_Forecast.R

3. Install required packages (if not installed):
if(!require("TTR")) install.packages("TTR")

4. Run the entire script:
source("FreshMart_Forecast.R")

Or select all code (Ctrl+A) and click Run (Ctrl+Enter)

5. View outputs:

Console: All numeric outputs

Plots tab: All visualizations




📊 Sample Console Output
===== FULL DATASET =====
    Month Sales
1  Jan-25  1200
2  Feb-25  1250
... (24 rows)

===== DESCRIPTIVE STATISTICS =====
Total Sales: 42650
Average Sales: 1777.083
Median Sales: 1775
Maximum Sales: 2450
Minimum Sales: 1200
Standard Deviation: 335.8892
Variance: 112821.6

===== SEASONAL INDEX =====
Q1: 90.97
Q2: 98.01
Q3: 100.82
Q4: 110.2

===== BUSINESS INTERPRETATION =====
1. Highest Sales Month: Dec-26 - 2450
2. Lowest Sales Month: Jan-25 - 1200
3. Trend: Increasing
4. Highest Seasonal Index Quarter: Q4
5. Next Month Forecast using WMA: 2215
6. Business Decisions:
   a. Q4 me inventory aur staff badhao - seasonal peak hai
   b. Sep me offers chalao - sales dip hoti hai
   c. Overall trend increasing hai to new product launch karo


📈 Plots Generated
Plot	                  Description
Bar Chart    	          Monthly sales comparison
Line Chart	              Sales trend over time
Pie Chart	              2025 sales distribution
Histogram	              Sales frequency distribution
Box Plot	              Sales spread and outliers
Time Series Plot          Sales over 24 months
Moving Average Plot	      3-MA and 4-MA overlay
Trend Analysis	          Actual vs Trend line
Seasonal Index	          Q1-Q4 bar chart


## 🗓️ Practical Details

| Item | Detail |
|------|--------|
| **Subject** | Business Forecasting |
| **Course** | TYBSc Data Science |
| **Maximum Marks** | 50 |
| **Software** | R and RStudio |
| **Presentation Date** | 06 August 2026 |
| **Faculty** | Asst. Prof. Raju Kukade |

---

## ⭐ Acknowledgments

- **Asst. Prof. Raju Kukade** – for his invaluable guidance, support, and expertise throughout the **Business Forecasting** practical sessions.
- **Department of Data Science**, Reena Mehta College
- **R Foundation** for the R programming language
- **FreshMart Supermarket** for the real-life dataset scenario


🧠 Learning Outcomes
Through this project, I have gained hands-on experience in:

Creating and manipulating datasets in R

Performing descriptive statistical analysis

Visualizing business data using R graphics

Analyzing time series components (trend, seasonality, cycle, irregular)

Applying moving averages (simple and weighted)

Performing linear trend analysis with regression

Calculating seasonal indices using the simple method

Interpreting results and recommending business decisions


📜 License
This project is for educational purposes as part of the TYBSc Data Science curriculum.


👨‍💻 Author
Vaibhav Singh
B.Sc. Data Science (2024–2027)
Reena Mehta College, Mumbai

GitHub: vaibhav07772

LinkedIn: Vaibhav Singh



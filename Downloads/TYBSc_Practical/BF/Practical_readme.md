# 📊 Business Forecasting – Practical Repository

This repository contains the practical work of **Business Forecasting** for TYBSc Data Science. It covers forecasting techniques, statistical analysis, data visualization, time-series analysis, sales forecasting, and business applications using R and Excel.

## 📚 Table of Contents

| Sr. No. | Practical Name |
|---|---|
| 1 | Types of Forecasting – Qualitative and Quantitative |
| 2 | Data Collection, Classification and Presentation |
| 3 | Introduction to Excel and Statistical Software for Forecasting |
| 4 | Components of Time Series |
| 5 | Simple Moving Average (SMA) and Weighted Moving Average (WMA) |
| 6 | Trend Analysis – Linear Trend Method |
| 7 | Seasonal Variation – Simple Average Method |
| 8 | Sales Forecasting and Time-Series Analysis Using R (FreshMart Case Study) |
| 9 | Demand Forecasting and Sales Forecasting Using Seasonal Variation – Ratio-to-Average Method |
| 10 | Index Numbers – Basics and Applications (Cost of Living Index Case Study) |

---

# 🧪 Practical 1: Types of Forecasting – Qualitative and Quantitative

## Aim
To study and understand qualitative and quantitative forecasting techniques.

## Theory
Forecasting is the process of predicting future events or values using past information, experience, and analytical methods.

### Types of Forecasting

**1. Qualitative Forecasting**
- Based on expert opinions and judgment.
- Used when historical data is limited.
- Examples: Expert Opinion, Market Survey, Delphi Method.

**2. Quantitative Forecasting**
- Based on historical numerical data.
- Uses mathematical and statistical methods.
- Examples: Moving Average, Regression Analysis, Time-Series Analysis.

## R Program

```r
# Qualitative Forecasting - Expert Opinion

experts <- c(100, 120, 110, 130, 115)

forecast_qualitative <- mean(experts)

print(forecast_qualitative)

# Quantitative Forecasting - Moving Average

sales <- c(100, 120, 130, 140, 150, 160)

moving_average <- mean(tail(sales, 3))

print(moving_average)
```

## Conclusion
We studied qualitative and quantitative forecasting and understood how expert opinions and historical data can be used to predict future values.

---

# 🧪 Practical 2: Data Collection, Classification and Presentation

## Aim
To collect, classify, summarize, and present data using statistical methods and graphical representations.

## Theory
Data collection is the process of gathering information. Classification organizes data into groups, while presentation uses tables and graphs to make data understandable.

## R Program

```r
# Creating a Data Frame

students <- data.frame(
  Name = c("Amit", "Rahul", "Priya", "Sneha", "Neha"),
  Marks = c(75, 82, 90, 65, 88)
)

print(students)

# Summary Statistics

summary(students$Marks)

# Frequency Table

grade <- cut(
  students$Marks,
  breaks = c(0, 40, 60, 80, 100),
  labels = c("Fail", "Average", "Good", "Excellent")
)

print(table(grade))

# Bar Chart

barplot(
  students$Marks,
  names.arg = students$Name,
  main = "Students' Marks",
  xlab = "Students",
  ylab = "Marks",
  col = "skyblue"
)

# Pie Chart

pie(
  students$Marks,
  labels = students$Name,
  main = "Marks Distribution"
)

# Histogram

hist(
  students$Marks,
  main = "Distribution of Marks",
  xlab = "Marks",
  col = "lightgreen"
)

# Box Plot

boxplot(
  students$Marks,
  main = "Box Plot of Marks",
  col = "orange"
)
```

## Conclusion
We created a data frame, classified data, calculated summary statistics, generated frequency tables, and presented data using different graphical techniques.

---

# 🧪 Practical 3: Introduction to Excel and Statistical Software for Forecasting

## Aim
To understand Excel and statistical software used for forecasting and perform forecasting using statistical techniques.

## Theory

Microsoft Excel and R are useful tools for data analysis and forecasting.

### Excel Functions
- `AVERAGE()` – Calculates average.
- `SUM()` – Calculates total.
- `FORECAST.LINEAR()` – Predicts future values using linear regression.
- Moving Average – Smooths data to identify trends.

### Statistical Methods
- Moving Average
- Linear Regression
- Time-Series Forecasting

## R Program

```r
# Historical Sales Data

sales <- c(100, 120, 140, 160, 180)

# Average

mean(sales)

# Moving Average

ma <- mean(tail(sales, 3))
print(ma)

# Linear Regression

time <- 1:5

model <- lm(sales ~ time)

print(model)

# Forecasting

future_time <- data.frame(time = 6)

prediction <- predict(model, future_time)

print(prediction)
```

## Conclusion
We studied Excel and statistical software and applied Moving Average and Linear Regression techniques for forecasting.

---

# 🧪 Practical 4: Components of Time Series

## Aim
To study and identify the different components of a time series.

## Theory

A time series is a sequence of observations recorded over a period of time.

### Components of Time Series

1. **Trend (T):** Long-term upward or downward movement.
2. **Seasonal (S):** Regular patterns occurring within a fixed period.
3. **Cyclical (C):** Long-term fluctuations related to business cycles.
4. **Random (I):** Unexpected variations caused by unpredictable events.

### Models
- Additive Model: `Y = T + S + C + I`
- Multiplicative Model: `Y = T × S × C × I`

## R Program

```r
# Creating Time Series Data

sales <- c(
  100, 120, 130, 110,
  140, 160, 170, 150,
  180, 200, 210, 190
)

ts_data <- ts(
  sales,
  start = 2023,
  frequency = 4
)

# Plot Time Series

plot(
  ts_data,
  main = "Quarterly Sales Time Series",
  xlab = "Year",
  ylab = "Sales",
  col = "blue"
)

# Time Series Decomposition

decomposition <- decompose(ts_data)

plot(decomposition)
```

## Conclusion
We created and plotted a time series and studied its trend, seasonal, cyclical, and random components.

---

# 🧪 Practical 5: Simple Moving Average (SMA) and Weighted Moving Average (WMA)

## Aim
To calculate forecasts using Simple Moving Average and Weighted Moving Average methods.

## Theory

### Simple Moving Average (SMA)
SMA calculates the average of a fixed number of recent observations.

\[
SMA = \frac{\sum X}{n}
\]

### Weighted Moving Average (WMA)
WMA assigns different weights to observations. Recent values may receive higher weights.

\[
WMA = \frac{\sum WX}{\sum W}
\]

## R Program

```r
# Sales Data

sales <- c(100, 120, 130, 140, 150)

# Simple Moving Average

sma <- mean(tail(sales, 3))

print(sma)

# Weighted Moving Average

recent_sales <- tail(sales, 3)

weights <- c(1, 2, 3)

wma <- sum(recent_sales * weights) / sum(weights)

print(wma)
```

## Conclusion
We calculated SMA and WMA forecasts and understood how moving averages help smooth historical data and predict future sales.

---

# 🧪 Practical 6: Trend Analysis – Linear Trend Method

## Aim
To analyze trends in data and forecast future values using the Linear Trend Method.

## Theory

Trend analysis identifies the long-term direction of data.

The Linear Trend Equation is:

\[
Y = a + bX
\]

Where:

- `Y` = Forecast value
- `a` = Intercept
- `b` = Slope
- `X` = Time period

## R Program

```r
# Historical Delivery Data

delivery <- c(120, 135, 150, 165, 180, 195)

time <- 1:6

# Linear Trend Model

model <- lm(delivery ~ time)

print(summary(model))

# Trend Line

plot(
  time,
  delivery,
  main = "Linear Trend Analysis",
  xlab = "Time",
  ylab = "Delivery",
  pch = 19
)

abline(model, col = "red")

# Forecast for July

future <- data.frame(time = 7)

forecast <- predict(model, future)

print(forecast)
```

## Conclusion
We applied Linear Regression to identify the trend and forecast future delivery values.

---

# 🧪 Practical 7: Seasonal Variation – Simple Average Method

## Aim
To calculate seasonal indices and analyze seasonal variations using the Simple Average Method.

## Theory

Seasonal variation refers to regular fluctuations in data occurring during particular periods, such as months, quarters, or seasons.

### Seasonal Index

\[
Seasonal\ Index =
\frac{Seasonal\ Average}{Overall\ Average}
\times 100
\]

## R Program

```r
# Quarterly Sales Data

sales <- c(
  100, 120, 150, 130,
  110, 130, 160, 140,
  120, 140, 170, 150
)

# Creating Matrix

sales_matrix <- matrix(
  sales,
  nrow = 3,
  byrow = TRUE
)

colnames(sales_matrix) <- c(
  "Q1", "Q2", "Q3", "Q4"
)

print(sales_matrix)

# Quarterly Averages

quarterly_avg <- colMeans(sales_matrix)

print(quarterly_avg)

# Overall Average

overall_avg <- mean(sales)

print(overall_avg)

# Seasonal Indices

seasonal_index <- (
  quarterly_avg / overall_avg
) * 100

print(seasonal_index)

# Visualization

barplot(
  seasonal_index,
  main = "Quarterly Seasonal Indices",
  xlab = "Quarter",
  ylab = "Seasonal Index",
  col = "lightblue"
)
```

## Conclusion
We calculated quarterly averages and seasonal indices to identify seasonal patterns in business sales.

---

# 🧪 Practical 8: Sales Forecasting and Time-Series Analysis Using R – FreshMart Case Study

## Aim
To perform sales forecasting and time-series analysis using R for the FreshMart business case study.

## Theory
Sales forecasting helps businesses estimate future sales based on historical data. Time-series analysis identifies patterns, trends, and seasonal fluctuations.

## R Program

```r
# FreshMart Sales Data

sales <- c(
  120, 140, 160, 130,
  150, 170, 190, 160,
  180, 200, 220, 190
)

# Creating Data Frame

freshmart <- data.frame(
  Month = 1:length(sales),
  Sales = sales
)

print(freshmart)

# Summary Statistics

summary(freshmart$Sales)

# Visualization

plot(
  sales,
  type = "o",
  main = "FreshMart Sales",
  xlab = "Month",
  ylab = "Sales",
  col = "blue"
)

# Time Series

ts_sales <- ts(
  sales,
  start = 2023,
  frequency = 4
)

plot(ts_sales)

# Moving Average

sma <- mean(tail(sales, 3))

print(sma)

# Linear Trend

time <- 1:length(sales)

model <- lm(sales ~ time)

print(summary(model))

# Forecast

future <- data.frame(time = length(sales) + 1)

forecast <- predict(model, future)

print(forecast)

# Seasonal Analysis

decomposition <- decompose(ts_sales)

plot(decomposition)
```

## Conclusion
We performed data analysis, visualization, time-series analysis, trend forecasting, and seasonal analysis using R for the FreshMart case study.

---

# 🧪 Practical 9: Demand Forecasting and Sales Forecasting Using Seasonal Variation – Ratio-to-Average Method

## Aim
To forecast demand and sales by calculating seasonal indices using the Ratio-to-Average Method.

## Theory

The Ratio-to-Average Method identifies seasonal variation by comparing actual observations with their corresponding moving averages.

### Formula

\[
Seasonal\ Ratio =
\frac{Actual\ Value}{Moving\ Average}
\times 100
\]

Seasonal ratios are averaged to calculate seasonal indices, which are then used for forecasting.

## R Program

```r
# Quarterly Sales Data

sales <- c(
  100, 120, 150, 130,
  110, 130, 160, 140,
  120, 140, 170, 150
)

# Time Series

ts_sales <- ts(
  sales,
  start = 2023,
  frequency = 4
)

# Moving Average

moving_avg <- stats::filter(
  ts_sales,
  filter = rep(1/4, 4),
  sides = 2
)

# Plot

plot(
  ts_sales,
  main = "Sales and Seasonal Variation",
  xlab = "Year",
  ylab = "Sales",
  col = "blue"
)

print(moving_avg)
```

## Conclusion
We studied seasonal forecasting and understood how seasonal ratios and indices help predict demand and sales.

---

# 🧪 Practical 10: Index Numbers – Basics and Applications (Cost of Living Index Case Study)

## Aim
To understand index numbers and calculate the Cost of Living Index.

## Theory

An index number measures changes in prices, quantities, or values over time compared with a base period.

### Formula

\[
Index\ Number =
\frac{Current\ Year\ Value}{Base\ Year\ Value}
\times 100
\]

### Applications
- Cost of Living Index
- Price comparison
- Economic analysis
- Inflation measurement
- Purchasing power analysis

## R Program

```r
# Cost of Living Data

base_price <- c(100, 200, 150, 250)

current_price <- c(120, 230, 180, 300)

# Price Relative

price_relative <- (
  current_price / base_price
) * 100

print(price_relative)

# Simple Average Index

cost_of_living_index <- mean(price_relative)

print(cost_of_living_index)

# Visualization

barplot(
  price_relative,
  main = "Price Index",
  xlab = "Items",
  ylab = "Index Number",
  col = "orange"
)
```

## Conclusion
We studied index numbers and calculated price relatives and the Cost of Living Index to understand changes in prices over time.

---

# 🛠️ Tools & Technologies

- **R Programming**
- **RStudio**
- **Microsoft Excel**
- **Statistical Analysis**
- **Time-Series Analysis**
- **Data Visualization**
- **Forecasting Techniques**

---

# 🎯 Learning Outcomes

After completing these practicals, we can:

- Understand qualitative and quantitative forecasting.
- Collect, classify, and present data.
- Calculate statistical measures.
- Perform Moving Average and Weighted Moving Average forecasting.
- Analyze trends using Linear Regression.
- Understand time-series components.
- Calculate seasonal indices.
- Perform sales and demand forecasting.
- Apply index numbers in business analysis.
- Interpret forecasting results for decision-making.

---

## 👨‍🎓 Academic Information

**Course:** TYBSc Data Science  
**Subject:** Business Forecasting  
**Repository Purpose:** Academic Practical Work and Learning

---

⭐ *This repository is intended for educational purposes and practical learning in Business Forecasting.*
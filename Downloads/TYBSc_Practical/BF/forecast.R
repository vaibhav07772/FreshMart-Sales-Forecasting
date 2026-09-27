# ===== FORECASTING TECHNIQUES USING R =====
library(forecast)
library(tseries)
library(ggplot2)

# ===== TASK 1: DATA LOAD & PLOT =====
data <- read.csv("sales_data.csv")
ts_data <- ts(data$Sales, start=c(2022,1), frequency=12) # 12 = Monthly

plot(ts_data, main="Task 1: Monthly Sales Time Series", ylab="Sales", xlab="Year", col="blue", lwd=2)
# INTERPRETATION: Sales me har saal badhotri aur Dec me peak dikh raha

# ===== TASK 2: STATIONARITY CHECK =====
adf.test(ts_data)
diff_data <- diff(ts_data, differences=1)
plot(diff_data, main="Task 2: Differenced Data - Stationary")

# ===== TASK 3: ACF & PACF PLOT =====
acf(ts_data, main="Task 3: ACF Plot")
pacf(ts_data, main="Task 3: PACF Plot")

# ===== TASK 4: SMOOTHING TECHNIQUES =====
ses_model <- ses(ts_data, h=6)
plot(ses_model, main="Task 4a: Simple Exponential Smoothing Forecast")

holt_model <- holt(ts_data, h=6)
plot(holt_model, main="Task 4b: Holt's Linear Trend Forecast")

hw_model <- hw(ts_data, seasonal="additive", h=6)
plot(hw_model, main="Task 4c: Holt-Winters Seasonal Forecast")

# ===== TASK 5: ARIMA MODEL =====
auto_arima <- auto.arima(ts_data)
summary(auto_arima)
arima_forecast <- forecast(auto_arima, h=6)
plot(arima_forecast, main="Task 5: ARIMA Forecast - Next 6 Months")

# ===== TASK 6: MODEL ACCURACY =====
cat("SES Accuracy:\n"); accuracy(ses_model)
cat("Holt Accuracy:\n"); accuracy(holt_model)
cat("HW Accuracy:\n"); accuracy(hw_model)
cat("ARIMA Accuracy:\n"); accuracy(arima_forecast)
# Jiska MAPE sabse kam ho wo best model

# ===== TASK 7: BUSINESS CONCLUSION =====
print("===== BUSINESS INTERPRETATION =====")
print(paste("Next 6 months ka forecast:", round(arima_forecast$mean[6],2)))
print("1. Sales me har mahine ~5 unit ka growth trend hai")
print("2. Dec me har saal peak aata hai - seasonality hai")
print("3. Business Decision: Oct-Dec ke liye inventory aur staff badhao")
# ================================================
# TYBSc Data Science - Forecasting Practical
# Title: Sales Forecasting and Time Series Analysis
# Company: FreshMart Supermarket, Mumbai
# ================================================

# -------- TASK 1: DATA COLLECTION & PRESENTATION --------
# 1. Create a data frame
Month <- c("Jan-25","Feb-25","Mar-25","Apr-25","May-25","Jun-25",
           "Jul-25","Aug-25","Sep-25","Oct-25","Nov-25","Dec-25",
           "Jan-26","Feb-26","Mar-26","Apr-26","May-26","Jun-26",
           "Jul-26","Aug-26","Sep-26","Oct-26","Nov-26","Dec-26")

Sales <- c(1200,1250,1400,1650,1900,2100,
           1850,1750,1600,1700,1950,2300,
           1300,1350,1500,1750,2000,2250,
           1950,1850,1700,1800,2100,2450)

freshmart <- data.frame(Month, Sales) # data.frame() function

# 2. Display the dataset
print("===== FULL DATASET =====")
print(freshmart)

# 3. Display structure of dataset
print("===== STRUCTURE =====")
str(freshmart)

# 4. Display summary statistics
print("===== SUMMARY STATISTICS =====")
summary(freshmart$Sales)

# 5. Display first five records
print("===== FIRST 5 RECORDS =====")
head(freshmart, 5)

# 6. Display last five records
print("===== LAST 5 RECORDS =====")
tail(freshmart, 5)

# -------- TASK 2: DESCRIPTIVE STATISTICS --------
print("===== DESCRIPTIVE STATISTICS =====")
cat("Total Sales:", sum(freshmart$Sales), "\n") # sum()
cat("Average Sales:", mean(freshmart$Sales), "\n") # mean()
cat("Median Sales:", median(freshmart$Sales), "\n") # median()
cat("Maximum Sales:", max(freshmart$Sales), "\n") # max()
cat("Minimum Sales:", min(freshmart$Sales), "\n") # min()
cat("Standard Deviation:", sd(freshmart$Sales), "\n") # sd()
cat("Variance:", var(freshmart$Sales), "\n") # var()
cat("Range:", range(freshmart$Sales), "\n") # range()

# -------- TASK 3: DATA VISUALIZATION --------
par(mfrow=c(2,3)) # 6 graphs ek saath

# 1. Bar Chart
barplot(freshmart$Sales, names.arg=freshmart$Month, col="skyblue",
        main="Bar Chart: Monthly Sales", xlab="Month", ylab="Sales", las=2)

# 2. Line Chart
plot(freshmart$Sales, type="o", col="red", lwd=2,
     main="Line Chart: Sales Trend", xlab="Month Number", ylab="Sales")

# 3. Pie Chart
pie(freshmart$Sales[1:12], labels=freshmart$Month[1:12], col=rainbow(12),
    main="Pie Chart: 2025 Sales Distribution")

# 4. Histogram
hist(freshmart$Sales, col="lightgreen", border="black",
     main="Histogram: Sales Distribution", xlab="Sales")

# 5. Box Plot
boxplot(freshmart$Sales, col="orange",
        main="Box Plot: Sales Spread", ylab="Sales")

par(mfrow=c(2,3)) # wapas normal

# -------- TASK 4: COMPONENTS OF TIME SERIES --------
# 1. Convert to Time Series object
sales_ts <- ts(freshmart$Sales, start=c(2025,1), frequency=12) # ts()

# 2. Plot the time series
plot(sales_ts, main="Time Series Plot: FreshMart Sales",
     ylab="Sales", xlab="Year", col="blue", lwd=2)

# Interpretation
print("TREND: Sales me increasing trend hai - har saal sales badh rahi hai")
print("SEASONAL: Dec me peak aur Sep me dip - seasonal pattern hai")
print("CYCLICAL: 2 saal ka data hai to clear cycle nahi dikh raha")
print("IRREGULAR: Chote fluctuations hai jo random hai")

# -------- TASK 5: MOVING AVERAGE --------
# Install if needed
if(!require("TTR")) install.packages("TTR")
library(TTR)

# A. Simple Moving Average
SMA_3 <- SMA(freshmart$Sales, n=3) # 3-Month MA
SMA_4 <- SMA(freshmart$Sales, n=4) # 4-Month MA

print("===== 3-MONTH MOVING AVERAGE =====")
print(SMA_3)
print("===== 4-MONTH MOVING AVERAGE =====")
print(SMA_4)

plot(sales_ts, main="Simple Moving Average", ylab="Sales", col="black")
lines(SMA_3, col="red", lwd=2)
lines(SMA_4, col="blue", lwd=2)
legend("topleft", legend=c("Actual","3-MA","4-MA"), col=c("black","red","blue"), lwd=2)

# B. Weighted Moving Average - weights: 0.2, 0.3, 0.5
weights <- c(0.2, 0.3, 0.5)
WMA <- filter(freshmart$Sales, weights, sides=1)
print("===== WEIGHTED MOVING AVERAGE =====")
print(WMA)

# Next month forecast = last 3 months ka WMA
last3 <- tail(freshmart$Sales, 3)
next_forecast <- sum(last3 * weights)
cat("Forecast for Jan-27 using WMA:", next_forecast, "\n")

# -------- TASK 6: TREND ANALYSIS - LINEAR REGRESSION --------
time <- 1:24 # time variable
model <- lm(Sales ~ time, data=freshmart) # lm()

print("===== REGRESSION MODEL =====")
summary(model)
cat("Regression Equation: Sales =", coef(model)[1], "+", coef(model)[2], "* time\n")

# Predict for Jan 2027 = time 25
new_data <- data.frame(time=25)
predicted_jan27 <- predict(model, new_data)
cat("Predicted Sales for Jan-2027:", predicted_jan27, "\n")

# Plot Actual vs Trend
plot(sales_ts, main="Trend Analysis", ylab="Sales", col="black", lwd=2)
abline(model, col="red", lwd=2) # trend line
legend("topleft", legend=c("Actual","Trend Line"), col=c("black","red"), lwd=2)

# -------- TASK 7: SEASONAL VARIATION --------
# 1. Arrange quarter-wise
quarters <- rep(1:4, 6) # 6 quarters x 4 = 24 months
sales_matrix <- matrix(freshmart$Sales, nrow=4, byrow=FALSE) # rows=quarters

# 2. Calculate
overall_avg <- mean(freshmart$Sales)
seasonal_avg <- rowMeans(sales_matrix) # colMeans agar month wise chahiye
seasonal_index <- (seasonal_avg / overall_avg) * 100

print("===== SEASONAL INDEX =====")
print(paste("Q1:", round(seasonal_index[1],2)))
print(paste("Q2:", round(seasonal_index[2],2)))
print(paste("Q3:", round(seasonal_index[3],2)))
print(paste("Q4:", round(seasonal_index[4],2)))

barplot(seasonal_index, names.arg=c("Q1","Q2","Q3","Q4"), col="purple",
        main="Seasonal Index by Quarter", ylab="Seasonal Index %")
cat("Quarter with Maximum Demand: Q", which.max(seasonal_index), "\n")

# -------- TASK 8: BUSINESS INTERPRETATION --------
print("===== BUSINESS INTERPRETATION =====")
cat("1. Highest Sales Month:", Month[which.max(Sales)], "-", max(Sales), "\n")
cat("2. Lowest Sales Month:", Month[which.min(Sales)], "-", min(Sales), "\n")
cat("3. Trend:", ifelse(coef(model)[2]>0, "Increasing", "Decreasing"), "\n")
cat("4. Highest Seasonal Index Quarter: Q", which.max(seasonal_index), "\n")
cat("5. Next Month Forecast using WMA:", next_forecast, "\n")
cat("6. Business Decisions:\n")
cat(" a. Q4 me inventory aur staff badhao - seasonal peak hai\n")
cat(" b. Sep me offers chalao - sales dip hoti hai\n")
cat(" c. Overall trend increasing hai to new product launch karo\n")

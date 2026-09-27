# 🛒 FreshMart Supermarket - Sales Forecasting & Time Series Analysis (Hinglish Edition)

---

## 🎯 **Ye Project Kya Hai? (Overview)**

Bhai, ye project **FreshMart Supermarket, Mumbai** ke liye banaya gaya hai. Isme humne **Fruit Juice** ki monthly sales data (2 saal ka — Jan 2025 se Dec 2026) ko analyze kiya hai. Goal tha ki **trend, seasonality, aur future sales** ka pata lagayein taaki management ko business decisions lene mein help mile.

**Ek Line Mein:**  
*"Data ko samjho, usme pattern dhundo, aur future ke liye forecast karo."*

---

## 📊 **Data Kaisa Hai? (Dataset)**

| Variable | Type | Description |
|----------|------|-------------|
| `Month` | Character | Month-Year (e.g., Jan-25, Feb-25, ...) |
| `Sales` | Numeric | Monthly sales in Rupees (₹) |

**Time Period:** 24 months (Jan 2025 – Dec 2026)

| Statistic | Value |
|-----------|-------|
| **Total Sales** | ₹42,650 |
| **Average Monthly Sales** | ₹1,777.08 |
| **Median Sales** | ₹1,775 |
| **Maximum Sales** | ₹2,450 (Dec-26) |
| **Minimum Sales** | ₹1,200 (Jan-25) |
| **Standard Deviation** | ₹335.89 |
| **Variance** | 112,821.6 |
| **Range** | ₹1,200 – ₹2,450 |

**Matlab:** Sales me 1200 se 2450 tak ka fluctuation hai. Average 1777 hai, par kuch mahine me sale kam toh kuch me zyada. Iska matlab **seasonality** hai — kuch months me naturally sales badhti hai (jaise festive season).

---

## 🧰 **Kya Use Kiya? (Tools & Technologies)**

| Tool | Purpose |
|------|---------|
| **R Programming** | Data manipulation, analysis, aur forecasting |
| **RStudio** | IDE for writing and executing R scripts |
| **R Packages** | `base`, `stats`, `graphics`, `TTR` (Moving Average ke liye) |

---

## 🗂️ **Project Structure**
FreshMart-Forecast/
├── FreshMart_Forecast.R # Complete R script with all tasks
├── README_Hinglish.md # Ye file (Hinglish explanation)
├── ARIMA_Forecast.png # ARIMA forecast plot
├── final_plot.png # Combined plots (MA, Trend, Seasonal)
├── forecast.R # Alternative R script
└── sales_data.csv # Raw dataset



---

## 📋 **Tasks (Kya-Kya Kiya?)**

### ✅ Task 1: Data Collection & Presentation (8 Marks)

**Kya Kiya?**
- Ek data frame (`freshmart`) banaya jisme Month aur Sales columns hain.
- Dataset ko display kiya, structure (`str()`) check kiya, summary statistics (`summary()`) nikali.
- `head()` aur `tail()` se pehle aur aakhri 5 records dekhe.

**R Functions Used:** `data.frame()`, `str()`, `summary()`, `head()`, `tail()`

**Kyun?** Taaki data ka overview mile aur aage ke analysis ke liye data ready ho.

---

### ✅ Task 2: Descriptive Statistics (7 Marks)

**Kya Kiya?**
- Total Sales: `sum()` — 42650
- Average Sales: `mean()` — 1777.08
- Median Sales: `median()` — 1775
- Maximum Sales: `max()` — 2450
- Minimum Sales: `min()` — 1200
- Standard Deviation: `sd()` — 335.89
- Variance: `var()` — 112821.6
- Range: `range()` — 1200 to 2450

**Kyun?** Sales ki basic understanding ke liye — kitni average hai, kitna spread hai, extremes kya hain.

---

### ✅ Task 3: Data Visualization (8 Marks)

**5 Graphs Banaye:**

| Chart | Purpose |
|-------|---------|
| **Bar Chart** | Monthly sales comparison — kaunse month me zyada/kaam sales |
| **Line Chart** | Sales trend over time — overall direction |
| **Pie Chart** | 2025 sales distribution — kaunse month ka kitna contribution |
| **Histogram** | Sales frequency distribution — kitni baar konsi range aayi |
| **Box Plot** | Sales spread and outliers — koi extreme value hai ya nahi |

**R Functions Used:** `barplot()`, `plot()`, `pie()`, `hist()`, `boxplot()`

**Kyun?** Numbers se zyada graphs se pattern clear dikhta hai. Teacher ko bhi graphs pasand aate hain!

---

### ✅ Task 4: Time Series Analysis (6 Marks)

**Kya Kiya?**
- `ts()` function se data ko time series object mein convert kiya (frequency=12 for monthly data).
- Time series plot banaya.

**Components Identified:**

| Component | Finding |
|-----------|---------|
| **Trend** | Increasing 📈 (Sales badh rahi hai) |
| **Seasonal** | December peak, September dip |
| **Cyclical** | Not clearly visible (2 saal ka data hai) |
| **Irregular** | Minor random fluctuations |

**Kyun?** Ye 4 components time series analysis ki foundation hain. Inhe samjhe bina forecasting nahi kar sakte.

---

### ✅ Task 5: Moving Average (8 Marks)

**A. Simple Moving Average**

| Period | 3-MA | 4-MA |
|--------|------|------|
| Jan-25 | NA | NA |
| ... | ... | ... |
| Dec-26 | 2116.67 | 2012.50 |

- **3-MA:** Actual ke close follow karta hai.
- **4-MA:** Thoda smooth hai, actual se thoda piche lagta hai.

**B. Weighted Moving Average**

**Weights:** `0.2 (Oldest)`, `0.3 (Middle)`, `0.5 (Latest)`

**Jan 2027 Forecast:**
Last 3 months: Oct-26 (1800), Nov-26 (2100), Dec-26 (2450)
WMA = (0.2 × 1800) + (0.3 × 2100) + (0.5 × 2450)
WMA = 360 + 630 + 1225 = 2215



**Forecast:** ₹2,215 for January 2027

**Kyun?** Weighted MA latest month ko zyada importance deta hai, kyunki recent trends future ke liye zyada relevant hote hain.

---

### ✅ Task 6: Trend Analysis (7 Marks)

**Regression Model:**
Sales = 1471.377 + 24.45652 × time



**Interpretation:**
- **Intercept (1471.377):** Base sales jab time = 0
- **Slope (24.45652):** Har month sales ₹24.46 badh rahi hai.

**Jan 2027 Forecast:**
time = 25 (kyunki 24 months ho gaye)
Sales = 1471.377 + 24.45652 × 25
Sales = 1471.377 + 611.413 = 2082.79



**Forecast:** ₹2,083 (Regression) vs ₹2,215 (WMA)

**Kyun?** Regression long-term trend capture karta hai. WMA short-term recent trends ko zyada weight deta hai.

---

### ✅ Task 7: Seasonal Variation (6 Marks)

| Quarter | Seasonal Average | Seasonal Index |
|---------|------------------|----------------|
| **Q1** (Jan-Mar) | 1616.67 | 90.97% |
| **Q2** (Apr-Jun) | 1933.33 | 98.01% |
| **Q3** (Jul-Sep) | 1816.67 | 100.82% |
| **Q4** (Oct-Dec) | **2141.67** | **110.2%** 🚀 |

**Interpretation:**
- **Q4** me sales average se 10.2% zyada hai — festive season effect (Diwali/Christmas).
- **Q1** me sales average se 9% kam hai — post-holiday slump.

**Highest Demand Quarter:** Q4 (October–December)

**Kyun?** Seasonality samajhna business ke liye bahut important hai — inventory, staffing, aur marketing planning ke liye.

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

## 💼 **Business Recommendations**

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

5. **Collect more data**
   - 2 years of data is limited
   - More data → better predictions

---

## 🧠 **Viva Ke Liye Important Questions & Answers**

### Q1: **Ye assignment kyun banayi?**
**A:** FreshMart supermarket ki monthly sales analyze karni thi, trend aur seasonality find karni thi, aur future sales forecast karni thi.

### Q2: **Time series kya hai?**
**A:** Time series data wo hota hai jo time ke hisaab se record kiya jata hai — jaise monthly sales, daily temperature, etc.

### Q3: **Trend kya hai?**
**A:** Trend long-term direction hai — increasing, decreasing, ya stable. Hamare case mein increasing trend hai.

### Q4: **Seasonality kya hai?**
**A:** Regular pattern jo har saal repeat hota hai — jaise December me sales peak, September me dip.

### Q5: **Moving Average kyu use karte hain?**
**A:** Short-term fluctuations smooth karne ke liye, taaki underlying trend clear dikhe.

### Q6: **Weighted MA ka kya fayda?**
**A:** Recent observations ko zyada importance deta hai, kyunki wo future ke liye zyada relevant hain.

### Q7: **Regression equation ka kya matlab hai?**
**A:** Sales = 1471.377 + 24.45652 × time. Matlab har month sales ₹24.46 badh rahi hai.

### Q8: **Seasonal Index ka kya matlab hai?**
**A:** Q4 ka index 110.2% hai, matlab average se 10.2% zyada sales. Q1 ka 90.97% hai, matlab average se 9.03% kam.

### Q9: **Forecast ke liye kaunsi method better hai?**
**A:** WMA short-term ke liye better hai (2215), Regression long-term trend ke liye better hai (2083). Dono ka combination use karte hain.

### Q10: **Business ko kya suggest karoge?**
**A:** 1. Q4 me inventory/staff badhao, 2. September me offers chalao, 3. New products launch karo.

---

## 🗓️ **Practical Details**

| Item | Detail |
|------|--------|
| **Subject** | Business Forecasting |
| **Course** | TYBSc Data Science |
| **Maximum Marks** | 50 |
| **Software** | R and RStudio |
| **Presentation Date** | 06 August 2026 |
| **Faculty** | Asst. Prof. Raju Kukade |

---

## ⭐ **Acknowledgments**

- **Asst. Prof. Raju Kukade** – for his invaluable guidance, support, and expertise throughout the Business Forecasting practical sessions.
- **Department of Data Science**, Reena Mehta College
- **R Foundation** for the R programming language
- **FreshMart Supermarket** for the real-life dataset scenario

---

## 👨‍💻 **Author**

**Vaibhav Singh**  
B.Sc. Data Science (2024–2027)  
Reena Mehta College, Mumbai  

- **GitHub:** [vaibhav07772](https://github.com/vaibhav07772)
- **LinkedIn:** [Vaibhav Singh](https://www.linkedin.com/in/vaibhav-singh-9a9b9434a/)

---

> *"Data is the new oil, and forecasting is the engine that drives business success."*

---

## ✅ **Viva Ke Liye Ready!**

- ✅ Sab tasks complete hain
- ✅ Output verified hai
- ✅ Har step ka reason samajh mein aata hai
- ✅ Teacher ko sab explain kar sakte ho

**Bhai, ab 6 August ko confidence ke saath jaana! 🚀😎**




## ----> Kya Ho Raha Hai?
Maine FreshMart Supermarket ke 2 saal (24 months) ke monthly sales data ka R programming mein Time Series Analysis kiya hai — trend, seasonality, aur forecasting sab cover hai.

Kyu Kiya?
Management ko sales patterns samjhaane, future sales predict karne, aur business decisions (inventory, staffing, offers) ke liye data-driven recommendations dene ke liye.

Kaise Kiya?
R mein data.frame, ts(), SMA(), lm(), aur matrix() functions use karke Descriptive Stats, Graphs, Moving Averages, Regression, aur Seasonal Index calculate kiye.

Kya Nikal Ke Aaya?

Trend: Increasing 📈 (har month ₹24.45 growth)

Seasonal Peak: Q4 (Oct-Dec) — 110.2% above average

Forecast Jan 2027: ₹2,215 (WMA) / ₹2,083 (Regression)

Aage Kya Kar Sakte Hain?

Viva ke liye live R execution practice karo (6 Aug).

Isko Shiny Dashboard mein convert karo taaki interactive ho.

Aur data collect karo, ARIMA ya Prophet model lagao, aur product-wise forecasting expand karo. 🚀


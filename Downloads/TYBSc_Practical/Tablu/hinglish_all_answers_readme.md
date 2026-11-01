# 📊 Tableau Practical Exam – Complete Preparation Guide

**Subject:** Data Visualization using Tableau  
**Practicals:** 1 to 15  
**Language:** Simple Hinglish  
**Purpose:** Practical Exam + Viva Preparation

---

# 📌 Table of Contents

1. Practical 1 – Basic Visualizations
2. Practical 2 – Data Sources & Data Preparation
3. Practical 3 – Advanced Visualizations
4. Practical 4 – Calculations in Tableau
5. Practical 5 – Table Calculations
6. Practical 6 – Dashboard Formatting
7. Practical 7 – Interactive Dashboard & Stories
8. Practical 8 – Advanced Analytics
9. Practical 9 – Data Cleaning & Structuring
10. Practical 10 – Tableau Prep
11. Practical 11 – Advanced Visualizations
12. Practical 12 – Sharing & Publishing
13. Practical 13 – Retail Sales & Profitability Dashboard
14. Practical 14 – Customer Segmentation & Behavior Analysis
15. Practical 15 – Sales Forecasting & Trend Analysis
16. Important Formulas
17. Last-Minute Revision

---

# Practical 1: Getting Started with Tableau and Basic Visualizations

## Objective
Tableau interface explore karna aur basic visualizations create karna.

### A. Connect CSV Dataset
1. Tableau Desktop open karo.
2. Connect → Text File select karo.
3. CSV dataset choose karo.
4. Data Source page par data check karo.
5. Sheet 1 par click karo.

### B. Identify Dimensions and Measures

**Dimensions:** Category, Region, State, Customer Name

**Measures:** Sales, Profit, Quantity, Discount

### C. Convert Discrete and Continuous
1. Field par right-click karo.
2. Convert to Discrete ya Convert to Continuous select karo.
3. Chart mein changes observe karo.

### D. Bar Chart
- Columns → Category
- Rows → Sales
- Show Me → Bar Chart

### E. Line Chart
- Columns → Order Date
- Rows → Sales
- Date ko Month par set karo.
- Show Me → Line Chart

### F. Geographic Map
1. State par double-click karo.
2. Sales ko Color mein drag karo.
3. Marks → Map select karo.

### G. Dashboard
1. New Dashboard open karo.
2. Worksheets drag karo.
3. Title add karo.
4. Dashboard save karo.

---

# Practical 2: Working with Data Sources and Data Preparation

## Objective
Different data sources connect karna aur data prepare karna.

### A. Connect Data Sources
Connect → Excel / Text File / Database → Dataset select.

### B. Live vs Extract

- **Live:** Original data source se directly connect hota hai.
- **Extract:** Data ki stored copy hoti hai, jo generally faster analysis ke liye use hoti hai.

### C. Manage Metadata
1. Data Source page open karo.
2. Field par right-click karo.
3. Rename, Hide ya Change Data Type select karo.

### D. Joins
1. Second table drag karo.
2. Common field select karo.
3. Join type choose karo.

| Join Type | Meaning |
|---|---|
| Inner Join | Sirf matching records |
| Left Join | Left table ke saare records |
| Right Join | Right table ke saare records |
| Full Outer Join | Dono tables ke saare records |

### E. Data Blending
1. Do data sources connect karo.
2. Primary source select karo.
3. Secondary source se common field use karo.
4. Relationship verify karo.

### F. Filters
- Dimension Filter → Category, Region
- Measure Filter → Sales, Profit
- Date Filter → Order Date

Field par right-click → Show Filter.

### G. Performance Optimization
Unused fields hide karo aur unnecessary data filters apply karo.

---

# Practical 3: Creating Advanced Visualizations

## Objective
Different charts create karke data comparison aur analysis karna.

| Chart | Columns | Rows |
|---|---|---|
| Stacked Bar | Category | Sales |
| Grouped Bar | Category | Sales |
| Pie Chart | Category | Sales |
| Treemap | Category | Sales |
| Scatter Plot | Sales | Profit |
| Histogram | Sales (Bins) | Number of Records |
| Box Plot | Category | Sales |
| Gantt Chart | Order Date | Duration |

## A. Stacked Bar Chart
Category → Columns, Sales → Rows, Sub-Category → Color.

## B. Grouped Bar Chart
Category → Columns, Sales → Rows, Sub-Category → Columns.

## C. Pie Chart
Category → Color, Sales → Angle → Show Me → Pie Chart.

## D. Treemap
Category → Color, Sales → Size → Show Me → Treemap.

## E. Scatter Plot
Sales → Columns, Profit → Rows, Customer Name → Detail.

## F. Histogram
1. Sales par right-click karo.
2. Create → Bins select karo.
3. Sales (Bins) → Columns.
4. Number of Records → Rows.

## G. Box-and-Whisker Plot
Category → Columns, Sales → Rows → Show Me → Box Plot.

## H. Gantt Chart
Order Date → Rows, Duration → Size, Marks → Gantt Bar.

---

# Practical 4: Performing Data Analysis using Calculations

## Objective
Calculated fields, row-level, aggregate aur LOD calculations perform karna.

### Calculated Field Create Karna
Data Pane → Right-click → Create Calculated Field → Name → Formula → OK.

## A. Basic Calculation
```tableau
[Sales] - [Profit]
```

## B. Row-Level Calculation
```tableau
[Sales] * [Quantity]
```

## C. Aggregate Calculation
```tableau
SUM([Sales]) / SUM([Profit])
```

## D. FIXED LOD
```tableau
{ FIXED [Customer Name] : SUM([Sales]) }
```

## E. INCLUDE LOD
```tableau
{ INCLUDE [Customer Name] : SUM([Sales]) }
```

## F. EXCLUDE LOD
```tableau
{ EXCLUDE [Category] : SUM([Sales]) }
```

## G. Parameters
1. Data Pane → Create Parameter.
2. Parameter name aur data type select karo.
3. Allowable values set karo.
4. Show Parameter.
5. Calculated Field mein parameter use karo.

---

# Practical 5: Analyzing Data using Table Calculations

## Objective
Running total, moving average, ranking aur cumulative calculations perform karna.

## A. Running Total
1. Order Date → Columns.
2. Sales → Rows.
3. Sales par right-click.
4. Quick Table Calculation → Running Total.

## B. Percent of Total
Sales → Quick Table Calculation → Percent of Total.

## C. Moving Average
```tableau
WINDOW_AVG(SUM([Sales]), -2, 0)
```

## D. Year-over-Year Growth
1. Sales select karo.
2. Quick Table Calculation → Percent Difference.
3. Compute Using → Year.

## E. Ranking
```tableau
RANK(SUM([Sales]))
```

## F. Window Sum
```tableau
WINDOW_SUM(SUM([Sales]))
```

## G. Window Average
```tableau
WINDOW_AVG(SUM([Sales]))
```

**Important:** Edit Table Calculation mein Compute Using aur Partitioning check karo.

---

# Practical 6: Designing Effective Dashboards

## Objective
Professional aur visually appealing dashboard create karna.

1. New Dashboard open karo.
2. Worksheets drag karo.
3. Dashboard title add karo.
4. Worksheet aur workbook formatting apply karo.
5. Number aur date format customize karo.
6. Color schemes aur layout improve karo.
7. Tooltip edit karo → Marks → Tooltip.
8. Viz in Tooltip → Tooltip → Insert → Sheets.
9. Unnecessary legends remove karo.
10. Filters aur readability improve karo.

---

# Practical 7: Interactive Dashboards and Data Stories

## Objective
Interactive dashboards create karna aur Story feature use karna.

## A. Dashboard Layout
New Dashboard → Worksheets drag karo.

## B. Filters and Controls
Worksheet dropdown → Filters → Region / Category.

## C. Filter Action
Dashboard → Actions → Add Action → Filter.

## D. Highlight Action
Dashboard → Actions → Add Action → Highlight.

## E. URL Action
Dashboard → Actions → Add Action → Go to URL.

## F. Dynamic Dashboard
1. Parameter create karo.
2. Show Parameter.
3. Calculated Field mein parameter use karo.
4. Dashboard ko dynamic banao.

## G. Device Layout
Dashboard → Device Preview → Desktop / Tablet / Phone.

## H. Story
New Story → Worksheets drag karo → Caption add karo → Story Points create karo.

---

# Practical 8: Advanced Analytics – Trends, Clustering & Forecasting

## Objective
Trend lines, clustering aur forecasting apply karna.

## A. Trend Line
1. Scatter Plot create karo.
2. Analytics tab open karo.
3. Trend Line ko chart par drag karo.
4. Linear / Exponential select karo.

## B. Trend Model
Trend Line par right-click → Describe Trend Model.

## C. Clustering
1. Scatter Plot create karo.
2. Analytics → Cluster drag karo.
3. Number of clusters select karo.
4. Similar groups observe karo.

## D. Distribution Analysis
Analytics → Distribution Band / Box Plot drag karo.

## E. Forecasting
1. Order Date → Columns.
2. Sales → Rows.
3. Analytics → Forecast drag karo.

## F. Statistical Model
Forecast par right-click → Describe Forecast.

## G. Export Results
Worksheet → Export → Image / PDF (available options ke according).

---

# Practical 9: Cleaning and Structuring Data

## Objective
Missing values, pivot, union aur data cleaning perform karna.

## A. Missing Values
```tableau
IFNULL([Category], "Unknown")
```

## B. Wide to Tall Format (Pivot)
1. Data Source page open karo.
2. Multiple column headers select karo.
3. Right-click → Pivot.
4. Pivot Field Names aur Values rename karo.

## C. Union
1. Data Source page open karo.
2. New Union drag karo.
3. Multiple files add karo.
4. Combined data verify karo.

## D. Cross-Database Join
1. Excel aur CSV connect karo.
2. Common field select karo.
3. Join type choose karo.
4. Result verify karo.

## E. Top 10 Categories
1. Category → Rows.
2. Sales → Columns.
3. Category filter open karo.
4. Top tab → Top 10 by SUM(Sales).

## F. Different Levels of Detail
Customer Name / State / Category ke according Sales summarize karo.

## G. Advanced Cleaning
```tableau
TRIM(IFNULL([Category], "Unknown"))
```

---

# Practical 10: Data Preparation using Tableau Prep

## Objective
Tableau Prep mein data clean, transform aur flow create karna.

## A. Connect Data
Tableau Prep → Connect → Excel / CSV.

## B. Clean and Profile
1. Add Clean Step.
2. Missing values check karo.
3. Unwanted fields remove karo.
4. Data types correct karo.

## C. Group and Standardize
1. Field select karo.
2. Group Values.
3. Similar values combine karo.

## D. Merge Fields
Clean Step → Fields select karo → Merge Fields.

## E. Aggregation
1. Add Aggregate Step.
2. Grouped Fields select karo.
3. Aggregated Fields select karo.
4. SUM / AVG / COUNT apply karo.

## F. Filters and Transformations
Add Clean Step → Filter condition apply karo.

## G. Flow Automation
Input → Clean → Aggregate → Output.

Flow run karo aur output save karo.

---

# Practical 11: Advanced Visualization and Customization

## Objective
Advanced charts aur dashboard customizations create karna.

## A. Slope Chart
1. Year / Date → Columns.
2. Measure → Rows.
3. Do time periods select karo.
4. Line Chart create karo.

## B. Lollipop Chart
1. Bar Chart create karo.
2. Dual Axis use karo.
3. Circle Marks select karo.
4. Bar aur circle combine karo.

## C. Waterfall Chart
1. Category → Columns.
2. Sales / Profit → Rows.
3. Marks → Gantt Bar.
4. Running Total calculation apply karo.
5. Size mein measure use karo.

## D. Sparkline
1. Date → Columns.
2. Sales → Rows.
3. Line Chart create karo.
4. Small chart format karo.

## E. Sheet Swapping
1. Parameter create karo.
2. Calculated Field se selected sheet define karo.
3. Parameter ke according sheets display karo.

## F. Geographic Territories
Map create karo → Locations select karo → Create Group / Territory.

## G. Background Image
Map / Dashboard → Background Images → Add Image → Coordinates set karo.

---

# Practical 12: Sharing, Publishing and Presenting

## Objective
Dashboard export, publish aur share karna.

## A. Export PDF
File → Print to PDF / Export as PDF (version ke according).

## B. Presentation Mode
Toolbar → Presentation Mode.

## C. Publish to Tableau Public
1. File → Save to Tableau Public.
2. Account sign in karo.
3. Workbook name enter karo.
4. Save / Publish.

## D. Tableau Server / Online
Server → Publish Workbook → Sign in → Publish.

## E. User Interaction
Dashboard mein filters aur actions configure karo.

## F. Permissions
Published workbook ki permissions settings mein access control set karo.

## G. Evaluation
- Titles check karo.
- Filters test karo.
- Layout check karo.
- Screen size check karo.
- Dashboard properly display ho raha hai ya nahi verify karo.

---

# Practical 13: Retail Sales & Profitability Dashboard

## Objective
Region-wise Sales, Profit aur Discount ka impact analyze karna.

## A. Bar Chart
- Columns → Category
- Rows → SUM(Sales)

## B. Line Chart
- Columns → Order Date
- Rows → SUM(Sales)

## C. Map
- State → Map
- Sales → Color

## D. Profit Ratio Calculated Field
```tableau
SUM([Profit]) / SUM([Sales])
```

## E. Filters
Region → Show Filter.

Category → Show Filter.

## F. Interactive Dashboard
1. Bar Chart worksheet create karo.
2. Line Chart worksheet create karo.
3. Map worksheet create karo.
4. New Dashboard open karo.
5. Teeno worksheets drag karo.
6. Region aur Category filters add karo.
7. Use as Filter enable karo.
8. Dashboard title add karo.

---

# Practical 14: Customer Segmentation & Behavior Analysis

## Objective
Customers ko purchasing behavior ke according segment karna.

## A. Clustering
1. Scatter Plot create karo.
2. Sales → Columns.
3. Profit → Rows.
4. Analytics → Cluster drag karo.
5. Clusters analyze karo.

## B. RFM Analysis

**Recency:** Customer ne last purchase kab ki?

**Frequency:** Customer ne kitni baar purchase kiya?

**Monetary Value:** Customer ne total kitna spend kiya?

## C. Scatter Plot
Sales → Columns, Profit → Rows, Customer Name → Detail.

## D. Segmentation Dashboard
1. RFM fields prepare karo.
2. Scatter Plot create karo.
3. Clustering apply karo.
4. Customer segments show karo.
5. Dashboard create karo.

## E. High-Value Customers
1. Customer Name → Rows.
2. Sales → Columns.
3. Sort descending.
4. Top customers identify karo.

---

# Practical 15: Sales Forecasting and Trend Analysis

## Objective
Historical sales data se future sales predict karna.

## A. Time-Series Chart
1. Order Date → Columns.
2. Sales → Rows.
3. Date ko Month / Year select karo.
4. Line Chart create karo.

## B. Forecast
1. Analytics tab open karo.
2. Forecast ko chart par drag karo.
3. Future values observe karo.

## C. Seasonal Trends
Order Date ko Month / Quarter ke according analyze karo.

## D. Moving Average
```tableau
WINDOW_AVG(SUM([Sales]), -2, 0)
```

## E. Trend Analysis
Analytics → Trend Line drag karo.

## F. Compare Sales
Year → Columns, Sales → Rows.

## G. Final Dashboard
Time-Series Chart + Forecast + Moving Average ko ek Dashboard mein combine karo.

---

# 📌 Important Tableau Formulas

## 1. Profit Ratio
```tableau
SUM([Profit]) / SUM([Sales])
```

## 2. Sales Classification
```tableau
IF [Sales] >= 1000 THEN "High"
ELSE "Low"
END
```

## 3. Discount Classification
```tableau
IF [Discount] > 0.2 THEN "High Discount"
ELSE "Low Discount"
END
```

## 4. Null Values
```tableau
IFNULL([Category], "Unknown")
```

## 5. Remove Extra Spaces
```tableau
TRIM([Category])
```

## 6. Extract Year
```tableau
YEAR([Order Date])
```

## 7. Extract Month
```tableau
MONTH([Order Date])
```

## 8. Profit Status
```tableau
IF [Profit] > 0 THEN "Profit"
ELSEIF [Profit] < 0 THEN "Loss"
ELSE "No Profit"
END
```

## 9. Running Total
```tableau
RUNNING_SUM(SUM([Sales]))
```

## 10. Moving Average
```tableau
WINDOW_AVG(SUM([Sales]), -2, 0)
```

## 11. Ranking
```tableau
RANK(SUM([Sales]))
```

## 12. Window Sum
```tableau
WINDOW_SUM(SUM([Sales]))
```

---

# 🧠 Last-Minute Memory Tricks

## Tableau Workflow = C-D-M-A-S

- **C** – Connect Data
- **D** – Dimensions & Measures
- **M** – Make Charts
- **A** – Analyze Data
- **S** – Share Dashboard

## RFM = R-F-M

- **R** – Recency
- **F** – Frequency
- **M** – Monetary Value

## LOD = F-I-E

- **F** – FIXED
- **I** – INCLUDE
- **E** – EXCLUDE

## JOIN = I-L-R-F

- **I** – Inner
- **L** – Left
- **R** – Right
- **F** – Full Outer

---

# ⭐ Exam Strategy

Koi bhi practical aaye, sabse pehle:

1. Dataset connect karo.
2. Question mein required Dimension aur Measure identify karo.
3. Worksheet mein fields drag karo.
4. Required chart create karo.
5. Formatting, title aur labels add karo.
6. Agar dashboard poocha hai toh worksheets combine karo.
7. Save your work.

**Best of luck, bhai! ❤️ Tableau ke saare 15 practicals ki practice kar aur confidence ke saath exam de.**
## PROJECT TITLE
# 📊 Exploratory and Predictive Analysis of Founding Trends, Legal Structures, and Financial Stability in German FinTech

## 🔍 Project Objective

This project aims to analyze the German FinTech ecosystem using a combination of **exploratory data analysis**, **visual insight**, **business reasoning**, and **machine learning**. The goal is to uncover structural patterns and predict firm-level outcomes like inactivity and risk factors.

---

## 📁 Dataset Information

- **Source**: Kaggle  
- **File**: `German_FinTechCompanies.csv`

Features include:
- Founding year, City, Legal form
- Segment/Subsegment classification
- Bank Cooperation status
- Founder info
- Dates of Inactivity, Liquidation, Insolvency

---

## 🔎 1. Exploratory Data Analysis (EDA)

Basic statistical and categorical breakdowns were performed to understand the structure of the dataset.

### 📊 Visuals
- **Top Legal Forms**  
- **Top Cities**  
- **Founding Year Trend**  
- **Segment/Subsegment Distribution**  
- **Bank Cooperation**

Each of these plots helped us explore key structural properties of FinTech companies in Germany.


![alt text](<Screenshot 2025-07-29 121719.png>)
---

## 📈 2. Visual Analysis

Focused plotting was used to enhance interpretability.

- **Top 10 Cities by Number of Companies**  
- **Founding Trend Over Time**  
- **Legal Form Distribution (Pie)**  
- **Segment Heatmap by City**

📌 These revealed strong geographic and structural clustering patterns, especially in Berlin and Munich.

![alt text](<Screenshot 2025-07-29 122005.png>)  ![alt text](<Screenshot 2025-07-29 122051.png>)  ![alt text](<Screenshot 2025-07-29 122117.png>)  ![alt text](<Screenshot 2025-07-29 122141.png>)
---


## 💡 3. Business Insight

Strategic evaluation of lifecycle and founder-related patterns.

### Key Findings:

- 📉 **Lifespan**: Most companies close or become inactive within **3–7 years**
- 💰 **Insolvency/Liquidation**: Many firms show distress over time
- 👤 **Founder Influence**: Repeat founders exist, indicating serial entrepreneurship

> Top repeat founders were identified, offering potential for partnership targeting or ecosystem mapping.
 ![alt text](<Screenshot 2025-07-29 122215.png>)  ![alt text](<Screenshot 2025-07-29 122255.png>) ![alt text](<Screenshot 2025-07-29 122315.png>)
---

## 🤖 4. Advanced Modelling

This section applies **classification** and **clustering** models:

### 🧪 Random Forest – Predict Inactivity

#### 🧷 Target Variable:
- `Inactive` (based on presence of `Date of inactivity`)

#### 🧰 Features:
- Legal form, Founding year, Bank Cooperation

#### 📊 Results:
- Classification report and confusion matrix show moderate ability to predict which companies are inactive based on historical data.


---

### 🎯 KMeans Clustering – Company Typology

#### 🎯 Features used:
- Segment, City, Bank Cooperation

#### 🔍 Dimensionality Reduction:
- PCA used for visualization

![alt text](<Screenshot 2025-07-29 122359.png>)

This clustering revealed **four distinct groups** of companies based on service scope and urban concentration.

---

## 🛠️ Technologies Used

- Python (Pandas, Seaborn, Matplotlib, Sklearn)
- Data visualization
- Machine Learning (Random Forest, KMeans)
- Dimensionality Reduction (PCA)

---

## 📁 Running the Code

1. Clone the repo or open the Jupyter notebook
2. Make sure `German_FinTechCompanies.csv` is in the working directory
3. Run each cell/block from:
   - EDA
   - Visuals
   - Business Insight
   - Advanced Modelling

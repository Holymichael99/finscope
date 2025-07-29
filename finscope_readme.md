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

##  Exploratory Data Analysis (EDA)
The EDA section explores structural, geographical, and categorical distributions of the German FinTech ecosystem using visual insights.

 Overview Chart: German FinTech Companies Analysis
The figure below provides a multi-faceted overview of the dataset, combining key distributions and trends.


 Insights from the Chart:
Top 10 Legal Forms
The most common legal structure is GmbH, with over 600 companies registered under this form. Other structures like AG, UG, and Ltd. appear much less frequently, suggesting a strong preference for GmbH among German FinTechs due to its flexible and well-recognized corporate framework.

Top 10 Cities
The FinTech scene is heavily concentrated in Berlin, followed by München, Hamburg, and Frankfurt am Main. These urban centers likely offer stronger financial ecosystems, tech talent, and regulatory support.

Founding Year Trend
The founding trend shows a sharp increase in FinTech startups post-2010, peaking around 2017–2019. This surge aligns with broader global trends in digital finance and innovation post-2008 financial crisis.

Segment Distribution
The most represented segments are Other FinTechs, Financing, and Payments, indicating a diverse and growing market with companies branching beyond traditional banking or insurance.

Top 10 Subsectors
The leading subsectors include:

Technology, IT, and Infrastructure

Insurance

Alternative Payment Methods

Crowdinvesting

This points to a wide array of service innovations within the industry.

Bank Cooperation Status
The majority of FinTechs do not cooperate with traditional banks. This finding reflects a key FinTech ethos: offering independent, often disruptive services. However, a notable minority (~20%) still seek strategic alliances with banks.
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

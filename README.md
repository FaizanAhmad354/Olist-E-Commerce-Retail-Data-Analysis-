# 📊 Olist Brazilian E-Commerce Analytics & Customer Segmentation

An end-to-end business intelligence and data analytics project analyzing **100K+ Brazilian e-commerce orders** (2016–2018). This project examines platform growth, delivery bottlenecks, payment trends, and customer lifecycle dynamics using **SQL, Python, and Power BI**.

---

## 📸 Executive Dashboard
![Olist Executive Dashboard](assets/dashboard_overview.png)

---

## 🎯 Business Context & Problems
Olist connects regional small merchants across Brazil to central marketplaces. As order volume grew, operations faced key challenges:
1. **Logistics Bottlenecks:** Disproportionate fulfillment times across different geographical regions directly hurt customer ratings.
2. **Low Retention:** Over 97% of transactions originated from one-time shoppers, showing poor customer lifetime value.
3. **Financing Dependency:** Heavy customer reliance on split-payment financing (installments) across high-ticket categories.

---

## 🛠️ Tech Stack & Architecture
* **Data Storage & Querying:** SQLite, SQL (Window functions, CTEs, Joins)
* **Data Transformation & EDA:** Python (Pandas, NumPy)
* **Visualizations:** Power BI Desktop (DAX, Star Schema Modeling), Matplotlib
* **Environment:** Jupyter Notebook, VS Code, Git

---

## 🔍 Key Findings & Analytical Insights

* **The Retention Crisis:** 
  * Out of ~93K+ unique customers, **~97% ordered only once**, resulting in an overall repeat buyer rate of roughly **3%**.
  * Customer segmentation identified **~45K active/recent buyers**, while **~46K customers** sit in the "At Risk" or "Lost" segments.

* **Logistics Disparity & Rating Impact:**
  * **On-time deliveries** maintained an average customer review rating of **4.29 / 5.0**.
  * **Delayed deliveries** saw review scores drop sharply to **2.57 / 5.0**.
  * Orders in the primary hub (**São Paulo - SP**) averaged **~8.8 days** for delivery, whereas remote northern states (**RR, AP, AM**) took **26 to 29 days**.

* **Payment Dynamics:**
  * **Credit cards** drove **~78%** of total revenue.
  * Cardholders opted for an average of **3.5 installments**, demonstrating strong demand for short-term financing on non-essential purchases.

---

## 💡 Strategic Recommendations

1. **Retention Workflows:** Deploy automated post-delivery engagement (targeted loyalty discounts within 21–30 days) to prevent recent one-time buyers from churning.
2. **Regional Fulfillment Hubs:** Partner with 3PL micro-fulfillment centers in northern regions to cut delivery times down from ~28 days to under 14 days.
3. **Zero-Interest Installment Partnerships:** Work with financial partners to offer 3–6 month interest-free options on high-value categories (`watches_gifts`, `computers_accessories`) to lift average order value.

---

## 📂 Project Repository Structure
```text
├── assets/
│   └── dashboard_overview.png     # Power BI report preview
├── data/
│   ├── raw/olist_datasets         # Original Olist dataset CSVs
│   └── olist_dashboard_data.csv   # Aggregated data for dashboard
├── notebooks/
│   └── 01_exploration.ipynb       # SQL pipeline, EDA, and RFM calculations
├── olist.db                       # Relational database file
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation
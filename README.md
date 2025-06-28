## Language
- [English](README.md)
- [中文](README_zh.md)

---
# Proactive Backorder Prediction for Supply Chain Optimization

### A Machine Learning Model to Identify At-Risk Products *Before* They Go Out of Stock

This project builds and evaluates a binary classification model to solve a critical supply chain problem: **predicting product backorders**. By identifying which items are at high risk of going out of stock, businesses can move from a *reactive* (fire-fighting) to a *proactive* (preventive) inventory management strategy.

This model is designed to be used by a logistics or supply chain manager to generate a daily "at-risk" report, allowing them to take preventive action and optimize the flow of goods.

## 🚀 The Business Problem

In any supply chain, a product backorder is a major failure. It represents an order for an item that is currently out of stock. This leads to:

* **Lost Revenue:** The customer may cancel the order and buy from a competitor.
* **Poor Customer Satisfaction:** Leads to customer churn and damages brand reputation.
* **Increased Operational Costs:** Expedited shipping and manual interventions are expensive.

The goal is not just to forecast *demand*, but to predict the *risk of failure* in meeting that demand.

## 📊 Business Value

This model provides concrete, actionable insights for an operations team to:

* **Prevent Lost Sales:** Proactively identify the top 5% of products at high risk of backordering and expedite their inbound shipments.
* **Optimize Inventory Capital:** Avoid wasting capital on overstocking "safe" products and re-allocate it to buffer "at-risk" items.
* **Increase Customer Satisfaction:** Drastically reduce the number of "out of stock" notices and fulfillment delays, improving customer loyalty.
* **Drive Proactive Operations:** Give a supply chain manager a data-driven "warning list" instead of forcing them to react to problems as they happen.

## 💾 The Dataset

This project uses the **"Kaggle: Predict Material Backorders"** dataset. It is a large, real-world, and highly imbalanced dataset from a parts manufacturer.

* **Source:** [Kaggle: Back Order Prediction Dataset](https://www.kaggle.com/datasets/gowthammiryala/back-order-prediction-dataset)
* **Size:** ~1.69 million training observations
* **Features:** 22 features, including:
    * `national_inv`: Current inventory level
    * `lead_time`: Time from order to delivery
    * `sales_1_month`, `sales_3_month`, etc.: Historical sales figures
    * `forecast_3_month`, `forecast_6_month`, etc.: Internal demand forecasts
    * `went_on_backorder`: The target variable (Yes/No)
* **Core Challenge:** The dataset is **extremely imbalanced**. Fewer than 1.7% of all items went on backorder. This makes "accuracy" a useless metric and requires a specialized approach to modeling and evaluation.

## 🛠️ Tech Stack

* **Programming:** Python 3.10+
* **Data Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn, XGBoost
* **Imbalance Handling:** `imblearn` (for SMOTE)
* **Environment:** Jupyter Notebooks, VS Code

## 📈 Analysis & Modeling Workflow

1.  **Data Cleaning & EDA:**
    * Loaded the 1.69M-row dataset (`Training_BOP.csv`) and handled missing values.
    * Performed exploratory analysis to understand key features.

2.  **Feature Engineering:**
    * Added new features like `inventory_to_sales_ratio`, `forecast_error`.
    * Encoded categorical variables using one-hot encoding.

3.  **Imbalance Handling:**
    * **Baseline:** Raw data.
    * **SMOTE:** Oversampling.
    * **Class Weighting:** Penalize rare misclassification.

4.  **Modeling & Evaluation:**
    * Trained Logistic Regression, RandomForest, XGBoost.
    * Evaluated using Precision, Recall, F1-score, and PR-AUC.

## 💡 Key Results & Recommendations

The model successfully identifies 41% of all actual backorders (Recall = 0.41) on the unseen test data. While this means some backorders are still missed, it provides supply chain planners with a powerful early warning system for a large portion of potential stockouts.

Threshold Optimization is Crucial: The model's default 0.5 probability threshold yields the 41% recall. However, this can be adjusted to meet specific business needs:

- For Higher Detection (Aggressive Strategy): Lowering the threshold to 0.1 increases the detection rate to 64% of all backorders, allowing planners to be more proactive at the cost of more false alarms (Precision drops to 8%).
- For Higher Confidence (Conservative Strategy): Increasing the threshold to 0.8 improves the alert quality, with 22% of alerts being correct backorders, though this only captures 25% of total backorders.

Key Predictive Drivers: The most important features driving backorder predictions are:
- 6-Month Sales Forecast (forecast_6_month)
- Current Inventory Level (national_inv)
- 3-Month Sales Forecast (forecast_3_month)

### **Business Actions**

Implement a Prioritized Watchlist: Use the model's probability scores to create a daily or weekly "Backorder Risk" watchlist for supply chain planners. Items with the highest predicted probability should be investigated first.

Action: Start with a threshold of 0.5. This provides a good balance and correctly identifies 1,107 potential backorder events in the test set that can be proactively managed.

Focus on Key Drivers: Since forecasts and inventory are the top predictors, create specific alerts for items where the forecast_6_month is high but the national_inv is low. This simple heuristic, informed by the model, can serve as a quick, secondary check.

Optimize Inventory Strategy Based on Recall Needs:

For critical, high-cost-of-failure parts, use a low threshold (e.g., 0.2). It's better to carry extra inventory for a few non-critical items than to have a production line stop.

For less critical, low-cost parts, use a higher threshold (e.g., 0.7) to reduce the noise from false positives and focus planners' attention.

Feedback Loop for Continuous Improvement: Track the model's predictions against actual outcomes. Use this data to periodically retrain the model and refine the classification threshold based on the real-world cost of false positives (unneeded inventory) versus false negatives (missed backorders).

## 📁 Project Structure

```
product-backorder-prediction/
├── data/
│   ├── Training_BOP.csv
│   └── Testing_BOP.csv
├── notebooks/
│   ├── 01_EDA_and_Data_Cleaning.ipynb
│   ├── 02_Feature_Engineering_and_Modeling.ipynb
│   └── 03_Model_Evaluation_and_Interpretation.ipynb
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── models/
│   │   └── backorder_model_xgb.pkl
│   └── images/
│       ├── imbalance_plot.png
│       ├── pr_curve.png
│       └── feature_importance.png
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔌 Setup & How to Run

1. **Clone the Repo:**
    ```bash
    git clone https://github.com/your-username/product-backorder-prediction.git
    cd product-backorder-prediction
    ```
2. **Create Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # .\venv\Scripts\activate  # Windows
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Download Dataset:**
    * From [Kaggle](https://www.kaggle.com/datasets/gowthammiryala/back-order-prediction-dataset)
5. **Run Notebooks:**
    ```bash
    jupyter notebook
    ```

## 🚀 Future Improvements

* **Hyperparameter Tuning:** Use Optuna or Hyperopt.  
* **Cost-based Evaluation:** Add cost sensitivity.  
* **Deployment:** Streamlit dashboard for real-time use.

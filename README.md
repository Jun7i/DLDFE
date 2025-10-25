## Language
- [English](README.md)
- [中文](README_zh.md)

---

# Dynamic Demand Forecasting for E-commerce

### A "Niche Retailer" Model for Outdoor & Adventure Gear

This project builds a complete system to forecast product demand for a niche e-commerce retailer (e.g., "Outdoor & Adventure Gear"). It ingests data from multiple external sources—such as public news, weather forecasts, and social media trends—to create a predictive model that helps a business optimize its supply chain.

## Business Value

For a specialized retailer (like REI or a local outdoor shop), this model provides concrete, actionable insights to:

  * **Prevent Stockouts:** Identify a spike in social media `#hiking` posts and a sunny weather forecast to proactively increase stock of "hiking boots" and "daypacks" in that region.
  * **Reduce Overstocking:** Avoid ordering excess "skis" and "snowboards" if news sentiment and weather models predict a warm, low-snow winter.
  * **Optimize Logistics:** Reroute shipments to warehouses in regions where demand is predicted to spike, *before* the demand actually hits.
  * **Target Marketing:** Launch ad campaigns for "rain jackets" in the Pacific Northwest when a 5-day rainy forecast is detected.

## Tech Stack

  * **Programming:** Python 3.10+
  * **Data Processing:** Pandas
  * **Machine Learning:** XGBoost (or LightGBM), Scikit-learn
  * **NLP:** VADER (for fast sentiment analysis)
  * **APIs:** OpenWeatherMap, NewsAPI.org, Twitter API v2
  * **Dashboard:** Streamlit (or Tableau)
  * **Environment:** Jupyter Notebooks (for exploration), VS Code (for scripting)

## Data Pipeline & Architecture

This project runs as a daily batch process, which is managed by a single Python script.

1.  **Data Acquisition:** A Python script (`src/data_pipeline.py`) runs once per day.
      * It fetches 5-day weather forecasts from **OpenWeatherMap** for key regions (e.g., "Denver, CO", "Seattle, WA").
      * It fetches relevant news articles from **NewsAPI** using queries like `q="hiking" OR "camping" OR "ski season"`.
      * It fetches recent tweets from the **Twitter API** using queries like `#hiking OR #camping OR "new gear"`.
      * It loads the static, historical sales data (`data/raw/mock_sales.csv`).

2.  **Data Processing & NLP:**
      * **News:** News article descriptions are run through VADER to get a daily average `news_sentiment_score`.
      * **Twitter:** Tweet text is run through VADER to get a daily average `twitter_sentiment_score`.
      * **Weather:** Forecasts are flattened into features like `day_3_forecast_temp` and `day_3_forecast_is_rain`.
      * **Sales:** Historical sales data is aggregated by `date`, `region`, and `product_category`.

3.  **Feature Engineering & Merging:**
      * All data sources are merged into a single "master" dataset.
      * **Lag Features** are created (e.g., `units_sold_7_days_ago`).
      * **Forecast Features** are created (e.g., `weather_forecast_3_days_from_now`).
      * The final, clean dataset is saved to `data/processed/final_features.csv`.

4.  **Modeling:**
      * An XGBoost model is trained on `final_features.csv` to predict a future value (e.g., `units_sold_in_7_days`).
      * The trained model is saved to `models/demand_model.pkl`.

5.  **Dashboard:**
      * A Streamlit app (`src/dashboard.py`) loads the *latest* processed data and the *trained model*.
      * It generates new predictions and displays them on an interactive dashboard for a "Logistics Manager."

## Project Structure

```
dynamic-demand-forecasting/
├── data/
│   ├── raw/
│   │   ├── mock_sales.csv
│   │   ├── news_data_2025-10-25.json
│   │   ├── weather_data_2025-10-25.json
│   │   └── twitter_data_2025-10-25.json
│   ├── processed/
│   │   └── final_features.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│
├── src/
│   ├── __init__.py
│   ├── api_utils.py
│   ├── data_pipeline.py
│   ├── ml_pipeline.py
│   └── dashboard.py
│
├── models/
│   └── demand_model.pkl
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup & Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/dynamic-demand-forecasting.git
    cd dynamic-demand-forecasting
    ```

2.  **Create a Python Virtual Environment:**

    ```bash
    python -m venv venv
    ```

      * On macOS/Linux: `source venv/bin/activate`
      * On Windows: `.env\Scriptsctivate`

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up API Keys:**

      * Sign up for accounts at [NewsAPI.org](https://newsapi.org/), [OpenWeatherMap](https://openweathermap.org/api), and the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).
      * Copy the example `.env` file:
        ```bash
        cp .env.example .env
        ```
      * Open `.env` and add your secret API keys:
        ```plaintext
        NEWS_API_KEY="YOUR_KEY_HERE"
        OPENWEATHER_API_KEY="YOUR_KEY_HERE"
        TWITTER_BEARER_TOKEN="YOUR_TOKEN_HERE"
        ```

5.  **Add Mock Sales Data:**

      * Prepare a CSV dataset with columns like `date`, `region`, `product_category`, and `units_sold`.
      * Save it as `data/raw/mock_sales.csv`.

## How to Run

1.  **Run Data Pipeline:**
    ```bash
    python src/data_pipeline.py
    ```

2.  **Explore and Train Model:**
    ```bash
    jupyter notebook
    ```

3.  **Train Final Model:**
    ```bash
    python src/ml_pipeline.py
    ```

4.  **Launch Dashboard:**
    ```bash
    streamlit run src/dashboard.py
    ```

## Future Improvements

  * **Better NLP:** Use a pre-trained transformer model like `distilBERT`.
  * **More Data:** Add Google Trends or holiday data.
  * **Orchestration:** Automate with Apache Airflow or Mage.
  * **Deployment:** Host dashboard on Streamlit Cloud.

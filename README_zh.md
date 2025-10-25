## 语言
- [English](README.md)
- [中文](README_zh.md)

---

# 电商动态需求预测系统

### 户外与探险装备的“细分零售商”预测模型

这个项目构建了一个完整的系统，用来预测电商中某一细分领域（例如“户外和探险装备”）的产品需求。系统会从多个外部来源获取数据——包括新闻、天气预报和社交媒体趋势——并构建预测模型，帮助企业优化供应链。

## 商业价值

对于像 REI 或本地户外用品店这样的专业零售商，这个模型可以带来以下实际价值：

  * **防止断货：** 当社交媒体上出现大量 `#hiking`（徒步）帖文并且天气预报晴朗时，系统会提前建议增加该地区“登山鞋”和“背包”的库存。
  * **减少库存积压：** 如果新闻和天气模型预测冬季偏暖、少雪，系统会建议减少“滑雪板”等冬季商品的订货量。
  * **优化物流：** 当某地区预计需求上升时，提前将货物调配到该区域的仓库。
  * **精准营销：** 如果太平洋西北地区预计连续多天下雨，系统会自动建议投放“雨衣”广告。

## 技术栈

  * **编程语言：** Python 3.10+
  * **数据处理：** Pandas
  * **机器学习：** XGBoost（或 LightGBM）、Scikit-learn
  * **文本情感分析：** VADER
  * **数据接口：** OpenWeatherMap、NewsAPI.org、Twitter API v2
  * **可视化仪表盘：** Streamlit（或 Tableau）
  * **开发环境：** Jupyter Notebook（用于探索）、VS Code（用于脚本开发）

## 数据管道与架构

整个项目以每天自动运行的批处理任务形式执行，由一个主 Python 脚本统一管理。

1.  **数据获取：**
    * 每天运行一次 `src/data_pipeline.py`。
    * 从 **OpenWeatherMap** 获取主要城市（如 Denver, Seattle）的 5 天天气预报。
    * 从 **NewsAPI** 获取新闻数据，查询关键词如 `"hiking" OR "camping" OR "ski season"`。
    * 从 **Twitter API** 获取推文数据，查询如 `#hiking OR #camping OR "new gear"`。
    * 加载本地的销售历史数据文件 `data/raw/mock_sales.csv`。

2.  **数据处理与情感分析：**
    * 新闻：使用 VADER 分析文章摘要，生成每日平均 `news_sentiment_score`。
    * 推特：分析推文文本，生成每日平均 `twitter_sentiment_score`。
    * 天气：将预报展开为结构化特征，例如 `day_3_forecast_temp`、`day_3_forecast_is_rain`。
    * 销售：按 `date`、`region` 和 `product_category` 聚合销售数据。

3.  **特征工程与合并：**
    * 将所有数据源合并为一个“主数据集”。
    * 生成 **滞后特征**（如 `units_sold_7_days_ago`）。
    * 生成 **预测特征**（如 `weather_forecast_3_days_from_now`）。
    * 最终保存为 `data/processed/final_features.csv`。

4.  **建模：**
    * 使用 XGBoost 训练模型来预测未来销量（如 `units_sold_in_7_days`）。
    * 模型保存为 `models/demand_model.pkl`。

5.  **仪表盘：**
    * Streamlit 应用 `src/dashboard.py` 会加载最新数据和训练好的模型。
    * 生成预测结果并展示给物流或库存经理查看。

## 项目结构

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

## 安装与配置步骤

1. **克隆仓库：**
    ```bash
    git clone https://github.com/your-username/dynamic-demand-forecasting.git
    cd dynamic-demand-forecasting
    ```

2. **创建虚拟环境：**
    ```bash
    python -m venv venv
    ```
    * macOS/Linux：`source venv/bin/activate`
    * Windows：`.env\Scriptsctivate`

3. **安装依赖包：**
    ```bash
    pip install -r requirements.txt
    ```

4. **配置 API 密钥：**
    * 前往 [NewsAPI.org](https://newsapi.org/)、[OpenWeatherMap](https://openweathermap.org/api)、[Twitter 开发者平台](https://developer.twitter.com/en/portal/dashboard) 注册账户。
    * 复制 `.env` 模板文件：
      ```bash
      cp .env.example .env
      ```
    * 编辑 `.env` 文件，添加你的密钥：
      ```plaintext
      NEWS_API_KEY="YOUR_KEY_HERE"
      OPENWEATHER_API_KEY="YOUR_KEY_HERE"
      TWITTER_BEARER_TOKEN="YOUR_TOKEN_HERE"
      ```

5. **添加销售数据：**
    * 准备一个包含 `date`、`region`、`product_category`、`units_sold` 的 CSV 文件。
    * 保存为 `data/raw/mock_sales.csv`。

## 运行项目

1. **运行数据管道：**
    ```bash
    python src/data_pipeline.py
    ```

2. **探索与训练模型：**
    ```bash
    jupyter notebook
    ```

3. **训练最终模型：**
    ```bash
    python src/ml_pipeline.py
    ```

4. **启动仪表盘：**
    ```bash
    streamlit run src/dashboard.py
    ```

## 后续改进方向

  * **更好的 NLP：** 可用 `distilBERT` 等预训练模型替代 VADER。
  * **更多数据源：** 可加入 Google Trends 或节假日数据。
  * **任务调度：** 使用 Apache Airflow 或 Mage 做定时调度。
  * **部署：** 可将 Streamlit 仪表盘免费部署到 Streamlit Cloud。

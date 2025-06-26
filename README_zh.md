## 语言
- [English](README.md)
- [中文](README_zh.md)

---
# 供应链优化中的主动缺货预测

### 用机器学习模型提前识别“高风险”产品，防止断货

这个项目利用机器学习模型预测哪些产品最容易缺货（Backorder）。  
通过提前识别高风险产品，企业可以从“被动反应”转变为“主动预防”，让库存管理更智能高效。

模型可以帮助供应链或物流经理生成每日“高风险产品报告”，提前采取措施。

## 🚀 商业问题

在供应链中，缺货是一个严重的运营问题：

* **收入损失：** 客户可能取消订单并转向竞争对手。  
* **客户满意度下降：** 导致客户流失、品牌受损。  
* **运营成本上升：** 紧急发货和人工干预增加成本。  

目标不仅是预测需求，而是预测**供应失败的风险**。

## 📊 商业价值

该模型可以帮助：

* **防止销售损失：** 提前发现高风险产品并加快补货。  
* **优化库存：** 减少过量备货，把资金集中在关键产品上。  
* **提升客户体验：** 减少“缺货”通知和发货延迟。  
* **主动管理：** 从“救火”式反应转为提前预警。  

## 💾 数据集

项目使用 **Kaggle: Predict Material Backorders** 数据集（真实制造业数据，约 169 万条记录）。  

* **来源：** [Kaggle 数据集](https://www.kaggle.com/datasets/gowthammiryala/back-order-prediction-dataset)  
* **主要特征：**
  * `national_inv`：当前库存量  
  * `lead_time`：交付时间  
  * `sales_1_month`、`forecast_3_month`：销售与预测数据  
  * `went_on_backorder`：是否缺货（目标变量）  
* **挑战：** 数据极度不平衡，因此不能只看“准确率”，需关注 Precision、Recall、F1-score 等指标。

## 🛠️ 技术栈

* Python 3.10+  
* Pandas, NumPy  
* Matplotlib, Seaborn  
* Scikit-learn, XGBoost  
* imbalanced-learn（SMOTE）  
* Jupyter Notebook, VS Code  

## 📈 分析与建模流程

1. **数据清洗与探索：**
   * 加载 169 万条数据并处理缺失值。  
   * 观察库存、交期、销量分布。  


2. **特征工程：**
   * 构造 `inventory_to_sales_ratio`、`forecast_error` 等新特征。  
   * 对分类变量进行 One-Hot 编码。  

3. **样本不平衡处理：**
   * **原始数据训练（Baseline）**
   * **SMOTE 过采样**
   * **调整类别权重（XGBoost `scale_pos_weight`）**  

4. **建模与评估：**
   * 使用 Logistic Regression、RandomForest、XGBoost。  
   * 重点看 Precision、Recall、F1、PR-AUC。  

## 💡 结果与建议



### **业务建议**

1. 每日生成“高风险产品”清单。  
2. 重新评估安全库存策略。  
3. 改进需求预测与供应管理。  

## 📁 项目结构

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

## 🔌 安装与运行

1. **克隆项目：**
   ```bash
   git clone https://github.com/your-username/product-backorder-prediction.git
   cd product-backorder-prediction
   ```
2. **创建虚拟环境：**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate  # Windows
   ```
3. **安装依赖：**
   ```bash
   pip install -r requirements.txt
   ```
4. **下载数据：**
   从 [Kaggle](https://www.kaggle.com/datasets/gowthammiryala/back-order-prediction-dataset) 下载后放入 `data/` 文件夹。  
5. **运行 Notebook：**
   ```bash
   jupyter notebook
   ```

## 🚀 后续改进

* 使用 Optuna/Hyperopt 进行参数调优。  
* 加入成本因素的模型评估方法。  
* 构建 Streamlit 仪表盘，实现实时预测。

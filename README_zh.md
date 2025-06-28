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
该模型在未见过的测试数据上成功识别出41%的实际缺货订单（召回率=0.41）。虽然这意味着仍有部分缺货订单未能被识别，但它为供应链规划人员提供了一个强大的早期预警系统，可覆盖大量潜在缺货情况。

阈值优化至关重要：模型默认0.5概率阈值可实现41%的召回率。但该阈值可根据具体业务需求调整：

- 高检测率策略（激进型）：将阈值降至0.1可将检测率提升至64%，使规划人员能更主动应对，但代价是误报率上升（精确度降至8%）。
- 追求更高置信度（保守策略）：将阈值提高至0.8可提升警报质量，其中22%的警报为真实缺货订单，但仅覆盖总缺货量的25%。

关键预测驱动因素：影响缺货预测的核心特征包括：
- 6个月销售预测（forecast_6_month）
- 当前库存水平（national_inv）
- 3个月销售预测（forecast_3_month）


### **业务建议**

实施优先级监控清单：利用模型的概率评分，为供应链规划人员创建每日或每周的“缺货风险”监控清单。应优先调查预测概率最高的品类。

操作建议：初始阈值设定为0.5。该阈值能实现良好平衡，并在测试集中准确识别出1,107个可主动管理的潜在缺货事件。

聚焦关键驱动因素：鉴于预测值与库存量是首要预测指标，针对预测值较高但全国库存量较低的品类设置专项预警。该基于模型启发的简单启发式方法可作为快速二次核查手段。

基于召回需求优化库存策略：

对于关键性、高故障成本的零件，采用低阈值（如0.2）。与其让生产线停工，不如为少量非关键物品多备库存。

对于非关键低成本零件，采用较高阈值（如0.7）以降低误报干扰，使规划人员能集中精力处理关键事项。

持续改进的反馈循环：追踪模型预测与实际结果的偏差。利用该数据定期重新训练模型，并根据误报（冗余库存）与漏报（缺货订单）的实际成本差异，动态调整分类阈值。

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

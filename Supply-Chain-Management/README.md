# Supply Chain Management Analytics Project  
Streamlit Dashboard: [http://localhost:8501/]

## Overview
This project demonstrates an end-to-end **supply chain analytics workflow**, covering:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Demand prediction modeling
- Explainability
- Interactive business dashboard (Streamlit)

The focus is on translating data into **operational insights**, not overfitting models on limited data.

---

## Project Structure
```
Supply-Chain-Management/
│
├── data/
│   └── supply_chain_data.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modeling.ipynb
│
├── src/
│   ├── 01_preprocessing.py
│   └── 02_feature_engineering.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Dataset
- 100 records, 24 features
- Mix of numeric and categorical supply chain attributes
- Includes demand, inventory, cost, logistics, and quality indicators

⚠️ The dataset is cross-sectional (non-time-series).

---

## Exploratory Data Analysis (EDA)
The EDA identifies:
- Revenue concentration risks by product type
- Demand variability across categories
- Lead time and defect rate volatility
- Inventory efficiency using turnover & DSI
- Weak correlation between cost and revenue

**Key Insight:**  
Demand is driven more by **availability and logistics reliability** than manufacturing cost.

---

## Feature Engineering
Custom features include:
- Inventory Pressure Index
- Supply Risk Index
- Cost per Unit
- Logistics Delay Index
- Inventory Turnover
- Revenue per Unit

These features align directly with business KPIs.

---

## Modeling Approach
- Target variable: `Number of products sold`
- Model: Random Forest Regressor
- Train/Test split: 80/20
- Evaluation metrics: MAE, RMSE, R²

### Why Random Forest?
- Handles non-linear relationships
- Robust on small datasets
- Provides built-in feature importance

---

## Preprocessing
Preprocessing is used **only for modeling**, not visualization:
- Missing value handling
- Label encoding for categorical features
- Feature scaling using StandardScaler

This separation ensures clean analytics and reproducible ML pipelines.

---

## Explainability
- Feature importance analysis
- SHAP values (local & global explanations)

Top drivers:
- Inventory pressure
- Stock availability
- Supply risk indicators

---

## Streamlit Dashboard
The Streamlit app converts insights into an interactive decision tool:
- Revenue & demand analysis
- Inventory risk visualization
- Demand driver explanation
- Business recommendations

The app loads data directly from the repository, requiring no local setup.

---

## Limitations
- Small sample size
- No temporal data
- Synthetic dataset

Results are illustrative and intended for learning and demonstration.

---

## Future Improvements
- Add time-series demand data
- Implement rolling forecasts
- Integrate real supplier performance metrics
- Connect to live databases or APIs

---

## Conclusion
This project prioritizes **business relevance and interpretability** over model complexity, demonstrating how analytics supports real-world supply chain decisions.

# 🛒 Supermart360: Retail Profit Analytics & Predictive Modeling

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **Project Focus:** End-to-end retail analytics combining Exploratory Data Analysis (EDA) and Machine Learning to understand profit drivers and evaluate the feasibility of profit prediction in a grocery retail setting.

---

## Project Overview

**Supermart360** is a portfolio data science project built on grocery retail transaction data.
The objective is **not to inflate predictive performance**, but to demonstrate a **realistic ML workflow** that includes:

* Business-driven EDA
* Thoughtful feature engineering
* Model selection and validation
* Transparent discussion of data and modeling limitations

This project reflects how real-world data science problems are approached when data constraints exist.

---

##  Business Problem Statement

Retail grocery chains frequently ask:

* What factors truly drive profit at the transaction level?
* Can profit be reliably predicted using available sales and discount data?
* Where do pricing and discount strategies have diminishing returns?

This project answers these questions through analysis and modeling rather than assumptions.

---

##  Dataset Summary

* **Rows:** 9,994 transactions
* **Time Period:** 2015–2018
* **Geography:** Tamil Nadu, India
* **Data Source:** Synthetic dataset from an online internship program (practice-oriented)

>  The dataset does **not** contain cost, supplier, or procurement information, which directly impacts achievable model performance.

---

## 🔍 Exploratory Data Analysis (EDA)

### Key Findings

* **No Negative Profit Transactions**
  Indicates controlled pricing and discount rules; no loss-leading orders.

* **Uniform Sales Range (₹500–₹2,500)**
  Suggests stable demand without extreme price sensitivity.

* **Tiered Discount Structure**
  Discounts occur at fixed levels (10%, 15%, 20%, etc.), indicating rule-based discounting rather than dynamic pricing.

* **Regional Performance Differences**
  Cities such as *Kanyakumari* and *Virudhunagar* consistently show lower profit per order.

* **Category Profit Drivers**
  *Health Drinks* and *Soft Drinks* contribute disproportionately to overall profit.

* **Seasonality**
  Profit peaks observed in November, aligning with festive demand cycles.

### EDA-Driven Business Insights

* High-profit categories benefit more from volume expansion than aggressive discounting
* Low-margin cities require basket-size or volume strategies rather than price cuts
* Discount effectiveness is bounded due to rigid discount tiers

---

##  Data Preparation & Feature Engineering

* Robust date parsing for mixed formats using `pd.to_datetime(format="mixed")`
* Temporal features: Year, Month, Day, Day of Week
* One-Hot Encoding for:

  * Category
  * Sub-Category
  * City
  * Region
* StandardScaler applied **only to Sales** to control magnitude dominance
* Pipeline-based preprocessing to prevent data leakage

---

##  Machine Learning Objective

**Task:** Predict transaction-level **Profit**
**Type:** Regression

The goal was to test **whether profit is meaningfully predictable** using the available transactional features.

---

## Model Development

### Baseline Model

* **Algorithm:** Random Forest Regressor
* **Rationale:**

  * Handles non-linear effects
  * Works well with mixed numerical and categorical data
  * Interpretable via feature importance

**Baseline Performance (Test Set):**

* **R²:** ~0.33
* **MAE:** ~160
* **RMSE:** ~199

---

### Hyperparameter Tuning

* Implemented **RandomizedSearchCV**
* Tuned:

  * `n_estimators`
  * `max_depth`
  * `min_samples_split`
  * `max_features`
* Used pipelines and cross-validation to ensure fair comparison

**Result:**
Hyperparameter tuning **did not improve performance**.
The tuned model slightly underperformed the baseline.

---

### Target Transformation Experiment

* Attempted to predict **Profit Margin** instead of Profit
* Resulted in **R² ≈ 0**
* Conclusion: Margin is governed by cost and pricing policies not present in the data

---

##  Final Model Selection

The **baseline Random Forest Regressor** was selected as the final model.

### Justification

* Baseline model generalized better than tuned variants
* Feature importance showed strong dominance of Sales
* Performance ceiling driven by **feature expressiveness**, not algorithm choice
* Dataset is synthetic and formula-driven, limiting achievable R²

> **Key Insight:** When tuning and target reframing fail, the limitation lies in the data, not the model.

---

##  Model Interpretation

### Technical Interpretation

* Profit is primarily explained by **Sales volume**
* Discounts and temporal features add limited incremental signal
* Categorical effects (region, category) exist but are secondary

### Business Interpretation

* Increasing volume has a larger impact on profit than fine-grained discount tuning
* Discount strategies are constrained by rigid tiering
* Data supports **policy-level analysis**, not granular profit optimization

---

##  Project Limitations

* Synthetic training dataset
* No cost, supplier, or procurement features
* Profit closely tied to Sales by construction

These limitations were **explicitly documented** and not masked through overfitting.

---

##  Final Conclusion

This project demonstrates a **disciplined and realistic data science workflow**:

* Business-first EDA
* Careful model validation
* Rejection of unnecessary complexity
* Transparent acknowledgment of data constraints

Rather than optimizing for metrics alone, the project emphasizes **decision quality, explainability, and professional judgment**.

---

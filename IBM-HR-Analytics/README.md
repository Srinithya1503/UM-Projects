#  Employee Attrition Analytics

##  Project Overview

Employee attrition is a critical challenge for organizations, impacting productivity, morale, and long-term costs. This project delivers an **end-to-end HR analytics solution** to:

* Understand **who is leaving**
* Diagnose **why they are leaving**
* Provide **actionable insights** for HR policy and retention strategies

The project follows a complete analytics lifecycle:

> **Exploratory Data Analysis → Explainable Machine Learning → Executive Dashboarding**

---

##  Business Objectives

1. **Understand Current Turnover Rates**

   * Analyze overall attrition levels
   * Study demographic and organizational distribution by:

     * Age, Gender
     * Education
     * Department and Job Role

2. **Identify Key Drivers of Attrition**

   * Engagement & sentiment factors
     *(Job Involvement, Job Satisfaction, Work-Life Balance)*
   * Compensation & growth factors
     *(Monthly Income, Salary Hike, Promotion Lag)*
   * Work strain & policy factors
     *(OverTime, Business Travel, Manager Stability)*

3. **Enable Actionable Decision-Making**

   * Translate insights into **HR interventions**
   * Design dashboards that reduce **report fatigue**
   * Support early-warning retention strategies

---

##  Dataset

* **Source**: IBM HR Analytics – Employee Attrition & Performance
* **Records**: 1,470 employees
* **Target Variable**: `Attrition` (Yes / No)

---

##  1. Exploratory Data Analysis (EDA)

### Key EDA Design Principles

* Avoid redundant visuals and over-plotting
* Use **reusable helper functions** to ensure consistency
* Preserve **semantic meaning** of ordinal variables
* Focus on **attrition rates**, not just counts

### Variable Handling

*  Removed identifiers and constants:

  * EmployeeNumber, Over18, StandardHours, EmployeeCount
*  Numerical variables analyzed via common helper functions:

  * Age, MonthlyIncome, YearsAtCompany, YearsSinceLastPromotion, etc.
*  Ordinal variables mapped to meaningful labels:

  * *Low → Very High*, *Bad → Best*
*  Organizational variables visualized using **Sunburst charts**

### Key EDA Insights

* Attrition is higher among **younger employees** and those with **shorter tenure**
* Low **job involvement**, **job satisfaction**, and **work-life balance** strongly correlate with attrition
* Compensation acts as a **stabilizer**, not a primary trigger
* **Promotion stagnation** emerges as a major risk factor
* Overtime and frequent travel consistently increase attrition risk

---

##  2. Machine Learning & Explainability

### Problem Framing

* Binary classification problem
* Class imbalance (~16% attrition)
* Focus on **interpretability first**, performance second

### Models Used

1. **Logistic Regression**

   * Baseline, explainable model
   * Balanced class weights
   * Odds Ratios used for HR-friendly interpretation

2. **XGBoost**

   * Captures non-linear interactions
   * Used for performance validation
   * Class imbalance handled via scale_pos_weight

### Model Evaluation

* Metrics prioritized:

  * **Recall (Attrition = Yes)** → catching at-risk employees
  * **ROC-AUC** → ranking quality
* Achieved strong recall with acceptable trade-offs in precision

---

##  SHAP Analysis (Model Transparency)

SHAP was used to validate and explain model behavior.

### Consistent Top Drivers Across Models

* OverTime (Yes)
* Low Monthly Income
* Low Job Involvement
* Poor Work-Life Balance
* Long time since last promotion
* Low job satisfaction
* Frequent business travel
* Short tenure with current manager

### Key Validation Outcome

EDA insights, Logistic Regression odds ratios, and SHAP global explanations all showed **strong directional agreement**, confirming the robustness of conclusions.

---

##  3. Power BI Dashboard

The dashboard translates analytics into **executive-ready insights**.

### Design Philosophy (2026-Ready)

* One page = one story
* Percentages over raw counts
* Behavioral + financial + policy drivers combined
* Minimal slicers, maximum clarity

---

###  Key Pages

#### 1. Executive Overview

* Overall attrition rate
* Attrition by department, gender, and age band
* High-level organizational hotspots

#### 2. Demographics & Role Analysis

* Department → Job Role sunburst
* Attrition by education field and marital status
* Who is leaving?

#### 3. **Retention Risk & Drivers (Core Page)**

A single high-impact page combining:

**Sentiment & Engagement**

* 100% stacked bars for Job Involvement, Work-Life Balance, Job Satisfaction
* Traffic-light color logic highlights low-engagement attrition

**Financial & Growth Triggers**

* Scatter: Monthly Income vs Salary Hike
* Promotion lag analysis showing rising attrition after 3+ years

**Actionable Insight Footer**

> Burnout (OverTime) and stagnation (3+ years since promotion) are stronger predictors of attrition than base salary alone.

---

##  Key Business Insights

* Attrition is driven more by **burnout and stagnation** than salary alone
* Promotion cadence is a critical retention lever
* Overtime and frequent travel significantly elevate risk
* Manager relationship stability plays a dual role (early mismatch vs long-term stagnation)
* Engagement metrics provide early warning signals before exits occur

---

##  Recommendations

* Introduce early-warning retention monitoring for high-risk profiles
* Review promotion cycles for high-performing overtime employees
* Rebalance workloads and travel policies
* Use ML outputs as **decision support**, not punitive tools

---

##  Conclusion

This project demonstrates a **complete HR analytics lifecycle**:

> **EDA → Explainable ML → Executive Dashboard → Actionable Strategy**

It emphasizes:

* Interpretability
* Business relevance
* Ethical people analytics
* Decision-ready storytelling

---

## 🛠 Tools & Technologies

* Python (Pandas, Seaborn, Scikit-learn, XGBoost, SHAP)
* Power BI
* Jupyter Notebook

---

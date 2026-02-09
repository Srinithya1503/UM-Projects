import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import joblib

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Supply Chain Analytics Dashboard",
    layout="wide"
)

st.title(" Supply Chain Demand Analytics & Decision Support")

st.markdown("""
This dashboard translates **exploratory and predictive insights**
into actionable supply chain intelligence.

⚠️ **Note**: This is a decision-support system built on a limited,
cross-sectional dataset and should not be interpreted as a
production forecasting engine.
""")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("supply_chain_data.csv")

df = load_data()

# --------------------------------------------------
# Feature Engineering (consistent with notebook)
# --------------------------------------------------
def feature_engineering(df):
    df = df.copy()

    df["Inventory_Pressure"] = df["Order quantities"] / (df["Stock levels"] + 1)
    df["Supply_Risk_Index"] = df["Defect rates"] * df["Lead times"]
    df["Cost_per_Unit"] = df["Manufacturing costs"] / (df["Production volumes"] + 1)
    df["Logistics_Delay_Index"] = df["Lead times"] + df["Manufacturing lead time"]

    return df

df_fe = feature_engineering(df)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Demand Drivers",
        "Inventory & Risk Analysis",
        "Quality & Logistics",
        "Model Explainability",
        "Data Explorer",
        "Methodology & Limitations"
    ]
)

# --------------------------------------------------
# Overview
# --------------------------------------------------
if section == "Overview":
    st.header("📊 Executive Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Products", df["SKU"].nunique())
    col2.metric("Avg Stock Level", round(df["Stock levels"].mean(), 1))
    col3.metric("Avg Demand", round(df["Number of products sold"].mean(), 1))

    st.markdown("""
    **Key Insights**
    - Demand is strongly influenced by **inventory availability**
    - Cost variables play a secondary role
    - Logistics reliability affects demand indirectly
    """)

# --------------------------------------------------
# Demand Drivers
# --------------------------------------------------
elif section == "Demand Drivers":
    st.header("📈 Demand Drivers Analysis")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df_fe,
        x="Inventory_Pressure",
        y="Number of products sold",
        ax=ax
    )
    ax.set_title("Demand vs Inventory Pressure")
    st.pyplot(fig)

    st.markdown("""
    **Interpretation**
    - High inventory pressure often precedes higher demand
    - Indicates supply-constrained demand patterns
    """)

# --------------------------------------------------
# Inventory & Risk
# --------------------------------------------------
elif section == "Inventory & Risk Analysis":
    st.header("📦 Inventory & Supply Risk")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=df_fe,
        x="Product type",
        y="Inventory_Pressure",
        ax=ax
    )
    ax.set_title("Inventory Pressure by Product Type")
    st.pyplot(fig)

    st.markdown("""
    **Insight**
    - Certain product categories consistently operate
      under higher inventory stress
    """)

# --------------------------------------------------
# Quality & Logistics
# --------------------------------------------------
elif section == "Quality & Logistics":
    st.header("🚚 Quality & Logistics Impact")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df_fe,
        x="Defect rates",
        y="Lead times",
        ax=ax
    )
    ax.set_title("Defect Rates vs Lead Times")
    st.pyplot(fig)

    st.markdown("""
    **Observation**
    - Higher defect rates often coincide with longer lead times
    - Quality failures amplify logistics delays
    """)

# --------------------------------------------------
# Model Explainability
# --------------------------------------------------
elif section == "Model Explainability":
    st.header("🤖 Model Explainability (SHAP)")

    st.markdown("""
    A Random Forest model was trained to **understand demand drivers**.
    The goal is explanation — not real-time prediction.
    """)

    # Prepare data
    target = "Number of products sold"
    drop_cols = ["SKU", "Revenue generated", target]

    X = df_fe.drop(columns=drop_cols, errors="ignore")
    y = df_fe[target]

    # Encode categoricals
    for col in X.select_dtypes(include="object").columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )
    model.fit(X_scaled, y)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)

    st.subheader("Top Demand Drivers")

    importance = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=importance.values[:10], y=importance.index[:10], ax=ax)
    ax.set_title("Top 10 Demand Drivers")
    st.pyplot(fig)

    st.markdown("""
    **Key Takeaways**
    - Inventory pressure dominates demand prediction
    - Supply risk indicators matter more than cost
    - Pricing has limited short-term influence
    """)

# --------------------------------------------------
# Data Explorer
# --------------------------------------------------
elif section == "Data Explorer":
    st.header("🔍 Data Explorer")

    st.dataframe(df_fe)

# --------------------------------------------------
# Methodology & Limitations
# --------------------------------------------------
elif section == "Methodology & Limitations":
    st.header("📘 Methodology & Limitations")

    st.markdown("""
    **Methodology**
    - Exploratory Data Analysis (EDA)
    - Feature engineering grounded in supply chain theory
    - Random Forest for explainability
    - SHAP for interpretability

    **Limitations**
    - Small dataset (~100 rows)
    - Cross-sectional (no time series)
    - Synthetic / constrained variability
    - Not suitable for production forecasting

    **Recommended Next Steps**
    - Collect time-series sales data
    - Integrate real logistics event data
    - Transition to demand forecasting models
    """)

st.markdown("---")
st.caption("Supply Chain Analytics | UM Internship Project")

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Supply Chain Analytics Dashboard",
    layout="wide"
)

st.title("Supply Chain Demand Analytics & Decision Support")

st.markdown("""
This dashboard translates exploratory and predictive insights
into actionable supply chain intelligence.

Note: This is a decision-support prototype built on a small
cross-sectional dataset and not a production forecasting engine.
""")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "supply_chain_data.csv")
    return pd.read_csv(file_path)

df = load_data()

# --------------------------------------------------
# Feature Engineering (Same as Modeling Notebook)
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
        "Executive Overview",
        "Demand Analysis",
        "Inventory & Risk",
        "Quality & Logistics",
        "Model Insights",
        "Data Explorer",
        "Methodology"
    ]
)

# --------------------------------------------------
# Executive Overview
# --------------------------------------------------
if section == "Executive Overview":

    st.header("Executive Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total SKUs", df["SKU"].nunique())
    col2.metric("Average Demand", round(df["Number of products sold"].mean(), 1))
    col3.metric("Average Stock Level", round(df["Stock levels"].mean(), 1))

    st.markdown("""
    Key Observations:

    • Demand is strongly influenced by inventory availability  
    • Cost variables have limited direct influence  
    • Logistics reliability indirectly impacts demand  
    """)

# --------------------------------------------------
# Demand Analysis
# --------------------------------------------------
elif section == "Demand Analysis":

    st.header("Demand vs Inventory Pressure")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df_fe,
        x="Inventory_Pressure",
        y="Number of products sold",
        ax=ax
    )
    ax.set_title("Demand vs Inventory Pressure")
    st.pyplot(fig)

    st.markdown("""
    Interpretation:

    Higher inventory pressure often signals constrained demand.
    Demand variability supports the need for predictive modeling.
    """)

# --------------------------------------------------
# Inventory & Risk
# --------------------------------------------------
elif section == "Inventory & Risk":

    st.header("Inventory Stress by Product Type")

    fig, ax = plt.subplots()
    sns.boxplot(
        data=df_fe,
        x="Product type",
        y="Inventory_Pressure",
        ax=ax
    )
    ax.set_title("Inventory Pressure Distribution")
    st.pyplot(fig)

    st.markdown("""
    Insight:

    Certain product categories operate under higher inventory stress,
    increasing stockout and working capital risk.
    """)

# --------------------------------------------------
# Quality & Logistics
# --------------------------------------------------
elif section == "Quality & Logistics":

    st.header("Supply Risk Relationship")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df_fe,
        x="Defect rates",
        y="Lead times",
        ax=ax
    )
    ax.set_title("Defect Rates vs Lead Times")
    st.pyplot(fig)

    st.markdown("""
    Observation:

    Higher defect rates are often associated with longer lead times.
    Quality instability increases supply chain fragility.
    """)

# --------------------------------------------------
# Model Insights
# --------------------------------------------------
elif section == "Model Insights":

    st.header("Demand Driver Analysis")

    target = "Number of products sold"
    drop_cols = ["SKU", "Revenue generated", target]

    X = df_fe.drop(columns=drop_cols, errors="ignore")
    y = df_fe[target]

    # Encode categorical columns
    for col in X.select_dtypes(include="object").columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # Lightweight Model
    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=6,
        random_state=42
    )

    model.fit(X, y)

    importance = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    fig, ax = plt.subplots()
    sns.barplot(
        x=importance.values[:10],
        y=importance.index[:10],
        ax=ax
    )
    ax.set_title("Top 10 Demand Drivers")
    st.pyplot(fig)

    st.markdown("""
    Key Takeaways:

    • Inventory pressure is the dominant demand driver  
    • Supply risk indicators influence demand indirectly  
    • Cost and price have limited short-term impact  
    """)

# --------------------------------------------------
# Data Explorer
# --------------------------------------------------
elif section == "Data Explorer":

    st.header("Dataset Explorer")
    st.dataframe(df_fe)

# --------------------------------------------------
# Methodology
# --------------------------------------------------
elif section == "Methodology":

    st.header("Methodology & Limitations")

    st.markdown("""
    Methodology:

    • Exploratory Data Analysis  
    • Domain-driven feature engineering  
    • Random Forest for demand interpretation  
    • Feature importance for explainability  

    Limitations:

    • Small dataset (~100 rows)  
    • Cross-sectional (not time-series)  
    • Limited generalization capability  

    Recommended Next Step:

    Transition to time-series demand forecasting using
    historical transactional data.
    """)

st.markdown("---")
st.caption("Supply Chain Analytics | Internship Project")

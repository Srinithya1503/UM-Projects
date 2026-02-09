# src/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

class SupplyChainPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.encoders = {}
        self.scaler = StandardScaler()

    def feature_engineering(self):
        self.df['Total_Manufacturing_Cost'] = (
            self.df['Manufacturing costs'] *
            self.df['Number of products sold']
        )

        self.df['Profit_Margin'] = (
            (self.df['Revenue generated'] - self.df['Total_Manufacturing_Cost']) /
            (self.df['Revenue generated'] + 1)
        )

        self.df['Inventory_Pressure'] = (
            self.df['Order quantities'] / (self.df['Stock levels'] + 1)
        )

        self.df['Supply_Risk_Index'] = (
            self.df['Lead times'] * self.df['Defect rates']
        )

        self.df['Cost_per_Unit'] = (
            self.df['Manufacturing costs'] / (self.df['Production volumes'] + 1)
        )

        return self.df

    def encode_categoricals(self, X):
        cat_cols = X.select_dtypes(include='object').columns
        for col in cat_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            self.encoders[col] = le
        return X

    def split_and_scale(self, target='Number of products sold'):
        drop_cols = ['SKU', 'Revenue generated', target]
        X = self.df.drop(columns=drop_cols, errors='ignore')
        y = self.df[target]

        X = self.encode_categoricals(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        return X_train, X_test, y_train, y_test

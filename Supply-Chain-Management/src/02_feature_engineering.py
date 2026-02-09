import pandas as pd
import numpy as np

class SupplyChainFeatureEngineer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def create_features(self):
        """
        Feature engineering driven by EDA insights:
        - Inventory efficiency
        - Supply risk
        - Cost efficiency
        """

        # Inventory efficiency (supports turnover & DSI analysis)
        self.df['Inventory_Pressure'] = (
            self.df['Number of products sold'] / (self.df['Stock levels'] + 1)
        )

        # Supply risk (captures lead-time + quality instability)
        self.df['Supply_Risk_Index'] = (
            self.df['Lead times'] * self.df['Defect rates']
        )

        # Cost efficiency proxy (cost ≠ revenue insight)
        self.df['Cost_per_Unit'] = (
            self.df['Manufacturing costs'] / (self.df['Production volumes'] + 1)
        )

        # Logistics pressure
        self.df['Logistics_Delay_Index'] = (
            self.df['Shipping times'] + self.df['Manufacturing lead time']
        )

        return self.df


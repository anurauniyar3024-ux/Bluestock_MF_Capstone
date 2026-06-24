import pandas as pd
from pathlib import Path

# Load NAV dataset
file_path = Path("../data/raw/02_nav_history.csv")

df = pd.read_csv(file_path)

print("=" * 60)
print("NAV HISTORY DATASET")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nFirst 5 Rows:")
print(df.head())

df['date'] = pd.to_datetime(df['date'])

print("\nDate Range:")
print("Start:", df['date'].min())
print("End:", df['date'].max())

print("\n" + "=" * 60)
print("FUND MASTER DATASET")
print("=" * 60)

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

nav_df = pd.read_csv(RAW_DATA / "02_nav_history.csv")
transactions_df = pd.read_csv(RAW_DATA / "08_investor_transactions.csv")

# Convert date column to datetime
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Sort by AMFI code and date
nav_df = nav_df.sort_values(by=["amfi_code", "date"])

print(nav_df.head())
print(nav_df.dtypes)

# Check for invalid NAV values
invalid_nav = nav_df[nav_df["nav"] <= 0]

print("\nInvalid NAV values:")
print(invalid_nav)

print("\nNumber of invalid NAV values:", len(invalid_nav))

# ----------------------------
# Investor Transactions Cleaning
# ----------------------------

# Convert transaction_date to datetime
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

print("\nInvestor Transactions Info:")
transactions_df.info()

print("\nMissing Values:")
print(transactions_df.isnull().sum())

print("\nDuplicate Rows:")
print(transactions_df.duplicated().sum())

print("\nUnique Transaction Types:")
print(transactions_df["transaction_type"].unique())

print("\nUnique KYC Status:")
print(transactions_df["kyc_status"].unique())

print("\nInvalid Amount Records:")
invalid_amount = transactions_df[transactions_df["amount_inr"] <= 0]

print(invalid_amount)
print("\nNumber of Invalid Amount Records:", len(invalid_amount))

# Save cleaned datasets
print(PROCESSED_DATA)
print(PROCESSED_DATA.exists())

nav_df.to_csv(PROCESSED_DATA / "02_nav_history_cleaned.csv", index=False)

transactions_df.to_csv(
    PROCESSED_DATA / "08_investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned datasets saved successfully!")
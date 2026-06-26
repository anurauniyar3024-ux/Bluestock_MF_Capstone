import os
import sqlite3
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DATA = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"
# Delete old database if it exists
if DB_PATH.exists():
    os.remove(DB_PATH)

# Connect to SQLite database
print(DB_PATH)
print(DB_PATH.exists())
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Database connected successfully!")

# Execute schema.sql
with open(SCHEMA_PATH, "r") as file:
    schema = file.read()

cursor.executescript(schema)
conn.commit()

print("Database schema created successfully!")

# Load cleaned CSV files
fund_nav = pd.read_csv(PROCESSED_DATA / "02_nav_history_cleaned.csv")
transactions = pd.read_csv(PROCESSED_DATA / "08_investor_transactions_cleaned.csv")

# Insert into database
fund_nav.to_sql("fact_nav", conn, if_exists="append", index=False)

transactions.to_sql("fact_transactions", conn, if_exists="append", index=False)

print("Data loaded into SQLite successfully!")

conn.close()
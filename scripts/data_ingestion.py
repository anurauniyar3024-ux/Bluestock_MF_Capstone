# print("Script started")
# import pandas as pd
# from pathlib import Path
#
# raw_folder = Path("../data/raw")
#
# for csv_file in raw_folder.glob("*.csv"):
#     print("\n" + "=" * 60)
#     print(f"FILE: {csv_file.name}")
#
#     df = pd.read_csv(csv_file)
#
#     print("Shape:", df.shape)
#     print("Columns:")
#     print(df.columns.tolist())
#
#     print("\nFirst 3 rows:")
#     print(df.head(3))

import pandas as pd
from pathlib import Path

raw_folder = Path("../data/raw")

for csv_file in raw_folder.glob("*.csv"):
    print("\n" + "=" * 60)
    print(f"FILE: {csv_file.name}")

    df = pd.read_csv(csv_file)

    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 3 rows:")
    print(df.head(3))
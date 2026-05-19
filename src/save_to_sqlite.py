import pandas as pd
import sqlite3

db_path = "data/db/fx_data.db" 

conn = sqlite3.connect(db_path)
print("DB接続OK")

file_path = "data/processed/usdjpy_with_diff.csv"
df = pd.read_csv(file_path)

print("csv読み込みOK")
print(df.head())

df.to_sql("fx_rates", conn, if_exists="replace", index=False)
print("SQLite保存OK")

conn.close()
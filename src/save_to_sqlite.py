#configを見てDB保存

import pandas as pd
import sqlite3
from config import PROCESSED_CSV_PATH, DB_PATH,TABLE_NAME

conn = sqlite3.connect(DB_PATH)

df = pd.read_csv(PROCESSED_CSV_PATH)

df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
print("SQLite保存OK")

conn.close()
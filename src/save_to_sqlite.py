# configを見てDB保存

import sqlite3
import pandas as pd
from config import PROCESSED_CSV_PATH, DB_PATH, TABLE_NAME

def main():
    df = pd.read_csv(PROCESSED_CSV_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    print("SQLite保存OK")


if __name__ == "__main__":
    main()
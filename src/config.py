#日付・通貨ペア・ファイルパスを管理

START_DATE = "2026-04-01"
END_DATE = "2026-04-30"

BASE = "USD"
QUOTE = "JPY"

PAIR = f"{BASE.lower()}{QUOTE.lower()}"

RAW_CSV_PATH = f"data/raw/{PAIR}_{START_DATE}_{END_DATE}.csv" #raw CSV のファイル
PROCESSED_CSV_PATH = f"data/processed/{PAIR}_with_diff.csv" #processed CSV のファイル
DB_PATH = "data/db/fx_data.db" #SQLite のDBファイル
TABLE_NAME = "fx_rates" #DBの中のテーブル名
#configを見てAPI取得

import requests
import pandas as pd
from config import START_DATE, END_DATE, BASE, QUOTE, RAW_CSV_PATH

url = f"https://api.frankfurter.dev/v2/rates?from={START_DATE}&to={END_DATE}&base={BASE}&quotes={QUOTE}"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print("重複している日付け:")
print(df[df.duplicated(subset=["date"], keep=False)])

df = df.drop_duplicates(subset=["date"], keep="last").reset_index(drop=True)

first_date = df["date"].iloc[0]
last_date = df["date"].iloc[-1]
days_count = len(df)

print(f"{first_date} から {last_date} までの {days_count}日分")

df.to_csv(RAW_CSV_PATH, index=False)
print("CSV保存OK")
print(RAW_CSV_PATH)
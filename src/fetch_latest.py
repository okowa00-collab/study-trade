#python src/fetch_latest.py

import requests
import pandas as pd

url = "https://api.frankfurter.dev/v2/rates?from=2026-05-01&to=2026-05-05&base=USD&quotes=JPY"
response = requests.get(url)

data = response.json()

first_date = data[0]["date"]
last_date = data[-1]["date"]
days_count = len(data)

print(f"{first_date} から {last_date} までの {days_count}日分")

df = pd.DataFrame(data)
print(df)

file_path = f"data/raw/usdjpy_{first_date}_{last_date}.csv"
df.to_csv(file_path, index=False)

print("CSV保存OK")
print(file_path)


#python src/read_csv.py

import pandas as pd

#情報の取り方
file_path = "data/raw/usdjpy_2026-05-01_2026-05-05.csv"
loaded_df = pd.read_csv(file_path)

loaded_df["diff"] = loaded_df["rate"].diff()

output_path = "data/processed/usdjpy_with_diff.csv"
loaded_df.to_csv(output_path, index=False)

print("加工済みCSV保存OK")
print(output_path)
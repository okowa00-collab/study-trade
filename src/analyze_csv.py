import pandas as pd

file_path = "data/processed/usdjpy_with_diff.csv"
df = pd.read_csv(file_path)

print(df.columns)
print(df.head())
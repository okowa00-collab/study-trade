# configを見て加工

from pathlib import Path

import pandas as pd

from config import RAW_CSV_PATH, PROCESSED_CSV_PATH


def main():
    loaded_df = pd.read_csv(RAW_CSV_PATH)

    loaded_df["diff"] = loaded_df["rate"].diff().round(2)
    loaded_df["prev_diff"] = loaded_df["diff"].shift(1)
    loaded_df["day"] = pd.to_datetime(loaded_df["date"])
    loaded_df["weekday"] = loaded_df["day"].dt.day_name()

    Path(PROCESSED_CSV_PATH).parent.mkdir(parents=True, exist_ok=True)

    loaded_df.to_csv(PROCESSED_CSV_PATH, index=False)

    print("加工済みCSV保存OK")
    print(PROCESSED_CSV_PATH)


if __name__ == "__main__":
    main()

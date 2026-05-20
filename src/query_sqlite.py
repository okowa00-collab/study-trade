#configを見てDB検索(SQLで分析・集計する)

import sqlite3
from config import DB_PATH, TABLE_NAME

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute(f"""
SELECT
            MIN(date) AS start_date,
            MAX(date) AS end_date,
            COUNT(*) AS total_count,
            COUNT(diff) AS diff_count,
            SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS up_count,
            SUM(CASE WHEN diff < 0 THEN 1 ELSE 0 END) AS down_count,
            SUM(CASE WHEN diff = 0 THEN 1 ELSE 0 END) AS same_count
FROM {TABLE_NAME};
""")

summary = cur.fetchone()

start_date = summary["start_date"]
end_date = summary["end_date"]
total_count = summary["total_count"]
diff_count = summary["diff_count"]
up_count = summary["up_count"]
down_count = summary["down_count"]
same_count = summary["same_count"]

up_rate = up_count / diff_count * 100

print(f"全データは {total_count}件")
print(f"前日比があるデータは {diff_count}件")
print(f"上がった日は {up_count}日")
print(f"下がった日は {down_count}日")
print(f"変わらなかった日は {same_count}日")

print("分析メモ")
print(f"{start_date} から {end_date} までのデータを分析しました。")
print(f"前日比を比較できる{diff_count}回のうち、上昇が{up_count}回、下落が{down_count}回、横ばいが{same_count}回でした。")
print(f"上昇割合は {round(up_rate, 1)}% です")

cur.execute(f"""
            SELECT date, rate, diff
            FROM {TABLE_NAME}
            WHERE diff IS NOT NULL
            ORDER BY diff DESC
            LIMIT 1;
""")

max_up_day = cur.fetchone()

print("一番上がった日")
print(f"{max_up_day['date']} は前日比 {max_up_day['diff']} で、レートは {max_up_day['rate']} でした。")

cur.execute(f"""
            SELECT date, rate, diff
            FROM {TABLE_NAME}
            WHERE diff IS NOT NULL
            ORDER BY diff ASC
            LIMIT 1;
""")

max_down_day = cur.fetchone()

print("一番下がった日")
print(f"{max_down_day['date']} は前日比 {max_down_day['diff']} で、レートは {max_down_day['rate']} でした。")

conn.close()

import sqlite3

db_path = "data/db/fx_data.db"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
SELECT 
            SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END),
            SUM(CASE WHEN diff < 0 THEN 1 ELSE 0 END),
            SUM(CASE WHEN diff = 0 THEN 1 ELSE 0 END)
FROM fx_rates;
""")

up_count, down_count, same_count = cur.fetchone()


print(f"上がった日は {up_count}日")
print(f"下がった日は {down_count}日")
print(f"変わらなかった日は {same_count}日")

conn.close()

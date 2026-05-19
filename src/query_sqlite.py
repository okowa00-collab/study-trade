import sqlite3

db_path = "data/db/fx_data.db"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
SELECT
            AVG(rate),
            MAX(rate),
            MIN(rate),
            COUNT(*)
FROM fx_rates;
""")
summary = cur.fetchone()

avg_rate, max_rate, min_rate, count =summary


print(f"平均レートは{round(avg_rate, 2)}")
print(f"最大レートは {max_rate}")
print(f"最小レートは {min_rate}")
print(f"件数は {count}件")

conn.close()

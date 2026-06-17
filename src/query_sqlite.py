#configを見てDB検索(SQLで分析・集計する)

import sqlite3


from config import DB_PATH, TABLE_NAME


def main():
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


    cur.execute(f"""
                SELECT AVG(diff)AS avg_diff
                FROM {TABLE_NAME}
                WHERE diff IS NOT NULL;
                """)

    avg_row = cur.fetchone()

    print("平均前日比")
    print(f"この期間の平均前日比は {round(avg_row['avg_diff'], 2)}でした。")

    cur.execute(f"""
                SELECT
                    weekday,
                    COUNT(diff) AS diff_count,
                    SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS up_count,
                    ROUND(
                        SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(diff),
                    1            
                    ) AS up_rate,
                ROUND(AVG(diff), 2) AS avg_diff
                FROM {TABLE_NAME}
                WHERE diff IS NOT NULL
                AND weekday NOT IN ('Saturday', 'Sunday')
                GROUP BY weekday
                ORDER BY up_rate DESC;
                """)

    weekday_rows = cur.fetchall()

    print("曜日ごとの上昇率")

    for row in weekday_rows:
        print(
            f"{row['weekday']}: "
            f"{row['diff_count']}回中 {row['up_count']}回上昇 "
            f"上昇率 {row['up_rate']}% "
            f"平均前日比 {row['avg_diff']}"
        )

    cur.execute(f"""
                SELECT
                    COUNT(*) AS prev_up_count,
                    SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS next_up_count,
                    ROUND(
                        SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                    1
                    ) AS next_up_rate
                FROM {TABLE_NAME}
                WHERE prev_diff > 0;
                """)

    prev_up_row = cur.fetchone()

    print("前日上昇後の動き")
    print(
        f"前日が上がっていた日は {prev_up_row['prev_up_count']}回あり、"
        f"その翌日も上がったのは {prev_up_row['next_up_count']}回、"
        f"上昇率は {prev_up_row['next_up_rate']}% でした。"
    )

    cur.execute(f"""
                SELECT
                    COUNT(*) AS prev_down_count,
                    SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS next_up_count,
                    ROUND(
                        SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                    1
                    ) AS next_up_rate
                FROM {TABLE_NAME}
                WHERE prev_diff < 0;
                """)

    prev_down_row = cur.fetchone()

    print("前日下落後の動き")
    print(
        f"前日が下がっていた日は {prev_down_row['prev_down_count']}回あり、"
        f"その翌日も上がったのは {prev_down_row['next_up_count']}回、"
        f"上昇率は {prev_down_row['next_up_rate']}% でした。"
    )

    cur.execute(f"""
                SELECT
                    COUNT(*) AS prev_same_count,
                    SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) AS next_up_count,
                    ROUND(
                        SUM(CASE WHEN diff > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
                    1
                    ) AS next_up_rate
                FROM {TABLE_NAME}
                WHERE prev_diff = 0;
                """)

    prev_same_row = cur.fetchone()

    print("前日横ばい後の動き")
    print(
        f"前日が横ばいだった日は {prev_same_row['prev_same_count']}回あり、"
        f"その翌日も上がったのは {prev_same_row['next_up_count']}回、"
        f"上昇率は {prev_same_row['next_up_rate']}% でした。"
    )

    conn.close()


if __name__ == "__main__":
    main()

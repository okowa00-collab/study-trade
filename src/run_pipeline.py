# 処理をまとめて動かす
import subprocess
import sys
from pathlib import Path

def main():

    ROOT_DIR = Path(__file__).resolve().parent.parent

    def run_script(script_name, start_message, done_message):
        script_path = ROOT_DIR / "src" / script_name

        print(start_message)

        subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            cwd=ROOT_DIR,
        )
        
        print(done_message)

    run_script(
        "fetch_rates.py",
        "=== 1. 為替データを取得します ===",
        "=== fetch_rates.py 完了 ===",
    )

    run_script(
        "read_csv.py",
        "=== 2. CSVを読み込んで加工します ===",
        "=== read_csv.py 完了 ===",
    )

    run_script(
        "save_to_sqlite.py",
        "=== 3. SQLiteに保存します ===",
        "=== save_to_sqlite.py 完了 ===",
    )

    run_script(
        "query_sqlite.py",
        "=== 4. SQLiteから分析結果を表示します ===",
        "=== query_sqlite.py 完了 ===",
    )

if __name__ == "__main__":
    main()
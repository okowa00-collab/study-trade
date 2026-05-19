#処理をまとめて動かす

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

fetch_script = ROOT_DIR / "src" / "fetch_rates.py"
read_script = ROOT_DIR / "src" / "read_csv.py"
save_script = ROOT_DIR / "src" / "save_to_sqlite.py"
query_script = ROOT_DIR / "src" / "query_sqlite.py"

print("=== 1. 為替データを取得します。===")
subprocess.run(
    [sys.executable, str(fetch_script)],
    check = True,
    cwd=ROOT_DIR,
)
print("=== fetch_rates.py 完了 ===")


print("=== 2. CSVを読み込んで加工します ===")
subprocess.run(
    [sys.executable, str(read_script)],
    check = True,
    cwd=ROOT_DIR,
)
print("=== read_csv.py 完了 ===")


print("=== 3. SQLiteに保存します ===")
subprocess.run(
    [sys.executable, str(save_script)],
    check = True,
    cwd=ROOT_DIR,
)
print("=== save_to_sqlite.py 完了 ===")


print("=== 4. SQLiteから分析結果を表示します ===")
subprocess.run(
    [sys.executable, str(query_script)],
    check = True,
    cwd=ROOT_DIR,
)
print("=== query_sqlite.py 完了 ===")
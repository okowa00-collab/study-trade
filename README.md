# study-trade

Python、pandas、SQLite、SQLを使って、為替データの取得・加工・保存・集計を学ぶためのリポジトリです。

## できること

- APIからUSD/JPYの為替データを取得する
- CSVに保存する
- 前日比を計算する
- SQLiteに保存する
- SQLで簡単な集計をする

## 実行方法

python src/run_pipeline.py

## 主なファイル

- src/config.py: 日付、通貨ペア、保存先などの設定
- src/fetch_rates.py: APIから為替データを取得してraw CSVに保存
- src/read_csv.py: raw CSVを読み込み、前日比や曜日を追加
- src/save_to_sqlite.py: 加工済みCSVをSQLiteに保存
- src/query_sqlite.py: SQLで分析結果を表示
- src/run_pipeline.py: 一連の処理をまとめて実行
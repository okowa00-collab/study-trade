# AGENTS.md

## Project goal

This repository is for learning Python, pandas, SQLite, and SQL using FX rate data.
The goal is not to build a profitable trading bot.
The goal is to learn data collection, cleaning, analysis, storage, and querying.

## Working rules

- Keep changes small.
- Do not refactor the whole project unless explicitly asked.
- Prefer beginner-friendly Python.
- Explain changes in Japanese.
- Do not add new dependencies unless necessary.
- Do not implement trading automation or buy/sell signals unless explicitly requested.
- Before changing files, inspect the current structure and explain the plan.
- After changing files, show the commands used and the result.

## Current project structure

- src/config.py: shared settings
- src/fetch_rates.py: fetch FX data
- src/read_csv.py: read raw CSV and add diff column
- src/save_to_sqlite.py: save processed data to SQLite
- src/query_sqlite.py: run SQL analysis
- src/run_pipeline.py: run the full pipeline
- data/raw/: raw CSV files
- data/processed/: processed CSV files
- fx_data.db: SQLite database

## Style

Use simple code.
Prioritize readability over cleverness.
When explaining, assume the learner is still new to Python, pandas, SQLite, SQL, and FX data.
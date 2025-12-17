import pandas as pd
from pathlib import Path

DB_PATH = Path("data/signals.duckdb")

def get_conn():
    try:
        import duckdb
    except ModuleNotFoundError:
        raise RuntimeError(
            "DuckDB is not installed. Add `duckdb` to requirements.txt."
        )

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(DB_PATH)

def write_signal(signal: dict):
    conn = get_conn()
    df = pd.DataFrame([signal])

    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            timestamp TIMESTAMP,
            service VARCHAR,
            signal_type VARCHAR,
            name VARCHAR,
            value DOUBLE,
            tags MAP(VARCHAR, VARCHAR),
            source VARCHAR
        )
    """)
    conn.execute("INSERT INTO signals SELECT * FROM df")
    conn.close()

def read_signals(service=None):
    conn = get_conn()
    query = "SELECT * FROM signals"
    if service:
        query += f" WHERE service='{service}'"
    df = conn.execute(query).fetchdf()
    conn.close()
    return df

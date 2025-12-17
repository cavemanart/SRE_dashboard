import pandas as pd
from pathlib import Path

DB_PATH = Path("data/signals.duckdb")

def get_conn():
    import duckdb
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(DB_PATH)

def write_signal(signal: dict):
    conn = get_conn()
    df = pd.DataFrame([signal])

    # Create table if not exists
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
    """
    Read signals safely. If table does not exist, return empty DataFrame.
    """
    conn = get_conn()
    try:
        query = "SELECT * FROM signals"
        if service:
            query += f" WHERE service='{service}'"
        df = conn.execute(query).fetchdf()
    except Exception as e:
        # Table probably does not exist yet
        df = pd.DataFrame(columns=[
            "timestamp", "service", "signal_type", "name", "value", "tags", "source"
        ])
    conn.close()
    return df

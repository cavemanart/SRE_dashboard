import duckdb
import pandas as pd

DB_PATH = "data/signals.duckdb"

def write_signal(signal):
    conn = duckdb.connect(DB_PATH)
    df = pd.DataFrame([signal])
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS signals AS
        SELECT * FROM df
        """
    )
    conn.execute("INSERT INTO signals SELECT * FROM df")
    conn.close()

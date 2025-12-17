import streamlit as st
import pandas as pd
import numpy as np

def render_overview():
    st.header("📊 Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Latency p99", "420ms", "+30ms")
    col2.metric("Error Rate", "0.12%", "-0.02%")
    col3.metric("Traffic", "1.2k RPS", "+8%")

    data = pd.DataFrame({
        "time": pd.date_range(end=pd.Timestamp.now(), periods=50),
        "latency": np.random.normal(350, 40, 50)
    })

    st.line_chart(data.set_index("time"))

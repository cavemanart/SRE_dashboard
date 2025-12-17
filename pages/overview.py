import streamlit as st
import pandas as pd
import numpy as np

def render_overview():
    st.header("📊 Overview")

    from storage.signals import read_signals

    service = st.session_state.get("service", "payments-service")
    df = read_signals(service)

    # Show metrics summary if data exists
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        latest = df.sort_values("timestamp").iloc[-1]
        col1.metric("Latest Metric Value", latest["value"])
        col2.metric("Signal Type", latest["signal_type"])
        col3.metric("Total Signals", len(df))

        st.subheader("Time Series for Selected Service")
        ts = df.groupby("timestamp")["value"].mean().reset_index()
        st.line_chart(ts.set_index("timestamp"))
    else:
        st.info("No signals available for this service. Add some in the Data Input page.")

import streamlit as st
import pandas as pd
from ingestion.manual import save_manual_signal

def render_data_input():
    st.header("✍️ Manual Data Input")

    with st.form("manual_signal"):
        col1, col2 = st.columns(2)

        service = col1.text_input("Service", "payments-service")
        signal_type = col2.selectbox(
            "Signal Type",
            ["latency", "traffic", "error", "saturation", "incident"]
        )

        name = st.text_input("Metric / Event Name")
        value = st.number_input("Value", step=0.01)
        timestamp = st.date_input("Date")

        submitted = st.form_submit_button("Add Signal")

        if submitted:
            save_manual_signal(
                service=service,
                signal_type=signal_type,
                name=name,
                value=value,
                timestamp=timestamp
            )
            st.success("Signal added successfully")

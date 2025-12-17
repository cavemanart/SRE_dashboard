import streamlit as st
import pandas as pd

def render_data_input():
    st.header("✍️ Manual Data Input")

    try:
        from ingestion.manual import save_manual_signal
        from storage.signals import read_signals
    except Exception as e:
        st.error("Failed to load storage layer")
        st.exception(e)
        return

    st.subheader("Add a Single Signal")
    with st.form("manual_signal"):
        service = st.text_input("Service", st.session_state.get("service", "payments-service"))
        signal_type = st.selectbox(
            "Signal Type",
            ["latency", "traffic", "error", "saturation", "incident"]
        )
        name = st.text_input("Metric / Event Name")
        value = st.number_input("Value", step=0.01)
        timestamp = st.date_input("Date")

        submitted = st.form_submit_button("Add Signal")

        if submitted:
            save_manual_signal(service, signal_type, name, value, timestamp)
            st.success("Signal added successfully")

    st.subheader("Bulk Upload CSV")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        if "timestamp" in df.columns and "service" in df.columns and "name" in df.columns and "value" in df.columns:
            df["source"] = "manual"
            for _, row in df.iterrows():
                save_manual_signal(
                    row["service"], row.get("signal_type", "custom"), row["name"], row["value"], pd.to_datetime(row["timestamp"]).date()
                )
            st.success(f"Uploaded {len(df)} signals")
        else:
            st.error("CSV must contain: timestamp, service, name, value")

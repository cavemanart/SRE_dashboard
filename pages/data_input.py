import streamlit as st

def render_data_input():
    st.header("✍️ Manual Data Input")

    try:
        from ingestion.manual import save_manual_signal
    except Exception as e:
        st.error("Failed to load storage layer")
        st.exception(e)
        return  # ⬅️ NOT st.stop()

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
            st.success("Signal added")

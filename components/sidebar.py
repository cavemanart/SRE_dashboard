import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("🛠 SRE Console")

        st.selectbox(
            "Service",
            ["payments-service", "auth-service", "search-service"]
        )

        st.selectbox(
            "Environment",
            ["prod", "staging"]
        )

        st.radio(
            "Navigate",
            ["Overview", "Services", "SLOs", "Incidents", "Insights", "Simulator"]
        )

        st.divider()
        st.caption("Reliability first.")

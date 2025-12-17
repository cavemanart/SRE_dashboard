import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("🛠 SRE Console")

        st.session_state.service = st.selectbox(
            "Service",
            ["payments-service", "auth-service", "search-service"],
            key="service_select"
        )

        st.session_state.environment = st.selectbox(
            "Environment",
            ["prod", "staging"],
            key="env_select"
        )

        st.session_state.page = st.radio(
            "Navigate",
            ["Overview", "Data Input", "Services", "SLOs", "Incidents", "Insights", "Simulator"],
            key="page_select"
        )

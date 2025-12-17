import streamlit as st

def render_top_bar():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Health Score", "92", "+2")
    col2.metric("Active Incidents", "1")
    col3.metric("Error Budget", "78%")
    col4.metric("Burn Rate", "0.8x")

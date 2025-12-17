import streamlit as st

# Components
from components.sidebar import render_sidebar
from components.top_bar import render_top_bar

# Pages
from pages.overview import render_overview
from pages.data_input import render_data_input

st.set_page_config(
    page_title="SRE Intelligence Console",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar + top bar
render_sidebar()
render_top_bar()

# Page routing
page = st.session_state.get("page", "Overview")

if page == "Overview":
    render_overview()
elif page == "Data Input":
    render_data_input()
else:
    st.info(f"{page} page coming soon.")

import streamlit as st
from components.sidebar import render_sidebar
from components.top_bar import render_top_bar
from pages.overview import render_overview

st.set_page_config(
    page_title="SRE Intelligence Console",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_sidebar()
render_top_bar()
render_overview()

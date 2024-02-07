import streamlit as st
from config import pagesetup as ps

# Set st.page_config (done once per app not per page)
st.set_page_config(
    page_title=st.secrets.streamlit.page_config_title, 
    page_icon=st.secrets.streamlit.page_config_icon, 
    layout=st.secrets.streamlit.page_config_layout, 
    initial_sidebar_state=st.secrets.streamlit.page_config_sidebar
    )

# Set page title
title = ps.set_title(
    varTitle="FlowGenius",
    varSubtitle="Showcase"
)

#Set page overview
header_overview = ps.set_page_overview(
    varHeader="Overview",
    varText="**Welcome to the FlowGenius Showcase App!** This app will demonstrate **proprietary** functionality created by FlowGenius!"
)


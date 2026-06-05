import streamlit as st
import streamlit.components.v1 as components

# Set up the Streamlit page layout
st.set_page_config(layout="wide", page_title="D2C Ops Audit")

# Read the HTML file
with open("indian_d2c_multichannel_ops_audit_tool.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML within Streamlit
# You may need to adjust the height depending on how the tool expands
components.html(html_content, height=1200, scrolling=True)
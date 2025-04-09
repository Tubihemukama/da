import streamlit as st
from  streamlit_option_menu import option_menu

# Set page configuration FIRST
st.set_page_config(
    page_title="data-help",
    page_icon="🧠",
    layout="wide"
)


st.title("📊 Magnify Analysis")


st.markdown("""
Use the sidebar to navigate:
- **Data Upload**
- **Data Analysis**
- **Data Visualisation**
""")

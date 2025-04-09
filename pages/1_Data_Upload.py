import streamlit as st
import sqlite3
import pandas as pd

st.title("📁 Upload Data")

uploaded_file = st.file_uploader("Choose an Excel File", type=[".xlsx",".xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())

    # Save to SQLite
    conn = sqlite3.connect('data/data.db')
    df.to_sql('uploaded_data', conn, if_exists='replace', index=False)
    conn.close()
    st.success("Data uploaded to database!")

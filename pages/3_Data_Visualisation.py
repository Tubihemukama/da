import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Visualize Data")

conn = sqlite3.connect('data/data.db')
df = pd.read_sql_query("SELECT * FROM uploaded_data", conn)
conn.close()

if not df.empty:
    column = st.selectbox("Select a column to plot", df.select_dtypes(include='number').columns)

    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)
else:
    st.warning("No data available to visualize. Upload it first.")

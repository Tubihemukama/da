import streamlit as st
import sqlite3
import pandas as pd

st.title("🔍 Analyze Data")

conn = sqlite3.connect('data/data.db')
df = pd.read_sql_query("SELECT * FROM uploaded_data", conn)
conn.close()

if not df.empty:
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())
    #Rename to cater for analysis
    dataset = df
    variable_list = dataset.columns
    numeric_variable_list = dataset.select_dtypes(include="number").columns
    non_numeric_variable_list = dataset.select_dtypes(include=["object", "string", "category"]).columns

    # Numeric Summary
    st.subheader("📈 Numeric Variable Summary")

    # Categorical Summary
    st.subheader("🔠 Non-Numeric Variable Frequency Table")
    def non_numeric_variables():
        all_tables = []
        for var in non_numeric_variable_list:
            frequency_table = dataset[var].value_counts(dropna=False).reset_index()
            frequency_table.columns = ['Category', 'Frequency']
            frequency_table['Percentage'] = (frequency_table['Frequency'] / frequency_table['Frequency'].sum()) * 100
            frequency_table['Percentage'] = frequency_table['Percentage'].round(2)
            frequency_table['Variable'] = var
            frequency_table = frequency_table[['Variable', 'Category', 'Frequency', 'Percentage']]
            all_tables.append(frequency_table)

        combined_table = pd.concat(all_tables, ignore_index=True)
        st.dataframe(combined_table)

    non_numeric_variables()




else:
    st.warning("No data found. Please upload data first.")

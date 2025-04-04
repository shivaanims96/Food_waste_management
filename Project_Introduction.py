import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title = "Multipage App",
    page_icon = " Hi"

)

st.sidebar.success("Select a page above.")


# --- Database Connection ---
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('food_wastage.db')  # Replace with your database file
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

# --- SQL Query Execution ---
def execute_query(conn, query):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None

# --- Project Summary Streamlit App ---
def main():
    st.title("Local Food Wastage Management System")
    st.subheader("Project Summary")

    st.write("""
        This project aims to develop a Local Food Wastage Management System to address the significant issue of food wastage while tackling food insecurity. 
        The system provides a platform for restaurants and individuals to list surplus food, which can then be claimed by NGOs or individuals in need. 
        This is done by using a SQL database, and a user-friendly Streamlit application.
    """)
    

if __name__ == "__main__":
    main()

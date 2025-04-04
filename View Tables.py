import streamlit as st
import pandas as pd
import sqlite3

st.title(" ### View Tables / Dataframes :")
db = 'food_wastage.db'

def select_table(table_name,db):
    try :
        conn = sqlite3.connect(db)
        df = pd.read_sql("select * from "+table_name, conn)
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
        conn.rollback()
    
    return df

val = st.selectbox("Select the Tables",("Providers","receivers","claims","food_listings"))


if val == 'Providers':
    st.write(select_table('providers',db))
elif val == 'receivers':
    st.write(select_table('receivers',db))
elif val == 'claims':
    st.write(select_table('claims',db))
elif val == 'food_listings':
    st.write(select_table('food_listings',db))
else:
    st.write("Something went wrong !!")
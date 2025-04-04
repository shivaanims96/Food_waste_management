import streamlit as st
import pandas as pd
import sqlite3

# --- Database Connection ---
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('food_wastage.db')  # Replace with your database file
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

# --- SQL Query Execution ---
def execute_query(conn, query, params=None):
    try:
        if params:
            df = pd.read_sql_query(query, conn, params=params)
        else:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None

# --- CRUD Operations ---
def add_record(conn, table_name, data):
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(data.values()))
        conn.commit()
        st.success("Record added successfully!")
    except Exception as e:
        st.error(f"Error adding record: {e}")

def update_record(conn, table_name, column_to_update, new_value, where_clause):
    query = f"UPDATE {table_name} SET {column_to_update} = ? WHERE {where_clause}"
    try:
        cursor = conn.cursor()
        cursor.execute(query, (new_value,))
        conn.commit()
        st.success("Record updated successfully!")
    except Exception as e:
        st.error(f"Error updating record: {e}")

def delete_record(conn, table_name, where_clause):
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        st.success("Record deleted successfully!")
    except Exception as e:
        st.error(f"Error deleting record: {e}")

# --- Streamlit App ---
def main():
    st.title("CRUD Operations")

    conn = create_connection()
    if conn is None:
        return

    table_options = ["Providers", "Receivers", "Food_Listings", "Claims"]
    selected_table = st.selectbox("Select Table", table_options)

    operation = st.radio("Select Operation", ["Add", "Update", "Delete"])

    if operation == "Add":
        if selected_table == "Providers":
            name = st.text_input("Name")
            type_ = st.selectbox("Type",["Catering Service","Grocery Store","Restaurant","Supermarket"])
            address = st.text_input("Address")
            city = st.text_input("City")
            contact = st.text_input("Contact")
            if st.button("Add Record"):
                data = {"Name": name, "Type": type_, "Address": address, "City": city, "Contact": contact}
                add_record(conn, selected_table, data)

        elif selected_table == "Receivers":
            name = st.text_input("Name")
            type_ = st.selectbox("Type", ["Charity","Individual","NGO","Shelter"])
            city = st.text_input("City")
            contact = st.text_input("Contact")
            if st.button("Add Record"):
                data = {"Name": name, "Type": type_, "City": city, "Contact": contact}
                add_record(conn, selected_table, data)

        elif selected_table == "Food_Listings":
            food_name = st.text_input("Food Name")
            quantity = st.number_input("Quantity", step=1)
            expiry_date = st.date_input("Expiry Date")
            provider_id = st.number_input("Provider ID", step=1)
            provider_type = st.selectbox("Provider Type",["Catering Service","Grocery Store","Restaurant","Supermarket"])
            location = st.text_input("Location")
            food_type = st.selectbox("Food Type",["Non-Vegetarian","Vegan","Vegetarian"])
            meal_type = st.selectbox("Meal Type",["Breakfast","Dinner","Lunch","Snacks"])
            if st.button("Add Record"):
                data = {"Food_Name": food_name, "Quantity": quantity, "Expiry_Date": expiry_date,
                        "Provider_ID": provider_id, "Provider_Type": provider_type,
                        "Location": location, "Food_Type": food_type, "Meal_Type": meal_type}
                add_record(conn, selected_table, data)

        elif selected_table == "Claims":
            food_id = st.number_input("Food ID", step=1)
            receiver_id = st.number_input("Receiver ID", step=1)
            status = st.selectbox("Status",["Cancelled","Completed","Pending"])
            timestamp = st.date_input("Timestamp")
            if st.button("Add Record"):
                data = {"Food_ID": food_id, "Receiver_ID": receiver_id, "Status": status, "Timestamp": timestamp}
                add_record(conn, selected_table, data)

    elif operation == "Update":
    # if where_clause:
        if selected_table == "Providers":
            where_clause = st.number_input("provider_id",1)
            where = "provider_id ="+str(where_clause)
            column_options = ["Name", "Type", "Address", "City", "Contact"]
            column_to_update = st.selectbox("Select Column to Update", column_options)
            if column_to_update == "Type":
                new_value = st.selectbox("Type",["Catering Service","Grocery Store","Restaurant","Supermarket"])
            else:
                new_value = st.text_input(f"Enter New Value for {column_to_update}")
        elif selected_table == "Receivers":
            where_clause = st.number_input("receiver_id",1)
            where = "receiver_id ="+str(where_clause)
            column_options = ["Name", "Type", "City", "Contact"]
            column_to_update = st.selectbox("Select Column to Update", column_options)
            if column_to_update == "Type":
                new_value = st.selectbox("Type", ["Charity","Individual","NGO","Shelter"])
            else:
                new_value = st.text_input(f"Enter New Value for {column_to_update}")
        elif selected_table == "Food_Listings":
            where_clause = st.number_input("food_id",1)
            where = "food_id ="+str(where_clause)
            column_options = ["Food_Name", "Quantity", "Expiry_Date", "Provider_ID", "Provider_Type", "Location", "Food_Type", "Meal_Type"]
            column_to_update = st.selectbox("Select Column to Update", column_options)
            if column_to_update == 'Provider_Type':
                new_value = st.selectbox("Provider Type",["Catering Service","Grocery Store","Restaurant","Supermarket"])
            elif column_to_update == 'Food_Type':
                new_value = st.selectbox("Food Type",["Non-Vegetarian","Vegan","Vegetarian"])
            elif column_to_update == 'Meal_Type':
                new_value = st.selectbox("Meal Type",["Breakfast","Dinner","Lunch","Snacks"])
            else:
                new_value = st.text_input(f"Enter New Value for {column_to_update}")
        elif selected_table == "Claims":
            where_clause = st.number_input("claim_id",1)
            where = "claim_id ="+str(where_clause)
            column_options = ["Food_ID", "Receiver_ID", "Status", "Timestamp"]
            column_to_update = st.selectbox("Select Column to Update", column_options)
            if column_to_update == "Status":
                new_value = st.selectbox("Status",["Cancelled","Completed","Pending"])
                
            else:
                new_value = st.text_input(f"Enter New Value for {column_to_update}")

        

        if st.button("Update Record"):
            update_record(conn, selected_table, column_to_update, new_value, where)
            st.write(conn, selected_table, column_to_update, new_value, where)


    elif operation == "Delete":
        if selected_table == "Providers":
            where_clause = st.number_input("provider_id",1)
            where = "provider_id ="+str(where_clause)
            if where and st.button("Delete Record"):
                delete_record(conn, selected_table, where)
        elif selected_table == "Receivers":
            where_clause = st.number_input("receiver_id",1)
            where = "receiver_id ="+str(where_clause)
            if where and st.button("Delete Record"):
                delete_record(conn, selected_table, where)
        elif selected_table == "Claims":
            where_clause = st.number_input("claim_id",1)
            where = "claim_id ="+str(where_clause)
            if where and st.button("Delete Record"):
                delete_record(conn, selected_table, where)
        elif selected_table == "Food_Listings":
            where_clause = st.number_input("food_id",1)
            where = "food_id ="+str(where_clause)
            if where and st.button("Delete Record"):
                delete_record(conn, selected_table, where)
    conn.close()

if __name__ == "__main__":
    main()
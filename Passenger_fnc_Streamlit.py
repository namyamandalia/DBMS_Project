import streamlit as st
import mysql.connector
from datetime import datetime

# Function to insert passenger data into the database
def insert_passenger_data(name, address, sex, dob, phn, age, passport_no):
    try:
        # Establish a database connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="NAMYA@SQL2023",
            database="DBMS_PROJECT"
        )

        cursor = db.cursor()

        # Define the SQL query to insert passenger data
        insert_query = "INSERT INTO Passengers (Name, Address, Sex, DOB, PHN, Age, Passport_No) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        # Execute the SQL query with the provided data
        cursor.execute(insert_query, (name, address, sex, dob, phn, age, passport_no))

        # Commit the changes to the database
        db.commit()

        st.success("Passenger data added successfully.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    finally:
        db.close()

# Streamlit web app
st.title("Passenger Entry Form")

# Create form fields for passenger entry
name = st.text_input("Name")
address = st.text_input("Address")
sex = st.radio("Sex", ["Male", "Female"])
dob = st.date_input("Date of Birth")
phn = st.text_input("Phone Number")
age = st.number_input("Age", min_value=0)
passport_no = st.text_input("Passport Number")

if st.button("Add Passenger"):
    if name and address and dob and phn and age and passport_no:
        sex = 1 if sex == "Male" else 0
        insert_passenger_data(name, address, sex, dob, phn, age, passport_no)
        # Clear input fields
        name, address, sex, dob, phn, age, passport_no = "", "", "Male", dob, "", 0, ""
    else:
        st.warning("Please fill in all required fields.")

st.write("Note: Ensure that the MySQL database connection details and schema match your setup.")
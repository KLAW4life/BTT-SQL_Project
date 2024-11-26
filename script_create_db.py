"""
This file is the code that will create the databse, the table, read the data in the .csv, create a .sql file with the insert queries.
Upon Completion the data in the csv will be inserted into the database.

"""

import csv
import mysql.connector


import os
from dotenv import load_dotenv

# Get the database credentials
load_dotenv()


# Database connection configuration using environment variables
conn = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'auth_plugin': os.getenv('AUTH_PLUGIN')
}

cursor = conn.cursor()

print("Creating Database....")
# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS customers")

# Connect to exampledb database
conn.database = "customers"

print("Creating Customers Table....")
#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS Customers")

# Create table
cursor.execute("CREATE TABLE Customers (CustomerID int NOT NULL, Gender varchar(100) NOT NULL, Age int (100) NOT NULL, Annual_Income int NOT NULL, Spending_Score int (100) NOT NULL, Profession varchar(255) NOT NULL, Work_Experience int NOT NULL, Family_Size int NOT NULL)")

print("Reading data from .csv file....")
# Open the CSV file
with open('Customers.csv', 'r') as csvfile:
    
    # Create a CSV reader
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Extract the data from the row
        col1, col2, col3, col4, col5, col6, col7, col8 = row

        # Construct the SQL query
        query = "INSERT INTO Customers (CustomerID, Gender, Age, Annual_Income, Spending_Score, Profession, Work_Experience, Family_Size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # Execute the query
        cursor.execute(query, (col1, col2, col3, col4, col5, col6, col7, col8))

print("Fetching data....")
# Fetch all results from SELECT statement
cursor.execute("SELECT * FROM Customers")
result_set = cursor.fetchall()

print("Creating customers.sql file....")
# Write SQL commands to file
with open("customers.sql", "w") as f:
    for line in result_set:
        query = "INSERT INTO Customers (CustomerID, Gender, Age, Annual_Income, Spending_Score, Profession, Work_Experience, Family_Size) VALUES ({}, '{}', {}, {}, {}, '{}', {}, {});\n".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        f.write(query)

print("Database successfully created....")
# Commit changes and close connection
conn.commit()
conn.close()


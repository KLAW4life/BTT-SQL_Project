"""
This file creates the database, tables, reads data from .csv files, and generates a .sql file
with the INSERT queries for initializing the database.

"""

import csv
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables for database credentials
load_dotenv()

# Database connection configuration
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    auth_plugin=os.getenv('AUTH_PLUGIN')
)

cursor = conn.cursor()

print("Creating Database....")
# Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS University")

# Connect to the University database
conn.database = "University"

print("Creating Students Table....")
# Drop Students table if it exists
cursor.execute("DROP TABLE IF EXISTS Students")

# Create Students table
cursor.execute("""
    CREATE TABLE Students (
        StudentID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(100) NOT NULL,
        LastName VARCHAR(100) NOT NULL,
        Gender ENUM('Male', 'Female', 'Other') NOT NULL,
        Age INT NOT NULL,
        EnrollmentYear INT NOT NULL,
        Major VARCHAR(100)
    )
""")

print("Creating Courses Table....")
# Drop Courses table if it exists
cursor.execute("DROP TABLE IF EXISTS Courses")

# Create Courses table
cursor.execute("""
    CREATE TABLE Courses (
        CourseID INT AUTO_INCREMENT PRIMARY KEY,
        CourseName VARCHAR(255) NOT NULL,
        Department VARCHAR(100) NOT NULL,
        Credits INT NOT NULL,
        Semester VARCHAR(50) NOT NULL
    )
""")

print("Creating Enrollments Table....")
# Drop Enrollments table if it exists
cursor.execute("DROP TABLE IF EXISTS Enrollments")

# Create Enrollments table
cursor.execute("""
    CREATE TABLE Enrollments (
        EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
        StudentID INT NOT NULL,
        CourseID INT NOT NULL,
        Grade CHAR(2),
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
    )
""")

print("Reading and inserting data from CSV files....")

# Populate Students table
with open('Students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        query = "INSERT INTO Students (FirstName, LastName, Gender, Age, EnrollmentYear, Major) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, row)

# Populate Courses table
with open('Courses.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        query = "INSERT INTO Courses (CourseName, Department, Credits, Semester) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, row)

# Populate Enrollments table
with open('Enrollments.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        query = "INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES (%s, %s, %s)"
        cursor.execute(query, row)

print("Creating university.sql file....")
# Write SQL INSERT commands to file
with open("university.sql", "w") as f:
    # Students table
    cursor.execute("SELECT * FROM Students")
    results = cursor.fetchall()
    for row in results:
        f.write(f"INSERT INTO Students (FirstName, LastName, Gender, Age, EnrollmentYear, Major) VALUES ('{row[1]}', '{row[2]}', '{row[3]}', {row[4]}, {row[5]}, '{row[6]}');\n")

    # Courses table
    cursor.execute("SELECT * FROM Courses")
    results = cursor.fetchall()
    for row in results:
        f.write(f"INSERT INTO Courses (CourseName, Department, Credits, Semester) VALUES ('{row[1]}', '{row[2]}', {row[3]}, '{row[4]}');\n")

    # Enrollments table
    cursor.execute("SELECT * FROM Enrollments")
    results = cursor.fetchall()
    for row in results:
        f.write(f"INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES ({row[1]}, {row[2]}, '{row[3]}');\n")

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
print("Database setup complete! SQL commands saved to university.sql.")

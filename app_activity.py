"""
@File    :  app.py
@Time    :  26/11/2024
@Author  :  Your Name
@Version :  1.1
@Desc    : This program is a FLASK API implementation for simplified University database queries.
"""

from flask import Flask, make_response
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection configuration using environment variables
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'auth_plugin': os.getenv('AUTH_PLUGIN')
}


@app.route('/students', methods=['GET'])
def get_all_students():
    """Query 1: Retrieve all students enrolled in the university."""
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        query = "-------------------------------------------------------------------"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return make_response(results, 200)

    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/courses/mathematics', methods=['GET'])
def get_mathematics_courses():
    """Query 2: Find all courses offered by the 'Mathematics' department."""
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        query = "-------------------------------------------------------------------"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return make_response(results, 200)

    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/students/under-21', methods=['GET'])
def get_students_under_21():
    """Query 3: List all students who are under 21 years old."""
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        query = "-------------------------------------------------------------------"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return make_response(results, 200)

    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/courses/3-credits', methods=['GET'])
def get_courses_with_3_or_more_credits():
    """Query 4: Find all courses with 3 or more credits."""
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        query = "-------------------------------------------------------------------"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return make_response(results, 200)

    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/students/count', methods=['GET'])
def count_total_students():
    """Query 5: Count the total number of students enrolled in the university."""
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor(dictionary=True)
        query = "-------------------------------------------------------------------"
        cursor.execute(query)
        results = cursor.fetchone()
        cursor.close()
        cnx.close()
        return make_response(results, 200)

    except Exception as e:
        return make_response({'error': str(e)}, 400)


if __name__ == '__main__':
    app.run(debug=True)

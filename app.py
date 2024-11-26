"""
@File    :  app.py
@Time    :  19/03/2023
@Author  :  Kerene Wright
@Version :  1.0
@Desc    : This program is a FLASK API implementation for the Customers database 

"""
from flask import Flask, request, make_response

import mysql.connector
import os
from dotenv import load_dotenv

# Get the database credentials
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

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute('Enter code here') # SQL Query that selects all customers from the Customers table
        customers_list = []

        for CustomerID, Gender, Age, Annual_Income, Spending_Score, Profession, Work_Experience, Family_Size in cursor:
            customers = {}
            customers['Id'] = CustomerID
            customers['Gender'] = Gender
            customers['Age'] = Age
            customers['Annual Income'] = Annual_Income
            customers['Spending Score'] = Spending_Score
            customers['Profession'] = Profession
            customers['Work Experience'] = Work_Experience
            customers['Family Size'] = Family_Size

            customers_list.append(customers)
        cursor.close()
        cnx.close()
        return make_response(customers_list, 200)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)


@app.route('/customer/<customer_id>', methods=['GET'])
def get_customers_id(customer_id):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute(f"Enter code here. DO NOT DELETE->{customer_id};") #SQL code that selects a customer by their ID.
        row = cursor.fetchone()
        customers = {}

        if row is not None:
            CustomerID, Gender, Age, Annual_Income, Spending_Score, Profession, Work_Experience, Family_Size = row
            customers = {}
            customers['Id'] = CustomerID
            customers['Gender'] = Gender
            customers['Age'] = Age
            customers['Annual Income'] = Annual_Income
            customers['Spending Score'] = Spending_Score
            customers['Profession'] = Profession
            customers['Work Experience'] = Work_Experience
            customers['Family Size'] = Family_Size
            cursor.close()
            cnx.close()
            return make_response(customers, 200)
        else:
            return make_response({'error': 'Customer not found'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)


@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        #json way of accepting data
        content = request.json
        CustomerID = content['CustomerID']
        Gender = content['Gender']
        Age = content['Age']
        Annual_Income = content['Annual_Income']
        Spending_Score = content['Spending_Score']
        Profession = content['Profession']
        Work_Experience = content['Work_Experience']
        Family_Size = content['Family_Size']


        cursor.execute(f"Enter Code here ") #SQl Code that enters values into the Customers table.
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success" : "Customer added"}, 200)
    
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured when adding a customer'}, 400)
    
@app.route('/update_profession/<customer_id>', methods=['PUT'])
def update_profession_id(customer_id):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        #json way of accepting data
        content = request.json
        Profession = content['Profession']

        cursor.execute(f"Enter code here.") #SQL code that updates the profession of a customer by their ID.
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success" : "Profession Updated"}, 200)
    
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
# can use a sub query to get the highest and then use the query to match to the customer id
@app.route('/highest_income_report', methods=['GET'])
def profession_highest_income():
    try:
        
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        
        cursor.execute(f"Enter Code here") #SQL code that gets the highest income by profession.
        customers_list = []

        for CustomerID, AnnualIncome, Profession in cursor:
            customers = {}
            customers['CustomerID'] = CustomerID
            customers['AnnualIncome'] = AnnualIncome
            customers['Profession'] = Profession

            customers_list.append(customers)
        cursor.close()
        cnx.close()
        return make_response(customers_list, 200)
    
    except:
        return make_response({'error': 'An error has occured when retrieving highest income by profession'}, 400)
    


@app.route('/total_income_report', methods=['GET'])
def get_income_report():
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        cursor.execute('Enter Code here') #SQL code that gets the total income by profession.
        customers_list = []

        for TotalIncome, Profession in cursor:
            customers = {}
            customers['TotalIncome'] = TotalIncome
            customers['Profession'] = Profession

            customers_list.append(customers)
        cursor.close()
        cnx.close()
        return make_response(customers_list, 200)
    
    except:
        return make_response({'error': 'An error has occured when retrieving total income report by profession'}, 400)
     

@app.route('/average_work_experience', methods=['GET'])
def avg_work_experience():
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        cursor.execute(f"Enter Code here") #SQL code that gets the average work experience by profession where the icome is more that $50,000 and the age is less than 35.
        customers_list = []

        for AVGExperience, Profession in cursor:
            customers = {}
            customers['AVGExperience'] = AVGExperience
            customers['Profession'] = Profession

            customers_list.append(customers)
        cursor.close()
        cnx.close()
        return make_response(customers_list, 200)
    
    except Exception as e:
        return make_response({'error': 'An error has occured when getting the average work experience by profession'}, 400)
    

@app.route('/average_spending_score/<profession>', methods=['GET'])
def avg_spend_score(profession):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        cursor.execute(f"Enter Code here ") #SQL code that gets the average spending for entered profession and their gender. 
        customers_list = []

        for AVG_SpendScore, Gender in cursor:
            customers = {}
            customers['AVG_SpendScore'] = AVG_SpendScore
            customers['Gender'] = Gender

            customers_list.append(customers)
        cursor.close()
        cnx.close()
        return make_response(customers_list, 200)
    
    except Exception as e:
        return make_response({'error': 'An error has occured when getting the average spending score by gender'}, 400)

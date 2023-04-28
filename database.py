pip install sqlite3
import sqlite3

conn = sqlite3.connect('employees.db')

conn.execute('CREATE TABLE employees (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate DATE)')

print("Table created successfully")

conn.close()

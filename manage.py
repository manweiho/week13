from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_employee():
   return render_template('employee.htm')


@app.route('/registration',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         id = request.form['id']
         name = request.form['nm']
         gender = request.form['g']
         phone = request.form['phone']
         birthdate = request.form['date']
         
         with sql.connect("employees.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employees (EmpID,EmpName,EmpGender,EmpPhone,EmpBdate) VALUES ('{0}','{1}','{2}','{3}',{4}')".format(id,nm,g,phone,date)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

@app.route('/information')
def information():
   con = sql.connect("employees.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from employees")
   
   rows = cur.fetchall(); 
   return render_template("information.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

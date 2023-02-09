from flask import Flask, request, render_template, jsonify, json
from flaskext.mysql import MySQL #pip install flask-mysql
import pymysql
  
app = Flask(__name__)

mysql = MySQL()
   
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Shanu@123'
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)

def totalrecord():
    cursor.execute("select count(*) as allcount from employee")
    rsallcount = cursor.fetchone()
    return rsallcount

def totalrecordfilter(likeString):
    cursor.execute("SELECT count(*) as allcount from employee WHERE name LIKE %s OR position LIKE %s OR office LIKE %s", (likeString, likeString, likeString))
    rsallcount = cursor.fetchone()
    return rsallcount

def emptysearch(row, rowperpage):
    cursor.execute("SELECT * FROM employee ORDER BY name asc limit %s, %s;", (row, rowperpage))
    employeelist = cursor.fetchall()
    print(employeelist)
    return employeelist

def valuesearch(likeString, row, rowperpage):
    cursor.execute("SELECT * FROM employee WHERE name LIKE %s OR position LIKE %s OR office LIKE %s limit %s, %s;", (likeString, likeString, likeString, row, rowperpage))
    employeelist = cursor.fetchall()
    return employeelist

def insertjson():
    cursor.execute("SELECT * FROM employee") 
    json_file =  cursor.fetchall()
    json_data = json.dumps(json_file)
    with open("fortest.json", "w") as outfile:
        outfile.write(json_data)

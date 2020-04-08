from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
import os
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
Bootstrap(app)

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!@aA123456'
# app.config['MYSQL_DB'] = 'my_database'
app.config['MYSQL_DB'] = 'employee_data'
# data get dict
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    cur = mysql.connection.cursor()
    if cur.execute("INSERT INTO user(user_name) VALUES('Nasir')"):
        mysql.connection.commit()
        return 'success', 201
    '''
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        cur = mysql.connection.cursor()
        name = generate_password_hash(name)
        cur.execute("INSERT INTO employee(name, age) VALUES(%s, %s)", (name, age))
        mysql.connection.commit()
    return render_template('employee.html')

@app.route('/employees')
def employees():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        employees = cur.fetchall()
        session['username'] = employees[0]['name']
        return str(check_password_hash(employees[0]['name'], 'sunday'))
    # return render_template('employees.html', employees=employees)

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

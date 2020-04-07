from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!@aA123456'
app.config['MYSQL_DB'] = 'my_database'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    if cur.execute("INSERT INTO user(user_name) VALUES('Nasir')"):
        mysql.connection.commit()
        return 'success', 201
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

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
    result_value = cur.execute("SELECT * FROM user")
    if result_value > 0:
        users = cur.fetchall()
        print(users)

    if request.method == 'POST':
        # return 'Successfully registered'
        return request.form['password']


    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    fruits = ['Apple', '', 'Orange']
    return render_template('index.html', fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

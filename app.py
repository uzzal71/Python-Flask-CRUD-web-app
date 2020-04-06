from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ['Apple', '', 'Orange']
    return render_template('index.html', fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

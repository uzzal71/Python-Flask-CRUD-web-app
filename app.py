from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi!"

if __name__ == '__main__':
    app.run(debug=True) # also define a port app.run(debug=True, port=50001)

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Dockerized Flask App!'

@app.route('/{name}')
def hello_name(name):
    return 'Hello, {}!'.format(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.debug=True
    app.run("127.0.0.1", 3000)
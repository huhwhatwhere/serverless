#!/usr/bin/env python
from flask import Flask, current_app

app = Flask(__name__)

@app.route('/')
def index():
    return current_app.send_static_file('index.html')

# We only need this for local development.
if __name__ == '__main__':
    app.run()

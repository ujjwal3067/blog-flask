#!/usr/bin/env python3

from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {"username": "ujjwal"}
    return "<h1>hello world</h1>"

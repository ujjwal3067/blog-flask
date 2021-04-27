#!/usr/bin/env python3

'''
routing functions for URL routing
views based on URL request
'''

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "ujjwal"}
    posts = [
        {
            'author': {'username' : 'emma'} ,
            'body': "beutiful day is portland"
        },
        {
            'author': {'username': 'mark'} ,
            'body': "The avengers movie was so cool"
        }
    ]
    return render_template('index.html', title= 'Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm() # create new form object
    return render_template('login.html', title='Sign In', form = form )

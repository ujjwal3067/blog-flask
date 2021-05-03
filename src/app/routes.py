#!/usr/bin/env python3

'''
->  Routing functions for URL routing
->  Views based on URL request

'''

from flask import render_template, flash, redirect , url_for
from app import app
from app.forms import LoginForm

#VIEW 1
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

#VIEW 2
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm() # create new form object

    if form.validate_on_submit(): # if POST request
        flash("Login requested for user {}, remember_me={}",format(
            form.username.data, form.remember_me.data))


        # index  = view function name
        # redirect to different url
        return redirect(url_for('index'))

    # if GET request : show the form again
    # because this view function only accepts POST request to process form data
    return render_template('login.html', title='Sign In', form = form )

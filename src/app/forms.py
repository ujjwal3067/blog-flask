#!/usr/bin/env python3

from flask_wtf import FlaskFrom
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# inherits FlaskFrom
class LoginForm(FlaskForm):
    username    = StringField("Username", validators = [DataRequired()])
    password    = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit      = SubmitField("Sign in")

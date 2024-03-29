#!/usr/bin/env python3

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# user inherits db.Model class
class User(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(64), index = True, unique = True)
    email           = db.Column(db.String(120), index = True, unique = True)
    password_hash   = db.Column(db.String(128))
    posts           = db.relationship("Post", backref = "author", lazy = "dynamic")


    def __repr__(self):
        return '<User {}>'.format(self.username)

    # set's a new password hash for the user
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check if the password inputed  is correct ( compares with password_hash )
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    body            = db.Column(db.String(140))
    timestamp       = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post  {}>'.format(self.body)

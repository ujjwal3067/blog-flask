#!/usr/bin/env python3


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy(app)
# represents the migrate engine
migrate = Migrate(app, db)

# routes : routing engine
# modules: defines structure of the database
from app import routes  , models

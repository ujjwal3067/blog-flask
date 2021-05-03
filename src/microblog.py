#!/usr/bin/env python3

from app import app , db
from app.models import User , Post

# config for flask shell commands
@app.shell_context_processor
def  make_shell_context():
    return { 'db' : db,  "User" : User ,  "Post" : Post }

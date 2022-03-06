# Creating database models
from . import db
# This is custom class that we can inherrit, gives our user object specific for our flask login
# The user object needs to inherrit from UserMixin
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # defining all columns we want to have stored in this table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique=True means that email has one to one rel
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))





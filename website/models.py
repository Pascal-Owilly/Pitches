# Creating database models
from . import db
# This is custom class that we can inherrit, gives our user object specific for our flask login
# The user object needs to inherrit from UserMixin
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    # associateng different information to different users (setting up relationship between class and user object)
    # We do this in the form of a foreign key (a key that alwaysreferences a column of another database)
    # It stores the id of one of the users who created the note
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Foreign key shows that we must pass a valid of an existing user to this column - one-many rel 


class User(db.Model, UserMixin):
    # defining all columns we want to have stored in this table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique=True means that email has one to one rel
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #   then define class ⬆️
    #   we are telling sqlalchemy to find a class and add note to the id everytime we create a note 
    #   Making all the users to be able to find all of their notes
    notes = db.relationship('Note')

    # Creating this database inside dander init file
    

    



 
from flask import Blueprint, render_template
# import render template

views = Blueprint('views', __name__)

# register the blueprint inside init.py
@views.route('/')
def home():
    return render_template("home.html") 


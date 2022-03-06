
from unicodedata import category
from flask import Blueprint, render_template, request, flash
# from . import db
# request will get the form data
# Import flash will show the validation message


auth = Blueprint('auth', __name__)

# defining login, logout, signup
@auth.route('/login', methods=['GET', 'POST']) # With GET nad POST requests we are able to accept get and post requests from this route
def login():   

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h3>You are loged out"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signin():

    # getting user info and storing in the database for creating their accounts
    # differentiate between get request and post request
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checking if the information is valid
   
        if len(email) < 4:
            flash('email is too short.', category='error')
        elif len(firstName) < 2:
            flash('first name is too short, enter atleat 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords don not match', category='error')
        elif len(password1) < 7:
            flash('Passwords shoud be atleast 8 ccharacters', category='error')
        else:
            flash('Account created successfully!', category='success')    

        # if all the conditions are met we add the user to the database
    return render_template("sign_up.html")


from flask import Blueprint, render_template, request
# request will get the form data


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
        firstName.request.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checking if the information is valid
   
        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass

        # if all the conditions are met we add the user to the database




    return render_template("sign_up.html")

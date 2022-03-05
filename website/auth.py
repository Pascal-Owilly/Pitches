
from flask import Blueprint, render_template, request
# request will get the form data


auth = Blueprint('auth', __name__)

# defining login, logout, signup
@auth.route('/login', methods=['GET', 'POST']) # With GET nad POST requests we are able to accept get and post requests from this route
def login():
   
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h3>You are loged out"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signin():
    return render_template("sign_up.html")

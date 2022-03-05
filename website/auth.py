from cgitb import text
from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

# defining login, logout, signup
@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h3>You are loged out"

@auth.route('/sign-up')
def signin():
    return render_template("sign_up.html")

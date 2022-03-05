from flask import Blueprint


auth = Blueprint('auth', __name__)

# defining login, logout, signup
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signin():
    return "<p>Sign up</p>"

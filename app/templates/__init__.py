# set up flask app
from flask import Flask

# Initializing app
def create_app():
    app = Flask(__name__) # __name__ reps the name of our app
    app.config['SECRET_KEY'] = 'abc123' #will encript/secure cookies or session data related to our website

    return app

 
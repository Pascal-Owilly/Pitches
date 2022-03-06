from flask import Flask
# Setting up database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, template_folder='../templates') # debugging template not found error
    app.config['SECRET_KEY'] = 'abc123'
    # Telling flask that we are using DB_NAME database and where it will be located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # telling flask we have different appllucation containing blueprint 
    from website.views import views
    from website.auth import auth

    # After importing the blueprintd we register them with flask app
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    

    return app

    
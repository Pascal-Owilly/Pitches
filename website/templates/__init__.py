from flask import Flask
# Setting up database
from flask_sqlalchemy import SQLAlchemy
# We use this path module to determine whether or not path exists
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, template_folder='../templates') # debugging template not found error
    app.config['SECRET_KEY'] = 'abc123'
    # Telling flask that we are using DB_NAME database and where it will be located using sqlite
    # It will store the database inside the app folder
    # f string only works in python3.6 and above
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initializing the database
    db.init_app(app)
    # defining database models


    # telling flask we have different appllucation containing blueprint 
    from website.views import views
    from website.auth import auth

    # After importing the blueprintd we register them with flask app
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    # writing script that will checks everytime if we have created the database
    # The .models ensures the models.py runs before we initialize or create our database

    from website.models import User, Note
    
    # returning create app database
  

    
    return app

    def create_database(app):
        # This checks if the database already exists and if not creates it
        # So we import path from os then use it
        if not path.exists('website/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database!')

    create_database(app)        


    
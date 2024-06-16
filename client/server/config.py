from flask import Flask
from flask_sqlalchemy import SQLAlchemy # used to store data in the db.
from flask_cors import CORS # used to send request to the backend from a different URL(frontend) for security.

app = Flask(__name__) # initializes flask application.
CORS(app) # blocks CORS errors that occur when sending requests from backend to frontend.

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///profile.db" # initialize database connection and name of db.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Disable changes to database from getting tracked.


db = SQLAlchemy(app) # Database instance which gives me access to the database connection from ("sqlite:///profile.db")
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
UPLOAD_FOLDER =  "./app/static/uploads"
os.environ['DATABASE_URL'] ='postgres://ftgijimruwxgpb:2c5273399058f0ad0d4b04e7bdbcfeb750386af136d97845930ebfeb11416d94@ec2-52-207-93-32.compute-1.amazonaws.com:5432/d8aq5jfdrr6thn'

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ftgijimruwxgpb:2c5273399058f0ad0d4b04e7bdbcfeb750386af136d97845930ebfeb11416d94@ec2-52-207-93-32.compute-1.amazonaws.com:5432/d8aq5jfdrr6thn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.from_object(__name__)
from app import views

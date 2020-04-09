from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
UPLOAD_FOLDER =  "./app/static/uploads"

app = Flask(__name__)

app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xmhmzjtroxlkai:6774b90ded624cfc4742e23ab8d501420fbedf369c73b613f3a4c0a127078e40@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d548gt6u5v15ma"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.from_object(__name__)

from app import views

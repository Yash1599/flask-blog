from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '921f199b9ccaa71c937d21beebeec552'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///website.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manage = LoginManager(app)

from webblog import routes
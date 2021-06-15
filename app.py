from flask import Flask
from flask_login import LoginManager
import os

core = Flask(__name__)
core.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
core.config['SECRET_KEY'] = 'OyEYHsMZ7kZIKfr/09DkSPR941U02eBjzoGlL83AepE='

login_manager = LoginManager()
login_manager.init_app(core)
login_manager.login_view = 'loginPage'


if os.path.isdir('install'):
    import install
    

import base, Admin, Accounts
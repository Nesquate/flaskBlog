from flask import Flask
import os

core = Flask(__name__)
core.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

if os.path.isdir('install'):
    import install
    

import base, Admin
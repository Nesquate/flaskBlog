from flask import Flask

core = Flask(__name__)
core.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

import base, install
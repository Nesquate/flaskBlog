from flask_sqlalchemy import SQLAlchemy
from app import core

db = SQLAlchemy(core)
db.init_app(core)

from database.models import Posts, Pages, Site, Tags, Categories, relations
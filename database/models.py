from database.db import db
from app import login_manager
from flask_login import UserMixin, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

relations = db.Table(
    'relations',
    db.Column('postid_rt', db.Integer, db.ForeignKey('posts.id', prinmary_key=True)),
    db.Column('tagid_rt', db.Integer, db.ForeignKey('tags.id', primary_key=True))
)

# Site Information Datas
class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=True)
    description = db.Column(db.String(), unique=True, nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Page Information Datas
class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)

    def __init__(self, name ,description, content):
        self.name = name
        self.description = description
        self.content = content

# Post Information Datas
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)
    tags = db.relationship('Tags', secondary=relations, backref=db.backref('tag'))
    categories = db.Column(db.Integer(), db.ForeignKey('categories.id'), nullable=True)
    author = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=True)

    def __init__(self, name, description, content):
        self.name = name
        self.description = description
        self.content = content
        # self.tag = tag
        # self.category = category

# Categories Information Datas
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.relationship('Posts', backref='category', lazy=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Tags Information Datas
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description


# Admin Information Datas

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.relationship('Posts', backref='user', lazy=True)
    account = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)
    introduction= db.Column(db.String(), nullable=True)

    def __init__(self, account, password):
        self.account = account
        self.password_hash = generate_password_hash(password)

    def change_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
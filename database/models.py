from database.db import db

relations = db.Table(
    'relations',
    db.Column('postid_rt', db.Integer, db.ForeignKey('posts.id', prinmary_key=True)),
    db.Column('tagid_rt', db.Integer, db.ForeignKey('tags.id', primary_key=True))
)

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=True)
    description = db.Column(db.String(), unique=True, nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)

    def __init__(self, name ,description, content):
        self.name = name
        self.description = description
        self.content = content


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)
    tags = db.relationship('Tags', secondary=relations, backref=db.backref('tag'))
    categories = db.Column(db.Integer(), db.ForeignKey('categories.id'), nullable=True)

    def __init__(self, name, description, content, tag, category):
        self.name = name
        self.description = description
        self.content = content
        self.tag = tag
        self.category = category

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.relationship('Posts', backref='category', lazy=True)
    name = db.Column(db.String(), nullable=False)
    descrpitpin = db.Column(db.String(), nullable=True)

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
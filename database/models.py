from database.db import db

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

    def __init__(self, id, name, description, content):
        self.id = id
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
    descrpitpin = db.Column(db.String(), nullable=True)

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.descrpitpin = description

# Tags Information Datas
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


# Admin Information Datas
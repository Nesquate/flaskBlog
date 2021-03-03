from flask import Flask, render_template, url_for, escape, redirect, abort
from flask_sqlalchemy import SQLAlchemy
core = Flask(__name__)
core.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(core)
db.init_app(core)

class Site(db.Model):
    __tablename__ = 'site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=True)
    description = db.Column(db.String(), unique=True, nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)

    def __init__(self, name ,description, content):
        self.name = name
        self.description = description
        self.content = content


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String(), nullable=True)
    content = db.Column(db.String(), nullable=True)
    tag = db.Column(db.String(), nullable=True)
    category = db.Column(db.String(), nullable=True)

    def __init__(self, name, description, content, tag, category):
        self.name = name
        self.description = description
        self.content = content
        self.tag = tag
        self.category = category

@core.route('/')
def home():
    posts = Post.query.all()
    siteInfo = Site.query.first()
    # print(type(siteInfo))
    if posts:
        return render_template('post.html', siteData=siteInfo, postData=posts)
    else:
        abort(404)
    # return 'OK'

@core.route('/post/<int:postid>')
def postPage(postid):
    anPost = Post.query.filter_by(id=postid).first()
    siteInfo = Site.query.first()
    if anPost:
        return render_template('post.html', siteData=siteInfo, post=anPost)
    else:
        abort(404)

@core.route('/post')
@core.route('/categorie')
@core.route('/tag')
def returnToHome():
    return redirect(url_for('home'))

@core.route('/tag/<tag>')
def tagPage(tag):
    return 'Now tag is :' + escape(tag)

@core.route('/category/<category>')
def categoryPage(category):
    return 'Now category is : ' + escape(categories)

@core.route('/search')
def search():
    siteInfo = Site.query.first()
    return render_template('search.html', siteData=siteInfo)

@core.route('/search/<keyword>')
def search_result(keyword):
    return 'result of ' + escape(keyword) + ' : '

@core.route('/install')
def dbCreate():
    db.create_all()
    return 'You can check if data.db exist or not.'
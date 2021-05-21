from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db
from os import path

@core.route('/')
def home():
    if path.isfile('data.db'):
        posts = db.Posts.query.all()
        return render_template('post.html', db=db, posts=posts)
    else:
        return 'Database not found, maybe you need to run /install first.'
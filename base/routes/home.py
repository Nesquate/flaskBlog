from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/')
def home():
    posts = db.Posts.query.all()
    return render_template('post.html', db=db, posts=posts)
from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/')
def home():
    siteInfo = db.Site.query.first()
    posts = db.Posts.query.all()
    if posts:
        return render_template('post.html', siteData=siteInfo, postData=posts)
    else:
        return render_template('post.html', siteData=siteInfo)
from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/post/<int:postid>')
def postPage(postid):
    siteInfo = db.Site.query.first()
    # Query post by post id
    anPost = db.Posts.query.filter_by(id=postid).first()
    # Query all tags by post
    tags = db.Posts.query.filter_by(id=postid).first().tags
    if anPost:
        return render_template('post.html', siteData=siteInfo, post=anPost, tags=tags)
    else:
        abort(404)
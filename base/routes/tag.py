from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/tag/<tag>')
def tagPage(tag):
    siteInfo = db.Site.query.first()
    # Query tag by tag id
    anTag = db.Tags.query.filter_by(id=tag).first()
    # Query any posts by tag == post.tags
    postsByTag = db.Posts.query.filter(db.Posts.tags.any(id=tag)).all()
    if anTag:
        return render_template('tag.html', siteData=siteInfo, tag=anTag, postData=postsByTag)
    else:
        abort(404)
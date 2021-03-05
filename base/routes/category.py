from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/category/<category>')
def categoryPage(category):
    siteInfo = db.Site.query.first()
    # Query result contents post id, so don't need other query
    anCategory = db.Categories.query.filter_by(id=category).first()
    if anCategory:
        return render_template('category.html', siteData=siteInfo, category=anCategory, postData=anCategory.postid)
    else:
        abort(404)
    # return '0'
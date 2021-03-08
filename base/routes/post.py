from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/post/<int:postid>')
def postPage(postid):
    # Query post by post id
    postData = db.Posts.query.filter_by(id=postid).first()
    if postData:
        return render_template(
            'post.html', 
            db=db, 
            postData=postData
        )
    else:
        abort(404)
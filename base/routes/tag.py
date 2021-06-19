from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db, models

@core.route('/tag/<tag>')
def tagPage(tag):
    # Query tag by tag id
    tagData = db.Tags.query.filter_by(id=tag).first()
    if tagData:
        return render_template(
            'tag.html', 
            db=db,
            tagData=tagData,
            models=models
        )
    else:
        abort(404)
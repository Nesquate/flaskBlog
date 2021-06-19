from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db, models

@core.route('/category/<category>')
def categoryPage(category):
    # Query result contents post id, so don't need other query
    categoryData = db.Categories.query.filter_by(id=category).first() 
    if categoryData:
        return render_template(
            'category.html', 
            db=db,
            categoryData=categoryData,
            models=models
        )
    else:
        abort(404)
    # return '0'
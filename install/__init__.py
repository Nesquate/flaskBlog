from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db,models

@core.route('/install')
def dbCreate():
    db.db.create_all()

    # Create test datas
    siteInfo =  models.Site('Test Site', 'An Test Site')
    firstCategory = models.Categories(1, 'Uncategorized', 'Uncategorized post is here')
    firstTag = models.Tags(1,'FirstTag', 'This is first tag')
    firstPost = models.Posts(1, 'First Post', 'First', 'This is first post')

    db.db.session.add_all([siteInfo, firstCategory, firstTag, firstPost])
    db.db.session.commit()

    ## Create category, tag and post relationship
     
    firstPost.categories = 1
    firstPost.tags = [firstTag]
    db.db.session.commit()

    return 'You can check if data.db exist or not.'
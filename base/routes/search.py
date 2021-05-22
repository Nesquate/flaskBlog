import re
from flask import render_template, url_for, escape, request
from werkzeug.utils import redirect 
from app import core
from database import db

@core.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.values['keyword']
        result = keyword
        result = '%{}%'.format(result) # Need '%' to use LIKE search
        post = db.Posts.query.filter(
            db.Posts.name.like(result)
        ).all()
        tag = db.Tags.query.filter(
            db.Tags.name.like(result)
        ).all()
        category = db.Categories.query.filter(
            db.Categories.name.like(result)
        ).all()

        if (len(post) == 0 and len(post) == 0) and len(category) == 0:
            return render_template('search_result.html', db=db, keyword=keyword)
        else:
            # Merge post title and url
            postDict = dict()
            for postItem in post:
                url = url_for('postPage', postid=postItem.id)
                postDict[postItem.name] = url
            
            tagDict = dict()
            for tagItem in tag:
                url = url_for('tagPage', tag=tagItem.id)
                tagDict[tagItem.name] = url
            
            categoryDict = dict()
            for categoryItem in category:
                url = url_for('categoryPage', category=categoryItem.id)
                categoryDict[categoryItem.name] = url
            
            result = list()
            result.append(postDict)
            result.append(tagDict)
            result.append(categoryDict)
            print(result)
            return render_template('search_result.html', db=db, result=result, keyword=keyword)
    return render_template('search.html', db=db)
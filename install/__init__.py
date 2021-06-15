from flask import render_template, url_for, escape, redirect, abort, request
from app import core
from database import db,models

@core.route('/install', methods=['GET', 'POST'])
def installPage():
    if request.method == "POST":
        siteName = request.form['name']
        siteDescription = request.form['description']
        account = request.form['account']
        password = request.form['password']
        dbCreate(siteName, siteDescription, account, password)
        return redirect('/')

    return render_template("install/index.html")

def dbCreate(siteName, siteDescription, account, password):
    db.db.create_all()

    # Create User
    admin = models.Users(account, password)
    admin.name = ""
    admin.introduction = ""
    print(admin)
    db.db.session.add(admin)
    db.db.session.commit()

    # Create test datas
    siteInfo =  models.Site(siteName, siteDescription)
    firstCategory = models.Categories('Uncategorized', 'Uncategorized post is here')
    firstTag = models.Tags('FirstTag', 'This is first tag')
    firstPost = models.Posts('First Post', 'First', 'This is first post')

    db.db.session.add_all([siteInfo, firstCategory, firstTag, firstPost])
    db.db.session.commit()

    ## Create category, tag and post relationship
     
    firstPost.categories = 1
    firstPost.author = admin.id
    firstPost.tags = [firstTag]
    db.db.session.commit()
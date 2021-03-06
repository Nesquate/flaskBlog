from flask import render_template, url_for, escape, redirect, abort, request
from flask_login.utils import login_required, current_user
from app import core
from database import db, models

@core.route('/admin/posts', methods=['GET', 'POST'])
@login_required
def adminPosts():
    status = 0
    if request.method == 'POST':
        print(request.form)
        status = delPost(request.form['delPost'])
        postsList = db.Posts.query.all()
        return render_template('admin/posts/posts.html', postsList=postsList, status=status)
    postsList = db.Posts.query.order_by(models.Posts.id.desc()).all()
    return render_template('admin/posts/posts.html', postsList=postsList)

@core.route('/admin/posts/new', methods=['GET', 'POST'])
@login_required
def newPost():
    if request.method == 'POST':
        print(request.form.getlist('tag'))
        post = models.Posts(name=request.form['title'], description=request.form['description'], content=request.form['content'])
        post.categories = request.form['category']

        tagList = list()
        for tagid in request.form.getlist('tag'):
            tag = db.Tags.query.filter_by(id=tagid).first()
            tagList.append(tag)
        post.tags = tagList
        post.author = current_user.id
        db.db.session.add(post)
        db.db.session.commit()
        return redirect(url_for('adminPosts'))
    categories = db.Categories.query.all()
    tags = db.Tags.query.all()
    return render_template('admin/posts/newpost.html', categoriesList=categories, tagsList=tags)

@core.route('/admin/posts/edit/<int:postid>', methods=['GET', 'POST'])
@login_required
def editPost(postid):
    if request.method == 'POST':
        print(request.form.getlist('tag'))
        post = db.Posts.query.filter_by(id=postid).first()
        print(post.id)
        post.name = request.form['title']
        post.description = request.form['description']
        post.content = request.form['content']
        post.categories = request.form['category']

        tagList = list()
        for tagid in request.form.getlist('tag'):
            tag = db.Tags.query.filter_by(id=tagid).first()
            tagList.append(tag)
        post.tags = tagList

        db.db.session.commit()
        return redirect(url_for('adminPosts'))
    post = db.Posts.query.filter_by(id=postid).first()
    print(post.categories)
    print(post.tags)
    categories = db.Categories.query.all()
    tags = db.Tags.query.all()
    return render_template('admin/posts/editpost.html', categoriesList=categories, tagsList=tags, post=post)

def delPost(postID):
    if db.Posts.query.filter_by(id=postID).first() is None:
        return -1
    else:
        post = db.Posts.query.filter_by(id=postID).first()
        db.db.session.delete(post)
        db.db.session.commit()
        return 1
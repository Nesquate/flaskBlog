from flask import render_template, url_for, escape, redirect, abort, request
from flask_login.utils import login_required
from app import core
from database import db, models

@core.route('/admin/tags', methods=['GET', 'POST'])
@login_required
def adminTags():
    status = 0
    if request.method == 'POST':
        print(request.form)
        status = delTag(request.form['delTag'])
        tagsList = db.Tags.query.all()
        return render_template('admin/tags/tags.html', tagsList=tagsList, status=status)
    tagsList = db.Tags.query.all()
    return render_template('admin/tags/tags.html', tagsList=tagsList)

@core.route('/admin/tags/new', methods=['GET', 'POST'])
@login_required
def newTag():
    if request.method == 'POST':
        print(request.form)
        tag = models.Tags(name=request.form['title'], description=request.form['description'])
        db.db.session.add(tag)
        db.db.session.commit()
        return redirect(url_for('adminTags'))
    tags = db.Tags.query.all()
    return render_template('admin/tags/newtag.html', tagsList=tags)

@core.route('/admin/tags/edit/<int:tagid>', methods=['GET', 'POST'])
@login_required
def editTag(tagid):
    if request.method == 'POST':
        print(request.form.getlist('tag'))
        tag = db.Tags.query.filter_by(id=tagid).first()
        print(tag.id)
        tag.name = request.form['title']
        tag.description = request.form['description']

        db.db.session.commit()
        return redirect(url_for('adminTags'))
    tag = db.Tags.query.filter_by(id=tagid).first()
    return render_template('admin/tags/edittag.html', tag=tag)

def delTag(tagID):
    print(db.Tags.query.filter_by(id=tagID).first() )
    if db.Tags.query.filter_by(id=tagID).first() is None:
        return -1
    else:
        tag = db.Tags.query.filter_by(id=tagID).first()
        db.db.session.delete(tag)
        db.db.session.commit()
        return 1

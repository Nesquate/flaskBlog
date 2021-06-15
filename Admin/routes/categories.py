from flask import render_template, url_for, escape, redirect, abort, request
from app import core
from database import db, models

@core.route('/admin/categories', methods=['GET', 'POST'])
def adminCategories():
    status = 0
    if request.method == 'POST':
        print(request.form)
        status = delTag(request.form['delCategory'])
        categoriesList = db.Categories.query.all()
        return render_template('admin/categories/categories.html', categoriesList=categoriesList, status=status)
    categoriesList = db.Categories.query.all()
    return render_template('admin/categories/categories.html', categoriesList=categoriesList)

@core.route('/admin/categories/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        print(request.form)
        tag = models.Categories(name=request.form['title'], description=request.form['description'])
        db.db.session.add(tag)
        db.db.session.commit()
        return redirect(url_for('adminCategories'))
    categories = db.Categories.query.all()
    return render_template('admin/categories/newcategory.html', categoriesList=categories)

@core.route('/admin/categories/edit/<int:categoryid>', methods=['GET', 'POST'])
def editCategory(categoryid):
    if request.method == 'POST':
        category = db.Categories.query.filter_by(id=categoryid).first()
        print(category.id)
        category.name = request.form['title']
        category.description = request.form['description']

        print(category.description)
        db.db.session.commit()
        return redirect(url_for('adminCategories'))
    category = db.Categories.query.filter_by(id=categoryid).first()
    return render_template('admin/categories/editcategory.html', category=category)

def delTag(categoryID):
    print(db.Categories.query.filter_by(id=categoryID).first() )
    if db.Categories.query.filter_by(id=categoryID).first() is None:
        return -1
    else:
        tag = db.Categories.query.filter_by(id=categoryID).first()
        db.db.session.delete(tag)
        db.db.session.commit()
        return 1

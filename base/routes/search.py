from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/search')
def search():
    return render_template('search.html', db=db)

@core.route('/search/<keyword>')
def search_result(keyword):
    return 'result of ' + escape(keyword) + ' : '
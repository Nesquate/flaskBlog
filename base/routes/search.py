from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/search')
def search():
    siteInfo = db.Site.query.first()
    return render_template('search.html', siteData=siteInfo)

@core.route('/search/<keyword>')
def search_result(keyword):
    return 'result of ' + escape(keyword) + ' : '
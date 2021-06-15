from operator import pos
from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/admin')
@core.route('/admin/')
def adminIndex():
    return render_template('admin/index.html')
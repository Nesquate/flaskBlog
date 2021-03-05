from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/install')
def dbCreate():
    db.db.create_all()
    return 'You can check if data.db exist or not.'
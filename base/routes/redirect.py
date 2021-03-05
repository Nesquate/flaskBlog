from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

@core.route('/post')
@core.route('/categorie')
@core.route('/tag')
def returnToHome():
    return redirect(url_for('home'))
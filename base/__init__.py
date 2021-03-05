from flask import render_template, url_for, escape, redirect, abort
from app import core
from database import db

from base.routes import redirect, home, post, tag, category, search
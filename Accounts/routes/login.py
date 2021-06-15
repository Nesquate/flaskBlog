from flask import render_template, url_for, escape, redirect, abort, request
from flask_login.utils import login_required, logout_user, login_user, current_user
from app import core, login_manager
from database import db, models

@core.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        account = db.Users.query.filter_by(account=account).first()
        if password is not None:
            if models.Users.check_password(account, password) and account is not None:
                login_user(account)
                return redirect('/')
    return render_template('login.html', db=db)

@core.route('/logout')
@login_required
def logoutPage():
    logout_user()
    return redirect('/')
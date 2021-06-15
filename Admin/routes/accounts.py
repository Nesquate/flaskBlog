from flask import render_template, url_for, request
from flask_login.utils import login_required, current_user
from app import core, login_manager
from database import db, models

@core.route('/admin/account', methods=['GET', 'POST'])
@login_required
def accountSetting():
    accountInfo = db.Users.query.filter_by(id=current_user.id).first()
    if request.method == 'POST':
        status = 0
        newName = request.form['accountName']
        newIntroduction = request.form['accountIntroduction']
        newPassword = request.form['changePassword']
        confirmPassword = request.form['confirmChange']
        accountInfo.name = newName
        accountInfo.introduction = newIntroduction
        if newPassword != "" and confirmPassword != "":
            if newPassword == confirmPassword:
                models.Users.change_password(accountInfo, newPassword)
                status = 1
            else:
                status = 2
        db.db.session.commit()
        return render_template('admin/account.html', accountInfo=accountInfo, status=status)

    return render_template('admin/account.html', accountInfo=accountInfo) 
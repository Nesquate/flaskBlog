from flask import render_template, url_for, request
from flask_login.utils import login_required
from app import core
from database import db

@core.route('/admin/setting', methods=['GET', 'POST'])
@login_required
def siteSetting():
    siteInfo = db.Site.query.filter_by(id=1).first()
    if request.method == 'POST':
        newSiteName = request.values['siteName']
        newSiteDescription = request.values['siteDescription']
        siteInfo.name = newSiteName
        siteInfo.description = newSiteDescription
        db.db.session.commit()
        return render_template('admin/setting.html', siteInfo=siteInfo, status=True)
    return render_template('admin/setting.html', siteInfo=siteInfo)
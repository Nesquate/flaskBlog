from flask import Flask, render_template, url_for, escape, redirect, abort
core = Flask(__name__)

postData = [{
    'id':'1',
    'name':'test',
    'content':'<p>this is a test post.</p>',
    'tag':'test, post',
    'category':'admin'
},
{
    'id':'2',
    'name':'test2',
    'content':'<p>this is a test post2.</p>',
    'tag':'test',
    'category':'admin'
}]

def setSite():
    homeUrl = url_for('home')
    searchUrl = url_for('search')
    siteData = [
        {
            'title':'Test Title',
            'description':'A test site by Flask',
            'url':homeUrl
        },
        [
            {'name':'Home', 'url':homeUrl},
            {'name':'Search', 'url':searchUrl}
        ]
    ]
    return siteData

    

def genPostLink(postData):
    for i in postData:
        i['url'] = url_for('postPage', postid = i['id'])

@core.route('/')
def home():
    genPostLink(postData)
    siteData = setSite()
    return render_template('post.html', 
        postData=postData,
        siteData=siteData
    )

@core.route('/post/<int:postid>')
def postPage(postid):
    siteData = setSite()
    postSize = len(postData)
    if postid <= postSize  and postid > 0:
        return render_template('post.html', 
            postData=postData,
            postid=postid,
            siteData=siteData
        )
    else:
        return abort(404)

@core.route('/post')
@core.route('/categorie')
@core.route('/tag')
def returnToHome():
    return redirect(url_for('home'))

@core.route('/tag/<tag>')
def tagPage(tag):
    return 'Now tag is :' + escape(tag)

@core.route('/category/<category>')
def categoryPage(category):
    return 'Now category is : ' + escape(categories)

@core.route('/search')
def search():
    siteData = setSite()
    return render_template(
        'search.html',
        siteData=siteData
    )

@core.route('/search/<keyword>')
def search_result(keyword):
    return 'result of ' + escape(keyword) + ' : '
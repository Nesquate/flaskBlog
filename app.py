from flask import Flask, render_template, url_for, escape
core = Flask(__name__)

from testdata import postData, title

@core.route('/')
def home():
    for i in postData:
        i['url'] = url_for('postPage', postid = i['id'])
    
    return render_template('post.html', postData=postData, viewPost=False, title=title, homelink=url_for('home'))

@core.route('/post/<postid>')
def postPage(postid):
    return render_template("post.html", postData=postData[int(postid)-1], viewPost=True, title=title, homelink=url_for('home'))

@core.route('/tags')
def tags():
    return render_template('tags.html')

@core.route('/tag/<tag>')
def tagPage(tag):
    return 'Now tag is :' + escape(tag)

@core.route('/categories')
def categories():
    return render_template("categories.html")

@core.route('/category/<category>')
def categoryPage(category):
    return 'Now category is : ' + escape(categories)

@core.route('/search')
def search():
    return render_template('search.html')

@core.route('/search/<keyword>')
def search_result(keyword):
    return 'result of ' + escape(keyword) + ' : '
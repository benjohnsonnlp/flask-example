from flask import request, render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    if 'name' in request.args:
        return "Hello, " + request.args['name']
    return "Hello, World!"


@app.route('/templated')
def templated():
    some_name = "Anuar"  # A normal python variable!
    posts = [
        {
            "text": "Great seeing you today, mate!",
            "author": "Geetha",
        },
        {
            "text": "Found a great new cookie recipe for you!",
            "author": "Sebastian",
        }
    ]
    return render_template('index.html', name=some_name, updates=posts)

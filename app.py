from flask import Flask, url_for, render_template

app = Flask(__name__)

name = '小明'
movies = [
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', name=name, movies=movies)


@app.route('/users/<name>')
def user_page(name):
    return 'User: %s' % name


@app.route('/test')
def test():
    url = url_for('test')
    print(url)
    url = url_for('user_page', name='jack')
    print(url)
    return url

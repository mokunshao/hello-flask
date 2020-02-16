from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'


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

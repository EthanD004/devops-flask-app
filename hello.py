from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About</a></p>'

@app.route('/about')
def about():
    return '<p>This app runs on the <a href="https://flask.palletsprojects.com/">Flask</a> web framework.</p>'

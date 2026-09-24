from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About</a> | <a href="/contact">Contact</a></p>'

@app.route('/about')
def about():
    return '<p>This app runs on the <a href="https://flask.palletsprojects.com/">Flask</a> web framework.</p>'

@app.route('/contact')
def contact():
    return '<p>Email: c23348713@mytudublin.ie</p>'

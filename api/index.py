from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'DIDDY PLEASE PLEASE PLEASE'

@app.route('/about')
def about():
    return 'About'

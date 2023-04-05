from flask import Flask, render_template

app = Flask(__name__)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/')
def index():
    return render_template('index.html')


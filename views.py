from flask import render_template

from app import app


@app.route('/')
def home():
    print('Test')
    return render_template('main.html')

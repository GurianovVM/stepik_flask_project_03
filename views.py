from flask import render_template

from app import app


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/cart/')
def cart():
    return render_template('cart.html')


@app.route('/account/')
def account():
    return render_template('account.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/logout/')
def logout():
    return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/ordered/')
def ordered():
    return render_template('ordered.html')

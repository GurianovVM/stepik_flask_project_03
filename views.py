from flask import render_template

from app import app, db
from models import Category, Dish

@app.route('/')
def home():
    category = db.session.query(Category).all()
    dish_list = []
    for cat in category:
        dish = db.session.query(Dish).filter(Dish.category_id == cat.id).limit(3)
        dish_list.append(dish)
    return render_template('index.html', category=category, dishes=dish_list)


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

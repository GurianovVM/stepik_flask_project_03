from flask import Flask, render_template
from flask_migrate import Migrate

from config import Config
from models import db, Client, Dish, Category, Order, dish_categories_association, order_dish_association

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# __________________________________________
# from views import *
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
# __________________________________________

"""
if __name__ == 'main':
    app.run()
"""
app.run()
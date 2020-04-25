from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  # Для работы записи в бд включить

from config import Config

# from models import db, Category, Client, Dish, Order   # для запуска миграций нужно включить


app = Flask(__name__)
app.config.from_object(Config)

# db.init_app(app)   # для запуска миграций нужно включить
db = SQLAlchemy(app)    # для работы записи в бд включить

migrate = Migrate(app, db)

from views import *

if __name__ == '__main__':
    app.run()

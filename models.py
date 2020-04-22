from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

dish_categories_association = db.Table('dish_categories',
                                       db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id')),
                                       db.Column('categories_id', db.Integer, db.ForeignKey('categories.id')),
                                       )
order_dish_association = db.Table('order_dish',
                                  db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                                  db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id')),
                                  )


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    orders = db.relationship('Order')


class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    picture = db.Column(db.String(200))
    category = db.relationship('Category', secondary=dish_categories_association, back_populates='dishes')
    order = db.relationship('Order', secondary=order_dish_association, back_populates='dishes')


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dishes = db.relationship('Dish', secondary=dish_categories_association, back_populates='categories')


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    cash = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(50))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('Client')
    dish = db.relation('Dish', secondary=dish_categories_association, back_populates='orders')

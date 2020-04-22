
import csv
from app import db
from models import Dish, Category

with open('Данные для проекта 4 - meals.csv', 'r') as f:
    read = csv.DictReader(f)
    print('Открыли файл с блюдами')
    for i in read:
        dish = Dish(title=i['title'], price=i['price'], description=i['description'], picture=i['picture'],
                    category_id=i['category_id'])
        db.session.add(dish)
        print('Добавили блюдо' + i['title'])
    db.session.commit()
    print('Добавили в базу')

'''
with open('Данные для проекта 4 - categories.csv', 'r') as f:
    read = csv.DictReader(f)
    print('Открыли файл с блюдами')
    for i in read:
        category = Category(name=i['title'])
        db.session.add(category)
        print('Добавили блюдо' + i['title'])
    db.session.commit()
    print('Добавили в базу')
'''
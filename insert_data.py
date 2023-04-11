from datetime import date
from sqlalchemy.ext.declarative import DeclarativeMeta

from database import db
from models import Publisher, Book, Stock, Shop, Sale


def insert_data(session: db, model: DeclarativeMeta, kw_data: dict):
    new_data = model(**kw_data)
    session.add(new_data)
    session.commit()


def insert_publishers():
    publishers = ['Миф', 'Питер', 'Китап', 'Эксмо']
    for publisher in publishers:
        data = {'name': publisher}
        insert_data(db, Publisher, data)


def insert_shops():
    shops = ['Лабиринт', 'Book24']
    for shop in shops:
        data = {'name': shop}
        insert_data(db, Shop, data)


def insert_books():
    books = ['Дом ворон', 'Макромир', 'Радость нашего дома', 'Python для детей', 'Математика 3 класс']
    for book in books:
        data = {'title': book, 'id_publisher': 1}
        insert_data(db, Book, data)


def insert_stocks():
    stocks = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5']
    for stock in stocks:
        data = {'id_shop': 1, 'id_book': 2, 'count': 10}
        insert_data(db, Stock, data)

# stock1 = Stock(Shop=shop1, Book=book1, count=10)
# stock2 = Stock(Shop=shop1, Book=book3, count=10)
# stock3 = Stock(Shop=shop1, Book=book4, count=10)
# stock4 = Stock(Shop=shop2, Book=book5, count=10)
# stock5 = Stock(Shop=shop2, Book=book2, count=10)

# sale1 = Sale(Stock=stock2, price=199, count=2, date_sale=date(2023, 1, 25))
# db.add_all([sale1])



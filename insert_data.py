from datetime import date
# from sqlalchemy.ext.declarative import DeclarativeMeta


from database import db
from models import Publisher, Book, Stock, Shop, Sale


# def insert_data(db: db, model: DeclarativeMeta, kw_data: dict):
#     new_data = model(**kw_data)
#     db.add(new_data)
#     db.commit()
#
#
# def insert_publishers():
#     publishers = ['Миф', 'Питер', 'Китап', 'Эксмо']
#     for publisher in publishers:
#         data = {'name': publisher}
#         insert_data(db, Publisher, data)
#
#
# def insert_shops():
#     shops = ['Лабиринт', 'Book24']
#     for shop in shops:
#         data = {'name': shop}
#         insert_data(db, Shop, data)
#
#
# def insert_books():
#     books = ['Дом ворон', 'Макромир', 'Радость нашего дома', 'Python для детей', 'Математика 3 класс']
#     for book in books:
#         data = {'title': book, 'id_publisher': 1}
#          #   Пока не понял как сюда нужного паблишера подставлять
#         insert_data(db, Book, data)
#
#
# def insert_stocks():
#     stocks = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5']
#     for stock in stocks:
#         data = {'id_shop': 1, 'id_book': 2, 'count': 10}
#         insert_data(db, Stock, data)


def insert_data():
    publisher1 = Publisher(name='Миф')
    publisher2 = Publisher(name='Питер')
    publisher3 = Publisher(name='Китап')
    publisher4 = Publisher(name='Эксмо')
    publisher5 = Publisher(name='Дрофа')
    db.add_all([publisher1, publisher2, publisher3, publisher4, publisher5])
    db.commit()

    book1 = Book(title='Дом ворон', Publisher=publisher1)
    book2 = Book(title='Макромир', Publisher=publisher2)
    book3 = Book(title='Радость нашего дома', Publisher=publisher3)
    book4 = Book(title='Python для детей', Publisher=publisher4)
    book5 = Book(title='Математика 3 класс', Publisher=publisher5)
    db.add_all([book1, book2, book3, book4, book5])
    db.commit()

    shop1 = Shop(name='Лабиринт')
    shop2 = Shop(name='Book24')
    db.add_all([shop1, shop2])
    db.commit()

    stock1 = Stock(Shop=shop1, Book=book1, count=10)
    stock2 = Stock(Shop=shop1, Book=book3, count=10)
    stock3 = Stock(Shop=shop1, Book=book4, count=10)
    stock4 = Stock(Shop=shop2, Book=book5, count=10)
    stock5 = Stock(Shop=shop2, Book=book5, count=10)
    db.add_all([stock1, stock2, stock3, stock4, stock5])
    db.commit()

    sale1 = Sale(Stock=stock2, price=199, count=2, date_sale=date(2023, 1, 25))
    db.add_all([sale1])
    db.commit()


if __name__ == '__main__':
    insert_data()

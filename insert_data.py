from datetime import date
from sqlalchemy.ext.declarative import DeclarativeMeta

from database import db
from models import Publisher, Book, Stock, Shop, Sale

publisher1 = Publisher(name='Миф')
publisher2 = Publisher(name='Питер')
publisher3 = Publisher(name='Китап')
publisher4 = Publisher(name='Эксмо')
db.add_all([publisher1, publisher2, publisher3, publisher4])
db.commit()

book1 = Book(title='Дом ворон', Publisher=publisher1)
book2 = Book(title='Макромир', Publisher=publisher2)
book3 = Book(title='Радость нашего дома', Publisher=publisher3)
book4 = Book(title='Python для детей', Publisher=publisher2)
book5 = Book(title='Математика 3 класс', Publisher=publisher4)
db.add_all([book1, book2, book3, book4, book5])
db.commit()

shop1 = Shop(name='Лабиринт')
shop2 = Shop(name='Book24')
db.add_all([shop1, shop2])

stock1 = Stock(Shop=shop1, Book=book1, count=10)
stock2 = Stock(Shop=shop1, Book=book3, count=10)
stock3 = Stock(Shop=shop1, Book=book4, count=10)
stock4 = Stock(Shop=shop2, Book=book5, count=10)
stock5 = Stock(Shop=shop2, Book=book2, count=10)
db.add_all([stock1, stock2, stock3, stock4, stock5])

sale1 = Sale(Stock=stock2, price=199, count=2, date_sale=date(2023, 1, 25))
db.add_all([sale1])


# def insert_data(model, *kwargs):
#     # example_data = kwargs
#     # m = Publisher(name='Эксмо')
#     # for k, v in kwargs:
#     m = model(kwargs)
#     db.add(m)
#     db.commit()
#     return f'Inserted {m} with {kwargs}'

def insert_data(session: db, model: DeclarativeMeta, kw_data: dict):
    new_data = model(**kw_data)
    session.add(new_data)
    session.commit()


if __name__ == '__main__':
    data = {'name': 'Миф'}
    insert_data(db, Publisher, data)

    # print(insert_data(model=Publisher, {'name': 'Миф'}))

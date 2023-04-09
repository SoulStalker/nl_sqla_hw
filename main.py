import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import date

from models import create_tables, Publisher, Book, Stock, Shop, Sale


with open('dsn.txt', encoding='utf-8') as dsn_file:
    # строка подключения к базе
    # если локалохст то вот такой:
    # postgresql://postgres:postgres@localhost:5432/nl_sqla_hw
    # у меня внешний сервер поэтому dsn не передаю в гит
    dsn = dsn_file.read()

DSN = dsn
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Миф')
publisher2 = Publisher(name='Питер')
publisher3 = Publisher(name='Китап')
publisher4 = Publisher(name='Эксмо')
session.add_all([publisher1, publisher2, publisher3, publisher4])
session.commit()

book1 = Book(title='Дом ворон', Publisher=publisher1)
book2 = Book(title='Макромир', Publisher=publisher2)
book3 = Book(title='Радость нашего дома', Publisher=publisher3)
book4 = Book(title='Python для детей', Publisher=publisher2)
book5 = Book(title='Математика 3 класс', Publisher=publisher4)
session.add_all([book1, book2, book3, book4, book5])
session.commit()

shop1 = Shop(name='Лабиринт')
shop2 = Shop(name='Book24')
session.add_all([shop1, shop2])

stock1 = Stock(Shop=shop1, Book=book1, count=10)
stock2 = Stock(Shop=shop1, Book=book3, count=10)
stock3 = Stock(Shop=shop1, Book=book4, count=10)
stock4 = Stock(Shop=shop2, Book=book5, count=10)
stock5 = Stock(Shop=shop2, Book=book2, count=10)
session.add_all([stock1, stock2, stock3, stock4, stock5])

sale1 = Sale(Stock=stock2, price=199, count=2, date_sale=date(2023, 1, 25))
session.add_all([sale1])

publisher_name = input("Введите имя издателя: ")

shops = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()

for shop in shops:
    print(shop.name)

session.close()

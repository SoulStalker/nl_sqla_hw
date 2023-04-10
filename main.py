from datetime import date
from database import db, engine
from models import create_tables, Publisher, Book, Stock, Shop, Sale

create_tables(engine)

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

publisher_name = input("Введите имя издателя: ")

shops = db.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()

for shop in shops:
    print(shop.name)

db.close()

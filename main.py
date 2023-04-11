from database import db
from models import Publisher, Book, Stock, Shop, Sale

publisher_name = input("Введите имя издателя: ")

shops = db.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()

for shop in shops:
    print(shop.name)

db.close()

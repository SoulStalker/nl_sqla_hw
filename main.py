from database import db
from models import create_db, Publisher, Book, Stock, Shop, Sale
import insert_data

create_db()

insert_data.insert_publishers()
insert_data.insert_shops()
insert_data.insert_books()


publisher_name = input("Введите имя издателя: ")

shops = db.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all()

for shop in shops:
    print(shop.name)

db.close()

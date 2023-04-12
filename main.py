from database import db
from models import Publisher, Book, Stock, Shop


def get_shops(publisher):
    shops = db.query(Shop).join(Stock).join(Book).join(Publisher)
    if publisher.isdigit():
        shops.filter(Publisher.id == publisher).all()
    else:
        shops.filter(Publisher.name == publisher).all()
    res_list = []
    for shop in shops:
        res_list.append(shop.name)
    return res_list


if __name__ == '__main__':
    print(*get_shops(input("Введите имя или ID издателя: ")))

db.close()

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from database import db_engine

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    Books = relationship("Book", back_populates="Publisher")

    def __str__(self):
        return f'Издатель {self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    Publisher = relationship("Publisher", back_populates="Books")
    Stocks = relationship("Stock", back_populates="Book")

    def __str__(self):
        return f'Книга {self.id}: {self.title}'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60))
    Stocks = relationship("Stock", back_populates="Shop")

    def __str__(self):
        return f'Магазин {self.id}, {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    Shop = relationship("Shop", back_populates="Stocks")
    Book = relationship("Book", back_populates="Stocks")


def __str__(self):
    return f'Склад {self.id}: {self.id_book}, {self.count}'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    Stock = relationship(Stock, backref='sale')


def create_db():
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)


if __name__ == '__main__':
    create_db()

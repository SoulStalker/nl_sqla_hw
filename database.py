import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session(), engine


with open('dsn.txt', encoding='utf-8') as dsn_file:
    # строка подключения к базе
    # если локалохст то вот такой:
    # postgresql://postgres:postgres@localhost:5432/nl_sqla_hw
    # у меня внешний сервер поэтому dsn не передаю в гит
    dsn = dsn_file.read()

db, engine = create_session(dsn)



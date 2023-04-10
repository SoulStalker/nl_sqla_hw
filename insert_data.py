from database import db


def insert_data(*args):
    example_data = args
    db.add(example_data)
    db.commit()


if __name__ == '__main__':
    insert_data()
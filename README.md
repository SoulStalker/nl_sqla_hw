# nl_sqla_hw
Домашнее задание к лекции «Python и БД. ORM»
Задание 1
Составить модели классов SQLAlchemy по схеме:
https://raw.githubusercontent.com/netology-code/py-homeworks-db/video/06-orm/readme/book_publishers_scheme.png

Интуитивно необходимо выбрать подходящие типы и связи полей.

Задание 2
Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
Импортирует необходимые модели данных.
Выводит название магазинов (shop), в которых представлены книги конкретного издателя, получая имя или идентификатор издателя (publisher), через input().

**Задание 3 (необязательное)
Заполните БД тестовыми данными.

Тестовые данные берутся из папки fixtures. Пример содержания в JSON файле.

Возможная реализация: прочитать json-файл, создать соотведствующие экземляры моделей и сохранить в БД.




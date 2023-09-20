import mysql.connector
from random import randint, choice
import datetime

# Устанавливаем соединение с базой данных
connection = mysql.connector.connect(
    host='localhost',
    user='roanvl',
    password='!And487052!',
    database='co_crm'
)

# Создаем объект для выполнения SQL-запросов
cursor = connection.cursor()

# Генерируем случайную дату и время


def created_at():
    year = randint(2023, 2023)
    month = randint(9, 10)
    day = randint(1, 30)  # Предполагаем, что февраль считается до 28 числа
    return f"{year}-{month:02d}-{day:02d}"
# Генерируем случайную дату в пределах последних года


def shipping_date():
    year = randint(2023, 2023)
    month = randint(10, 12)
    day = randint(1, 30)  # Предполагаем, что февраль считается до 28 числа
    return f"{year}-{month:02d}-{day:02d}"

# Генерируем случайное описание заказа


def order_description():
    return "Random description"  # Замените эту строку на свою логику


# Пример SQL-запроса для вставки данных в таблицу website_orders
insert_query = "INSERT INTO co_crm.website_orders (order_status_id, company_id, product_id, quantity, manager_id, shipping_date, order_amount, created_at, order_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    (randint(1, 2), randint(1, 35), randint(2, 20), randint(1, 50), randint(2, 13), shipping_date(), 0, created_at(), order_description()) for _ in range(50)
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

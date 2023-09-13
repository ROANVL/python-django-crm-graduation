import mysql.connector
from random import randint, choice

# Устанавливаем соединение с базой данных
connection = mysql.connector.connect(
    host='localhost',
    user='roanvl',
    password='!And487052!',
    database='co_crm'
)

# Создаем объект для выполнения SQL-запросов
cursor = connection.cursor()

# Генерируем случайную дату в пределах последних года


def random_date():
    year = randint(2021, 2022)
    month = randint(1, 12)
    day = randint(1, 28)  # Предполагаем, что февраль считается до 28 числа
    return f"{year}-{month:02d}-{day:02d}"

# Генерируем случайную сумму заказа


def random_order_amount():
    return round(randint(100, 10000) + randint(0, 99) / 100, 2)

# Генерируем случайный статус заказа


def order_status_id():
    return randint(1, 12)

# Генерируем случайное описание заказа


def random_order_description():
    return f"Description for order #{randint(1, 1000)}"

# Генерируем случайный адрес доставки


def random_shipping_address():
    return f"Address {randint(1, 1000)}, City {randint(1, 1000)}, State {randint(1, 1000)}, Zipcode {randint(1, 1000)}"


# Пример SQL-запроса для вставки данных в таблицу website_orders
insert_query = "INSERT INTO co_crm.website_orders (order_date, order_amount, company_id, manager_id, status_id, order_description, shipping_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    (random_date(), random_order_amount(), randint(1, 91), randint(2, 31), order_status_id(), random_order_description(), random_shipping_address()) for _ in range(30)
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

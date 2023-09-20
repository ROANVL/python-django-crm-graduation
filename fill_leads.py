import mysql.connector
import random
from faker import Faker
import datetime

fake = Faker(locale="en_US")

# Заданные варианты рекламы
advertising_sources = ["Internet", "Radio", "TV", "Social Media", "Print"]

# Текст о продажах компьютерной техники
sales_text = "We offer a wide range of computer hardware and software solutions to meet your technology needs."


def creation_date():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S')


def expected_close_date():
    future_date = fake.future_date(end_date='+30d', tzinfo=None)
    return future_date.strftime('%Y-%m-%d %H:%M:%S')


def generate_lead():
    lead = [
        fake.first_name(),
        fake.last_name(),
        fake.basic_phone_number(),
        fake.email(),
        creation_date(),
        creation_date(),
        random.choice(advertising_sources),
        sales_text,  # Используем текст о продажах компьютерной техники
        expected_close_date(),
        random.randint(1, 9),
    ]
    return lead


# Генерируем 5 лидов
leads = [generate_lead() for _ in range(100)]

# Установка соединения с базой данных MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='roanvl',
    password='!And487052!',
    database='co_crm'
)

# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Пример SQL-запроса для вставки данных в таблицу
insert_query = "INSERT INTO co_crm.website_leads (first_name, last_name, phone, email, created_at, creation_date, lead_source, lead_description, expected_close_date, lead_status_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Вставляем сгенерированные лиды в таблицу
cursor.executemany(insert_query, leads)

# Фиксируем изменения в базе данных
connection.commit()

# Закрываем курсор и соединение
cursor.close()
connection.close()

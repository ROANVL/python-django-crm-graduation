import mysql.connector

# Устанавливаем соединение с базой данных
connection = mysql.connector.connect(
    host='localhost',
    user='roanvl',
    password='!And487052!',
    database='co_crm'
)


# Создаем объект для выполнения SQL-запросов
cursor = connection.cursor()

# Пример SQL-запроса для вставки данных в таблицу
insert_query = "INSERT INTO co_crm.website_product (name, quantity, price_per_unit) VALUES (%s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    ("Laptop", 100, 799.99),
    ("Desktop PC", 50, 999.99),
    ("Smartphone", 200, 499.99),
    ("Tablet", 150, 299.99),
    ("Monitor", 120, 249.99),
    ("Keyboard", 300, 29.99),
    ("Mouse", 400, 19.99),
    ("Printer", 80, 149.99),
    ("Scanner", 60, 129.99),
    ("Graphics Card", 70, 399.99),
    ("CPU", 90, 299.99),
    ("RAM (8GB)", 200, 79.99),
    ("Hard Drive (1TB)", 150, 59.99),
    ("SSD (256GB)", 100, 89.99),
    ("Wireless Router", 120, 49.99),
    ("External Hard Drive (2TB)", 80, 79.99),
    ("USB Flash Drive (32GB)", 300, 12.99),
    ("Webcam", 200, 29.99),
    ("External SSD (512GB)", 50, 129.99),
    ("Gaming Mouse", 150, 69.99)
]


# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

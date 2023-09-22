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
insert_query = "INSERT INTO co_crm.website_managers (first_name, last_name, phone, email, job_title_id, department_id) VALUES (%s, %s, %s, %s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    ('Emma', 'Smith', '111-222-3333', 'emma.smith@example.com', 1, 1),
    ('John', 'Doe', '444-555-6666', 'john.doe@example.com', 2, 2),
    ('Michael', 'Johnson', '777-888-9999', 'michael.johnson@example.com', 2, 3),
    ('Sarah', 'Wilson', '333-444-5555', 'sarah.wilson@example.com', 2, 4),
    ('David', 'Brown', '666-777-8888', 'david.brown@example.com', 3, 2),
    ('Linda', 'Davis', '999-000-1111', 'linda.davis@example.com', 3, 3),
    ('James', 'Miller', '222-333-4444', 'james.miller@example.com', 3, 4),
    ('Susan', 'Martinez', '555-666-7777', 'susan.martinez@example.com', 3, 2),
    ('Robert', 'Hernandez', '888-999-0000', 'robert.hernandez@example.com', 3, 3),
    ('William', 'Garcia', '111-222-3333', 'william.garcia@example.com', 3, 4),
    ('Mary', 'Lopez', '444-555-6666', 'mary.lopez@example.com', 3, 2),
    ('Jennifer', 'Perez', '777-888-9999', 'jennifer.perez@example.com', 3, 3),
    ('Daniel', 'Taylor', '555-666-7777', 'daniel.taylor@example.com', 3, 4),
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

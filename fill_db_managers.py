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
    ('Emma', 'Smith', '111-222-3333', 'emma.smith@example.com', '9', '1'),


    # Добавьте другие данные, которые вы хотите вставить
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

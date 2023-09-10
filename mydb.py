import mysql.connector

# Параметры подключения к MySQL
db_config = {
    "host": "localhost",
    "user": "roanvl",
    "password": "!And487052!",
}

try:
    # Создаем подключение к MySQL серверу
    conn = mysql.connector.connect(**db_config)

    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # Создаем базу данных 'co_crm' (если она не существует)
    cursor.execute("CREATE DATABASE IF NOT EXISTS co_crm")

    print("Database 'co_crm' created (if it didn't exist).")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Закрываем курсор и соединение
    if cursor:
        cursor.close()
    if conn:
        conn.close()

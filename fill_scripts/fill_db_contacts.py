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
insert_query = "INSERT INTO co_crm.website_contacts (first_name, last_name, job_title, phone, email, description, date_of_birth, company_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    ('John', 'Doe', 'Director', '111-222-3333', 'john.doe@example.com',
     'Leading the company towards innovative technological solutions.', '1980-05-10', 1, '2023-09-20'),
    ('Emily', 'Smith', 'Financial Director', '222-333-4444', 'emily.smith@example.com',
     'Overseeing the financial operations of the company.', '1985-08-15', 1, '2023-09-20'),
    ('David', 'Johnson', 'Chief Accountant', '333-444-5555', 'david.johnson@example.com',
     'Managing financial records and budgets.', '1978-03-25', 1, '2023-09-20'),
    ('Sarah', 'Brown', 'Procurement Manager', '444-555-6666', 'sarah.brown@example.com',
     'Handling procurement and vendor relationships.', '1990-11-30', 1, '2023-09-20'),
    ('Olivia', 'Davis', 'Secretary', '555-666-7777', 'olivia.davis@example.com',
     'Providing administrative support to the team.', '1987-12-02', 1, '2023-09-20'),
    ('Michael', 'Wilson', 'Director', '666-777-8888', 'michael.wilson@example.com',
     'Leading the company in healthcare innovation.', '1983-07-20', 2, '2023-09-20'),

    ('Sophia', 'Garcia', 'Financial Director', '777-888-9999', 'sophia.garcia@example.com',
     'Overseeing financial aspects of healthcare projects.', '1989-11-10', 2, '2023-09-20'),
    ('William', 'Martinez', 'Chief Accountant', '888-999-0000', 'william.martinez@example.com',
     'Managing financial records in healthcare sector.', '1987-04-15', 2, '2023-09-20'),
    ('Eva', 'Clark', 'Procurement Manager', '999-000-1111', 'eva.clark@example.com',
     'Handling procurement for healthcare supplies.', '1994-02-12', 2, '2023-09-20'),
    ('James', 'Anderson', 'Secretary', '111-222-3333', 'james.anderson@example.com',
     'Providing administrative support in healthcare field.', '1992-08-25', 2, '2023-09-20'),
    ('Emma', 'Brown', 'Director', '111-222-3333', 'emma.brown@example.com',
     'Leading financial strategies and operations.', '1982-09-18', 3, '2023-09-20'),

    ('Liam', 'Davis', 'Financial Director', '222-333-4444', 'liam.davis@example.com',
     'Overseeing financial planning and analysis.', '1986-12-05', 3, '2023-09-20'),
    ('Chloe', 'Johnson', 'Chief Accountant', '333-444-5555', 'chloe.johnson@example.com',
     'Managing financial records and reporting.', '1979-06-30', 3, '2023-09-20'),
    ('Oliver', 'Smith', 'Procurement Manager', '444-555-6666', 'oliver.smith@example.com',
     'Handling procurement and supplier relationships.', '1991-10-14', 3, '2023-09-20'),
    ('Ava', 'Wilson', 'Secretary', '555-666-7777', 'ava.wilson@example.com',
     'Providing administrative support to the finance team.', '1984-02-22', 3, '2023-09-20'),
    ('Mia', 'Martinez', 'Director', '666-777-8888', 'mia.martinez@example.com',
     'Leading retail strategies and growth initiatives.', '1988-04-27', 4, '2023-09-20'),

    ('Noah', 'Clark', 'Financial Director', '777-888-9999', 'noah.clark@example.com',
     'Overseeing financial aspects of retail operations.', '1981-01-08', 4, '2023-09-20'),
    ('Aiden', 'Taylor', 'Chief Accountant', '888-999-0000', 'aiden.taylor@example.com',
     'Managing financial records in the retail sector.', '1983-05-16', 4, '2023-09-20'),
    ('Lucas', 'Anderson', 'Procurement Manager', '999-000-1111', 'lucas.anderson@example.com',
     'Handling procurement for retail products.', '1995-03-11', 4, '2023-09-20'),
    ('Sophie', 'Brown', 'Secretary', '111-222-3333', 'sophie.brown@example.com',
     'Providing administrative support in the retail industry.', '1993-07-19', 4, '2023-09-20'),
    ('Liam', 'Garcia', 'Director', '111-222-3333', 'liam.garcia@example.com',
     'Leading global logistics and supply chain solutions.', '1980-08-24', 5, '2023-09-20'),

    ('Emma', 'Martinez', 'Financial Director', '222-333-4444', 'emma.martinez@example.com',
     'Overseeing financial planning for logistics projects.', '1984-03-14', 5, '2023-09-20'),
    ('Ava', 'Taylor', 'Chief Accountant', '333-444-5555', 'ava.taylor@example.com',
     'Managing financial records for logistics operations.', '1986-09-28', 5, '2023-09-20'),
    ('Noah', 'Brown', 'Procurement Manager', '444-555-6666', 'noah.brown@example.com',
     'Handling procurement and vendor relationships in logistics.', '1990-11-30', 5, '2023-09-20'),
    ('Olivia', 'Davis', 'Secretary', '555-666-7777', 'olivia.davis@example.com',
     'Providing administrative support to the logistics team.', '1989-12-02', 5, '2023-09-20'),
    ('Sophia', 'Wilson', 'Director', '666-777-8888', 'sophia.wilson@example.com',
     'Leading data analytics projects and solutions.', '1983-07-20', 6, '2023-09-20'),

    ('Oliver', 'Brown', 'Financial Director', '777-888-9999', 'oliver.brown@example.com',
     'Overseeing financial aspects of data analytics ventures.', '1989-11-10', 6, '2023-09-20'),
    ('Liam', 'Clark', 'Chief Accountant', '888-999-0000', 'liam.clark@example.com',
     'Managing financial records in the data analytics field.', '1987-04-15', 6, '2023-09-20'),
    ('Aiden', 'Garcia', 'Procurement Manager', '999-000-1111', 'aiden.garcia@example.com',
     'Handling procurement for data analytics projects.', '1994-02-12', 6, '2023-09-20'),
    ('Chloe', 'Smith', 'Secretary', '111-222-3333', 'chloe.smith@example.com',
     'Providing administrative support in data analytics.', '1992-08-25', 6, '2023-09-20'),
    ('Lucas', 'Smith', 'Director', '111-222-3333', 'lucas.smith@example.com',
     'Leading green energy projects and innovations.', '1980-05-12', 7, '2023-09-20'),

    ('Chloe', 'Wilson', 'Financial Director', '222-333-4444', 'chloe.wilson@example.com',
     'Overseeing financial aspects of green energy initiatives.', '1983-03-19', 7, '2023-09-20'),
    ('Mia', 'Davis', 'Chief Accountant', '333-444-5555', 'mia.davis@example.com',
     'Managing financial records in the green energy sector.', '1982-09-23', 7, '2023-09-20'),
    ('Liam', 'Garcia', 'Procurement Manager', '444-555-6666', 'liam.garcia@example.com',
     'Handling procurement for green energy projects.', '1989-12-08', 7, '2023-09-20'),
    ('Noah', 'Martinez', 'Secretary', '555-666-7777', 'noah.martinez@example.com',
     'Providing administrative support in the green energy field.', '1995-02-01', 7, '2023-09-20'),
    ('Sophie', 'Brown', 'Director', '666-777-8888', 'sophie.brown@example.com',
     'Leading fashion trends and design initiatives.', '1987-06-15', 8, '2023-09-20'),

    ('Olivia', 'Davis', 'Financial Director', '777-888-9999', 'olivia.davis@example.com',
     'Overseeing financial planning for fashion projects.', '1982-10-28', 8, '2023-09-20'),
    ('Aiden', 'Garcia', 'Chief Accountant', '888-999-0000', 'aiden.garcia@example.com',
     'Managing financial records in the fashion industry.', '1985-04-17', 8, '2023-09-20'),
    ('Emma', 'Wilson', 'Procurement Manager', '999-000-1111', 'emma.wilson@example.com',
     'Handling procurement for fashion products and materials.', '1992-03-22', 8, '2023-09-20'),
    ('Liam', 'Smith', 'Secretary', '111-222-3333', 'liam.smith@example.com',
     'Providing administrative support to the fashion team.', '1986-08-09', 8, '2023-09-20'),
    ('Lucas', 'Clark', 'Director', '111-222-3333', 'lucas.clark@example.com',
     'Leading automotive parts sales and distribution.', '1984-02-05', 9, '2023-09-20'),

    ('Sophia', 'Garcia', 'Financial Director', '222-333-4444', 'sophia.garcia@example.com',
     'Overseeing financial aspects of auto parts sales.', '1989-07-14', 9, '2023-09-20'),
    ('Ava', 'Brown', 'Chief Accountant', '333-444-5555', 'ava.brown@example.com',
     'Managing financial records in the automotive industry.', '1983-12-18', 9, '2023-09-20'),
    ('Oliver', 'Martinez', 'Procurement Manager', '444-555-6666', 'oliver.martinez@example.com',
     'Handling procurement for auto parts and supplies.', '1991-05-31', 9, '2023-09-20'),
    ('Noah', 'Smith', 'Secretary', '555-666-7777', 'noah.smith@example.com',
     'Providing administrative support in the automotive field.', '1995-09-10', 9, '2023-09-20'),
    ('Emma', 'Johnson', 'Director', '666-777-8888', 'emma.johnson@example.com',
     'Leading food and culinary innovations.', '1988-11-03', 10, '2023-09-20'),

    ('Liam', 'Martinez', 'Financial Director', '777-888-9999', 'liam.martinez@example.com',
     'Overseeing financial planning for food projects.', '1981-04-12', 10, '2023-09-20'),
    ('Ava', 'Wilson', 'Chief Accountant', '888-999-0000', 'ava.wilson@example.com',
     'Managing financial records in the food industry.', '1985-03-29', 10, '2023-09-20'),
    ('Oliver', 'Smith', 'Procurement Manager', '999-000-1111', 'oliver.smith@example.com',
     'Handling procurement for food ingredients and supplies.', '1990-10-06', 10, '2023-09-20'),
    ('Mia', 'Davis', 'Secretary', '111-222-3333', 'mia.davis@example.com',
     'Providing administrative support in the food industry.', '1982-08-01', 10, '2023-09-20'),
    ('Chloe', 'Brown', 'Director', '111-222-3333', 'chloe.brown@example.com',
     'Leading construction projects and development.', '1987-09-14', 11, '2023-09-20'),

    ('Sophia', 'Smith', 'Financial Director', '222-333-4444', 'sophia.smith@example.com',
     'Overseeing financial planning for construction ventures.', '1984-05-25', 11, '2023-09-20'),
    ('Oliver', 'Martinez', 'Chief Accountant', '333-444-5555', 'oliver.martinez@example.com',
     'Managing financial records in the construction industry.', '1981-07-08', 11, '2023-09-20'),
    ('Noah', 'Garcia', 'Procurement Manager', '444-555-6666', 'noah.garcia@example.com',
     'Handling procurement for construction materials and equipment.', '1989-03-12', 11, '2023-09-20'),
    ('Mia', 'Davis', 'Secretary', '555-666-7777', 'mia.davis@example.com',
     'Providing administrative support to the construction team.', '1994-01-28', 11, '2023-09-20'),
    ('Liam', 'Clark', 'Director', '666-777-8888', 'liam.clark@example.com',
     'Leading eco-friendly technology and innovations.', '1982-12-02', 12, '2023-09-20'),

    ('Chloe', 'Wilson', 'Financial Director', '777-888-9999', 'chloe.wilson@example.com',
     'Overseeing financial aspects of eco-tech projects.', '1983-04-21', 12, '2023-09-20'),
    ('Sophie', 'Smith', 'Chief Accountant', '888-999-0000', 'sophie.smith@example.com',
     'Managing financial records in the eco-tech sector.', '1986-06-05', 12, '2023-09-20'),
    ('Oliver', 'Davis', 'Procurement Manager', '999-000-1111', 'oliver.davis@example.com',
     'Handling procurement for eco-tech components and materials.', '1991-09-16', 12, '2023-09-20'),
    ('Mia', 'Garcia', 'Secretary', '111-222-3333', 'mia.garcia@example.com',
     'Providing administrative support in the eco-tech field.', '1993-02-27', 12, '2023-09-20'),
    ('Emma', 'Brown', 'Director', '111-222-3333', 'emma.brown@example.com',
     'Leading software development and IT solutions.', '1980-11-19', 13, '2023-09-20'),

    ('Noah', 'Wilson', 'Financial Director', '222-333-4444', 'noah.wilson@example.com',
     'Overseeing financial planning for software projects.', '1985-08-22', 13, '2023-09-20'),
    ('Sophie', 'Davis', 'Chief Accountant', '333-444-5555', 'sophie.davis@example.com',
     'Managing financial records in the software industry.', '1982-07-07', 13, '2023-09-20'),
    ('Liam', 'Smith', 'Procurement Manager', '444-555-6666', 'liam.smith@example.com',
     'Handling procurement for software components and licenses.', '1989-01-14', 13, '2023-09-20'),
    ('Ava', 'Martinez', 'Secretary', '555-666-7777', 'ava.martinez@example.com',
     'Providing administrative support in the software field.', '1992-04-25', 13, '2023-09-20'),
    ('Oliver', 'Brown', 'Director', '666-777-8888', 'oliver.brown@example.com',
     'Leading health and fitness initiatives and services.', '1984-09-30', 14, '2023-09-20'),

    ('Sophie', 'Smith', 'Financial Director', '777-888-9999', 'sophie.smith@example.com',
     'Overseeing financial planning for health and fitness programs.', '1983-06-11', 14, '2023-09-20'),
    ('Noah', 'Garcia', 'Chief Accountant', '888-999-0000', 'noah.garcia@example.com',
     'Managing financial records in the health and fitness sector.', '1982-01-07', 14, '2023-09-20'),
    ('Mia', 'Davis', 'Procurement Manager', '999-000-1111', 'mia.davis@example.com',
     'Handling procurement for fitness equipment and supplies.', '1989-12-09', 14, '2023-09-20'),
    ('Liam', 'Martinez', 'Secretary', '111-222-3333', 'liam.martinez@example.com',
     'Providing administrative support to the health and fitness team.', '1995-07-14', 14, '2023-09-20'),
    ('Ava', 'Clark', 'Director', '666-777-8888', 'ava.clark@example.com',
     'Leading home decor and interior design projects.', '1981-03-01', 15, '2023-09-20'),

    ('Sophie', 'Martinez', 'Financial Director', '777-888-9999', 'sophie.martinez@example.com',
     'Overseeing financial planning for home decor ventures.', '1984-02-14', 15, '2023-09-20'),
    ('Noah', 'Garcia', 'Chief Accountant', '888-999-0000', 'noah.garcia@example.com',
     'Managing financial records in the home decor industry.', '1987-11-03', 15, '2023-09-20'),
    ('Oliver', 'Wilson', 'Procurement Manager', '999-000-1111', 'oliver.wilson@example.com',
     'Handling procurement for home decor items and furnishings.', '1990-06-18', 15, '2023-09-20'),
    ('Chloe', 'Brown', 'Secretary', '111-222-3333', 'chloe.brown@example.com',
     'Providing administrative support to the home decor team.', '1993-10-22', 15, '2023-09-20'),
    ('Liam', 'Smith', 'Director', '111-222-3333', 'liam.smith@example.com',
     'Leading technological innovations and IT solutions.', '1980-12-12', 16, '2023-09-20'),

    ('Mia', 'Garcia', 'Financial Director', '222-333-4444', 'mia.garcia@example.com',
     'Overseeing financial planning for tech projects.', '1983-04-30', 16, '2023-09-20'),
    ('Sophie', 'Davis', 'Chief Accountant', '333-444-5555', 'sophie.davis@example.com',
     'Managing financial records in the tech industry.', '1982-05-15', 16, '2023-09-20'),
    ('Noah', 'Wilson', 'Procurement Manager', '444-555-6666', 'noah.wilson@example.com',
     'Handling procurement for tech components and licenses.', '1990-09-05', 16, '2023-09-20'),
    ('Chloe', 'Brown', 'Secretary', '555-666-7777', 'chloe.brown@example.com',
     'Providing administrative support in the tech field.', '1993-03-25', 16, '2023-09-20'),
    ('Oliver', 'Smith', 'Director', '666-777-8888', 'oliver.smith@example.com',
     'Leading educational and e-learning initiatives.', '1981-08-10', 17, '2023-09-20'),

    ('Mia', 'Martinez', 'Financial Director', '777-888-9999', 'mia.martinez@example.com',
     'Overseeing financial planning for educational programs.', '1985-06-29', 17, '2023-09-20'),
    ('Sophie', 'Wilson', 'Chief Accountant', '888-999-0000', 'sophie.wilson@example.com',
     'Managing financial records in the education sector.', '1982-09-20', 17, '2023-09-20'),
    ('Noah', 'Davis', 'Procurement Manager', '999-000-1111', 'noah.davis@example.com',
     'Handling procurement for educational materials and resources.', '1990-11-12', 17, '2023-09-20'),
    ('Liam', 'Clark', 'Secretary', '111-222-3333', 'liam.clark@example.com',
     'Providing administrative support to the education team.', '1993-07-07', 17, '2023-09-20'),
    ('Ava', 'Smith', 'Director', '666-777-8888', 'ava.smith@example.com',
     'Leading artistic and creative projects.', '1984-12-15', 18, '2023-09-20'),

    ('Chloe', 'Martinez', 'Financial Director', '777-888-9999', 'chloe.martinez@example.com',
     'Overseeing financial planning for artistry ventures.', '1983-03-28', 18, '2023-09-20'),
    ('Mia', 'Garcia', 'Chief Accountant', '888-999-0000', 'mia.garcia@example.com',
     'Managing financial records in the artistry industry.', '1981-02-18', 18, '2023-09-20'),
    ('Noah', 'Wilson', 'Procurement Manager', '999-000-1111', 'noah.wilson@example.com',
     'Handling procurement for artistic materials and supplies.', '1990-10-02', 18, '2023-09-20'),
    ('Sophie', 'Brown', 'Secretary', '111-222-3333', 'sophie.brown@example.com',
     'Providing administrative support to the artistry team.', '1993-04-14', 18, '2023-09-20'),
    ('Emma', 'Johnson', 'Director', '666-777-8888', 'emma.johnson@example.com',
     'Leading sustainable energy and green power projects.', '1982-11-05', 19, '2023-09-20'),

    ('Noah', 'Garcia', 'Financial Director', '777-888-9999', 'noah.garcia@example.com',
     'Overseeing financial planning for green power initiatives.', '1984-01-27', 19, '2023-09-20'),
    ('Sophia', 'Brown', 'Chief Accountant', '888-999-0000', 'sophia.brown@example.com',
     'Managing financial records in the green energy sector.', '1981-12-08', 19, '2023-09-20'),
    ('Ava', 'Martinez', 'Procurement Manager', '999-000-1111', 'ava.martinez@example.com',
     'Handling procurement for green energy equipment and resources.', '1990-07-19', 19, '2023-09-20'),
    ('Oliver', 'Smith', 'Secretary', '111-222-3333', 'oliver.smith@example.com',
     'Providing administrative support to the green energy team.', '1993-08-30', 19, '2023-09-20'),
    ('Chloe', 'Wilson', 'Director', '666-777-8888', 'chloe.wilson@example.com',
     'Leading travel and adventure expeditions.', '1980-10-12', 20, '2023-09-20'),

    ('Noah', 'Davis', 'Financial Director', '777-888-9999', 'noah.davis@example.com',
     'Overseeing financial planning for travel experiences.', '1983-07-24', 20, '2023-09-20'),
    ('Sophie', 'Smith', 'Chief Accountant', '888-999-0000', 'sophie.smith@example.com',
     'Managing financial records in the travel industry.', '1981-05-06', 20, '2023-09-20'),
    ('Mia', 'Martinez', 'Procurement Manager', '999-000-1111', 'mia.martinez@example.com',
     'Handling procurement for travel accommodations and services.', '1990-02-18', 20, '2023-09-20'),
    ('Liam', 'Garcia', 'Secretary', '111-222-3333', 'liam.garcia@example.com',
     'Providing administrative support to the travel enthusiasts team.', '1993-12-30', 20, '2023-09-20'),
    ('Oliver', 'Smith', 'Director', '666-777-8888', 'oliver.smith@example.com',
     'Leading financial advisory and consulting services.', '1981-08-10', 21, '2023-09-20'),

    ('Mia', 'Garcia', 'Financial Director', '777-888-9999', 'mia.garcia@example.com',
     'Overseeing financial planning for clients.', '1985-06-29', 21, '2023-09-20'),
    ('Sophie', 'Wilson', 'Chief Accountant', '888-999-0000', 'sophie.wilson@example.com',
     'Managing financial records for advisory firm.', '1982-09-20', 21, '2023-09-20'),
    ('Noah', 'Davis', 'Procurement Manager', '999-000-1111', 'noah.davis@example.com',
     'Handling procurement for financial consultancy.', '1990-11-12', 21, '2023-09-20'),
    ('Liam', 'Clark', 'Secretary', '111-222-3333', 'liam.clark@example.com',
     'Providing administrative support to financial advisors.', '1993-07-07', 21, '2023-09-20'),
    ('Ava', 'Smith', 'Director', '666-777-8888', 'ava.smith@example.com',
     'Leading luxury home decor and interior design projects.', '1984-12-15', 22, '2023-09-20'),

    ('Chloe', 'Martinez', 'Financial Director', '777-888-9999', 'chloe.martinez@example.com',
     'Overseeing financial planning for luxury decor ventures.', '1983-03-28', 22, '2023-09-20'),
    ('Mia', 'Garcia', 'Chief Accountant', '888-999-0000', 'mia.garcia@example.com',
     'Managing financial records in the luxury decor industry.', '1981-02-18', 22, '2023-09-20'),
    ('Noah', 'Wilson', 'Procurement Manager', '999-000-1111', 'noah.wilson@example.com',
     'Handling procurement for luxury decor items and furnishings.', '1990-10-02', 22, '2023-09-20'),
    ('Sophie', 'Brown', 'Secretary', '111-222-3333', 'sophie.brown@example.com',
     'Providing administrative support to the luxury decor team.', '1993-04-14', 22, '2023-09-20')
    #  Добавьте другие данные, которые вы хотите вставить
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

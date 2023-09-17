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
insert_query = "INSERT INTO co_crm.website_companies (name, phone, email, address, city, state, zipcode, industry, website,year_founded, number_of_employees, manager_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Пример данных, которые нужно вставить в таблицу
data_to_insert = [
    ('Tech Solutions Inc.', '111-222-3333', 'info@techsolutions.com', '123 Main St',
     'New York', 'NY', '10001', 'Technology', 'www.techsolutions.com', 1990, 100, 5),
    ('HealthCare Innovations', '222-333-4444', 'contact@healthcareinnovations.com', '456 Elm St',
     'Los Angeles', 'CA', '90001', 'Healthcare', 'www.healthcareinnovations.com', 2000, 150, 6),
    ('Finance Pro', '333-444-5555', 'info@financepro.com', '789 Oak St',
     'Chicago', 'IL', '60001', 'Finance', 'www.financepro.com', 1985, 200, 7),
    ('Retail Express', '444-555-6666', 'contact@retailexpress.com', '101 Pine St',
     'Houston', 'TX', '77001', 'Retail', 'www.retailexpress.com', 2010, 50, 8),
    ('Global Logistics', '555-666-7777', 'info@globallogistics.com', '234 Cedar St',
     'San Francisco', 'CA', '94101', 'Logistics', 'www.globallogistics.com', 2005, 75, 8),
    ('Data Analytics Corp.', '666-777-8888', 'contact@dataanalyticscorp.com', '567 Birch St',
     'Seattle', 'WA', '98101', 'Data Analytics', 'www.dataanalyticscorp.com', 2015, 30, 10),
    ('Green Energy Solutions', '777-888-9999', 'info@greenenergysolutions.com', '890 Spruce St',
     'Boston', 'MA', '02201', 'Renewable Energy', 'www.greenenergysolutions.com', 2008, 80, 11),
    ('Fashion Hub', '888-999-0000', 'contact@fashionhub.com', '123 Rose St',
     'Miami', 'FL', '33101', 'Fashion', 'www.fashionhub.com', 1995, 120, 12),
    ('Auto Parts Express', '999-000-1111', 'info@autopartsexpress.com', '456 Maple St',
     'Dallas', 'TX', '75201', 'Automotive', 'www.autopartsexpress.com', 2002, 95, 13),
    ('Food Delights Inc.', '123-456-7890', 'contact@fooddelightsinc.com', '789 Oak St',
     'Chicago', 'IL', '60001', 'Food & Beverage', 'www.fooddelightsinc.com', 1998, 160, 5),
    ('Construction Pros', '234-567-8901', 'info@constructionpros.com', '101 Pine St',
     'Houston', 'TX', '77001', 'Construction', 'www.constructionpros.com', 2012, 45, 6),
    ('EcoTech Innovations', '345-678-9012', 'contact@ecotechinnovations.com', '234 Elm St',
     'Los Angeles', 'CA', '90001', 'Green Technology', 'www.ecotechinnovations.com', 2017, 25, 7),
    ('Software Wizards', '456-789-0123', 'info@softwarewizards.com', '567 Cedar St', 'San Francisco',
     'CA', '94101', 'Software Development', 'www.softwarewizards.com', 2007, 70, 8),
    ('Health & Fitness Pro', '567-890-1234', 'contact@healthfitnesspro.com', '890 Birch St',
     'Seattle', 'WA', '98101', 'Health & Fitness', 'www.healthfitnesspro.com', 2011, 85, 9),
    ('Home Decor Experts', '678-901-2345', 'info@homedecorexperts.com', '123 Pine St',
     'Miami', 'FL', '33101', 'Home Decor', 'www.homedecorexperts.com', 2004, 110, 10),
    ('Tech Innovations', '789-012-3456', 'contact@techinnovations.com', '456 Oak St', 'Dallas',
     'TX', '75201', 'Innovative Technology', 'www.techinnovations.com', 2009, 65, 11),
    ('Educational Solutions', '890-123-4567', 'info@educationalsolutions.com', '101 Elm St',
     'New York', 'NY', '10001', 'Education', 'www.educationalsolutions.com', 1997, 140, 12),
    ('Artistry Creations', '901-234-5678', 'contact@artistrycreations.com', '234 Cedar St',
     'Chicago', 'IL', '60001', 'Art & Design', 'www.artistrycreations.com', 2001, 75, 13),
    ('Green Power Systems', '012-345-6789', 'info@greenpowersystems.com', '789 Spruce St',
     'Los Angeles', 'CA', '90001', 'Renewable Energy', 'www.greenpowersystems.com', 2014, 40, 5),
    ('Travel Enthusiasts', '123-234-5678', 'contact@travelenthusiasts.com', '890 Rose St',
     'San Francisco', 'CA', '94101', 'Travel & Tourism', 'www.travelenthusiasts.com', 2003, 90, 6),
    ('Financial Solutions Inc.', '234-345-6789', 'info@financialsolutionsinc.com', '123 Birch St',
     'Houston', 'TX', '77001', 'Financial Services', 'www.financialsolutionsinc.com', 2018, 55, 7),
    ('Home Appliances Plus', '345-456-7890', 'contact@homeappliancesplus.com', '456 Maple St',
     'Boston', 'MA', '02201', 'Home Appliances', 'www.homeappliancesplus.com', 2006, 120, 8),
    ('Food Delicacies', '456-567-8901', 'info@fooddelicacies.com', '234 Oak St',
     'Dallas', 'TX', '75201', 'Food & Beverage', 'www.fooddelicacies.com', 2013, 70, 9),
    ('Construction Masters', '567-678-9012', 'contact@constructionmasters.com', '101 Cedar St',
     'Miami', 'FL', '33101', 'Construction', 'www.constructionmasters.com', 2005, 35, 10),
    ('Tech Innovations', '678-789-0123', 'info@techinnovations.com', '567 Elm St',
     'New York', 'NY', '10001', 'Technology', 'www.techinnovations.com', 2010, 80, 11),
    ('EcoTech Solutions', '789-890-1234', 'contact@ecotechsolutions.com', '123 Pine St', 'Los Angeles',
     'CA', '90001', 'Eco-Friendly Technology', 'www.ecotechsolutions.com', 2015, 45, 12),
    ('Fashion Trends', '890-901-2345', 'info@fashiontrends.com', '456 Spruce St',
     'Chicago', 'IL', '60001', 'Fashion', 'www.fashiontrends.com', 2002, 100, 13),
    ('Automotive Experts', '901-012-3456', 'contact@automotiveexperts.com', '101 Rose St',
     'San Francisco', 'CA', '94101', 'Automotive', 'www.automotiveexperts.com', 2008, 65, 1),
    ('Home Decor Creations', '012-123-2345', 'info@homedecorcreations.com', '890 Birch St',
     'Houston', 'TX', '77001', 'Home Decor', 'www.homedecorcreations.com', 2007, 75, 2),
    ('Green Energy Solutions', '123-234-3456', 'contact@greenenergysolutions.com', '234 Cedar St',
     'Miami', 'FL', '33101', 'Renewable Energy', 'www.greenenergysolutions.com', 2011, 85, 3),
    ('Global Travel Agency', '234-345-4567', 'info@globaltravelagency.com', '567 Oak St',
     'Dallas', 'TX', '75201', 'Travel & Tourism', 'www.globaltravelagency.com', 2004, 40, 4),
    ('Financial Advisors Inc.', '345-456-5678', 'contact@financialadvisorsinc.com', '101 Elm St',
     'New York', 'NY', '10001', 'Financial Services', 'www.financialadvisorsinc.com', 1998, 70, 1),
    ('Luxury Home Decor', '456-567-6789', 'info@luxuryhomedecor.com', '789 Pine St',
     'Chicago', 'IL', '60001', 'Home Decor', 'www.luxuryhomedecor.com', 2009, 110, 2),
    ('GreenTech Innovations', '567-678-7890', 'contact@greentechinnovations.com', '234 Maple St',
     'Los Angeles', 'CA', '90001', 'Green Technology', 'www.greentechinnovations.com', 2017, 30, 3),
    ('Healthy Living', '678-789-8901', 'info@healthyliving.com', '567 Rose St', 'San Francisco',
     'CA', '94101', 'Health & Wellness', 'www.healthyliving.com', 2012, 65, 4),
    # Добавьте другие данные, которые вы хотите вставить
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

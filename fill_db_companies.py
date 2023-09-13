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
     'New York', 'NY', '10001', 'Technology', 'www.techsolutions.com', 1990, 100, 6),
    ('HealthCare Innovations', '222-333-4444', 'contact@healthcareinnovations.com', '456 Elm St',
     'Los Angeles', 'CA', '90001', 'Healthcare', 'www.healthcareinnovations.com', 2000, 150, 10),
    ('Finance Pro', '333-444-5555', 'info@financepro.com', '789 Oak St',
     'Chicago', 'IL', '60001', 'Finance', 'www.financepro.com', 1985, 200, 14),
    ('Retail Express', '444-555-6666', 'contact@retailexpress.com', '101 Pine St',
     'Houston', 'TX', '77001', 'Retail', 'www.retailexpress.com', 2010, 50, 18),
    ('Global Logistics', '555-666-7777', 'info@globallogistics.com', '234 Cedar St',
     'San Francisco', 'CA', '94101', 'Logistics', 'www.globallogistics.com', 2005, 75, 22),
    ('Data Analytics Corp.', '666-777-8888', 'contact@dataanalyticscorp.com', '567 Birch St',
     'Seattle', 'WA', '98101', 'Data Analytics', 'www.dataanalyticscorp.com', 2015, 30, 26),
    ('Green Energy Solutions', '777-888-9999', 'info@greenenergysolutions.com', '890 Spruce St',
     'Boston', 'MA', '02201', 'Renewable Energy', 'www.greenenergysolutions.com', 2008, 80, 30),
    ('Fashion Hub', '888-999-0000', 'contact@fashionhub.com', '123 Rose St',
     'Miami', 'FL', '33101', 'Fashion', 'www.fashionhub.com', 1995, 120, 6),
    ('Auto Parts Express', '999-000-1111', 'info@autopartsexpress.com', '456 Maple St',
     'Dallas', 'TX', '75201', 'Automotive', 'www.autopartsexpress.com', 2002, 95, 10),
    ('Food Delights Inc.', '123-456-7890', 'contact@fooddelightsinc.com', '789 Oak St',
     'Chicago', 'IL', '60001', 'Food & Beverage', 'www.fooddelightsinc.com', 1998, 160, 14),
    ('Construction Pros', '234-567-8901', 'info@constructionpros.com', '101 Pine St',
     'Houston', 'TX', '77001', 'Construction', 'www.constructionpros.com', 2012, 45, 18),
    ('EcoTech Innovations', '345-678-9012', 'contact@ecotechinnovations.com', '234 Elm St',
     'Los Angeles', 'CA', '90001', 'Green Technology', 'www.ecotechinnovations.com', 2017, 25, 22),
    ('Software Wizards', '456-789-0123', 'info@softwarewizards.com', '567 Cedar St', 'San Francisco',
     'CA', '94101', 'Software Development', 'www.softwarewizards.com', 2007, 70, 26),
    ('Health & Fitness Pro', '567-890-1234', 'contact@healthfitnesspro.com', '890 Birch St',
     'Seattle', 'WA', '98101', 'Health & Fitness', 'www.healthfitnesspro.com', 2011, 85, 30),
    ('Home Decor Experts', '678-901-2345', 'info@homedecorexperts.com', '123 Pine St',
     'Miami', 'FL', '33101', 'Home Decor', 'www.homedecorexperts.com', 2004, 110, 6),
    ('Tech Innovations', '789-012-3456', 'contact@techinnovations.com', '456 Oak St', 'Dallas',
     'TX', '75201', 'Innovative Technology', 'www.techinnovations.com', 2009, 65, 10),
    ('Educational Solutions', '890-123-4567', 'info@educationalsolutions.com', '101 Elm St',
     'New York', 'NY', '10001', 'Education', 'www.educationalsolutions.com', 1997, 140, 14),
    ('Artistry Creations', '901-234-5678', 'contact@artistrycreations.com', '234 Cedar St',
     'Chicago', 'IL', '60001', 'Art & Design', 'www.artistrycreations.com', 2001, 75, 18),
    ('Green Power Systems', '012-345-6789', 'info@greenpowersystems.com', '789 Spruce St',
     'Los Angeles', 'CA', '90001', 'Renewable Energy', 'www.greenpowersystems.com', 2014, 40, 22),
    ('Travel Enthusiasts', '123-234-5678', 'contact@travelenthusiasts.com', '890 Rose St',
     'San Francisco', 'CA', '94101', 'Travel & Tourism', 'www.travelenthusiasts.com', 2003, 90, 26),
    ('Financial Solutions Inc.', '234-345-6789', 'info@financialsolutionsinc.com', '123 Birch St',
     'Houston', 'TX', '77001', 'Financial Services', 'www.financialsolutionsinc.com', 2018, 55, 30),
    ('Home Appliances Plus', '345-456-7890', 'contact@homeappliancesplus.com', '456 Maple St',
     'Boston', 'MA', '02201', 'Home Appliances', 'www.homeappliancesplus.com', 2006, 120, 6),
    ('Food Delicacies', '456-567-8901', 'info@fooddelicacies.com', '234 Oak St',
     'Dallas', 'TX', '75201', 'Food & Beverage', 'www.fooddelicacies.com', 2013, 70, 10),
    ('Construction Masters', '567-678-9012', 'contact@constructionmasters.com', '101 Cedar St',
     'Miami', 'FL', '33101', 'Construction', 'www.constructionmasters.com', 2005, 35, 14),
    ('Tech Innovations', '678-789-0123', 'info@techinnovations.com', '567 Elm St',
     'New York', 'NY', '10001', 'Technology', 'www.techinnovations.com', 2010, 80, 18),
    ('EcoTech Solutions', '789-890-1234', 'contact@ecotechsolutions.com', '123 Pine St', 'Los Angeles',
     'CA', '90001', 'Eco-Friendly Technology', 'www.ecotechsolutions.com', 2015, 45, 22),
    ('Fashion Trends', '890-901-2345', 'info@fashiontrends.com', '456 Spruce St',
     'Chicago', 'IL', '60001', 'Fashion', 'www.fashiontrends.com', 2002, 100, 26),
    ('Automotive Experts', '901-012-3456', 'contact@automotiveexperts.com', '101 Rose St',
     'San Francisco', 'CA', '94101', 'Automotive', 'www.automotiveexperts.com', 2008, 65, 30),
    ('Home Decor Creations', '012-123-2345', 'info@homedecorcreations.com', '890 Birch St',
     'Houston', 'TX', '77001', 'Home Decor', 'www.homedecorcreations.com', 2007, 75, 6),
    ('Green Energy Solutions', '123-234-3456', 'contact@greenenergysolutions.com', '234 Cedar St',
     'Miami', 'FL', '33101', 'Renewable Energy', 'www.greenenergysolutions.com', 2011, 85, 10),
    ('Global Travel Agency', '234-345-4567', 'info@globaltravelagency.com', '567 Oak St',
     'Dallas', 'TX', '75201', 'Travel & Tourism', 'www.globaltravelagency.com', 2004, 40, 14),
    ('Financial Advisors Inc.', '345-456-5678', 'contact@financialadvisorsinc.com', '101 Elm St',
     'New York', 'NY', '10001', 'Financial Services', 'www.financialadvisorsinc.com', 1998, 70, 18),
    ('Luxury Home Decor', '456-567-6789', 'info@luxuryhomedecor.com', '789 Pine St',
     'Chicago', 'IL', '60001', 'Home Decor', 'www.luxuryhomedecor.com', 2009, 110, 22),
    ('GreenTech Innovations', '567-678-7890', 'contact@greentechinnovations.com', '234 Maple St',
     'Los Angeles', 'CA', '90001', 'Green Technology', 'www.greentechinnovations.com', 2017, 30, 26),
    ('Healthy Living', '678-789-8901', 'info@healthyliving.com', '567 Rose St', 'San Francisco',
     'CA', '94101', 'Health & Wellness', 'www.healthyliving.com', 2012, 65, 30),
    ('Interior Design Masters', '789-890-9012', 'contact@interiordesignmasters.com', '234 Cedar St',
     'Miami', 'FL', '33101', 'Interior Design', 'www.interiordesignmasters.com', 2008, 90, 10),
    ('Smart Home Solutions', '890-901-0123', 'info@smarthomesolutions.com', '101 Spruce St',
     'Dallas', 'TX', '75201', 'Smart Home Technology', 'www.smarthomesolutions.com', 2013, 75, 14),
    ('Healthy Eats', '901-012-1234', 'contact@healthyeats.com', '456 Birch St',
     'New York', 'NY', '10001', 'Food & Nutrition', 'www.healthyeats.com', 2006, 50, 18),
    ('Travel Explorers', '012-123-2345', 'info@travelexplorers.com', '567 Elm St', 'Chicago',
     'IL', '60001', 'Travel & Adventure', 'www.travelexplorers.com', 2010, 80, 22),
    ('Home Renovation Pros', '123-234-3456', 'contact@homerenovationpros.com', '101 Oak St',
     'Los Angeles', 'CA', '90001', 'Home Renovation', 'www.homerenovationpros.com', 2005, 65, 26),
    ('Tech Solutions Group', '234-345-4567', 'info@techsolutionsgroup.com', '789 Cedar St',
     'San Francisco', 'CA', '94101', 'Technology Solutions', 'www.techsolutionsgroup.com', 2007, 75, 30),
    ('Green Energy Innovations', '345-456-5678', 'contact@greenenergyinnovations.com', '234 Pine St',
     'Houston', 'TX', '77001', 'Green Energy', 'www.greenenergyinnovations.com', 2011, 40, 6),
    ('Fashionistas', '456-567-6789', 'info@fashionistas.com', '890 Rose St', 'Miami',
     'FL', '33101', 'Fashion & Style', 'www.fashionistas.com', 2015, 60, 10),
    ('Digital Marketing Pros', '567-678-7890', 'contact@digitalmarketingpros.com', '456 Cedar St',
     'Dallas', 'TX', '75201', 'Digital Marketing', 'www.digitalmarketingpros.com', 2018, 50, 14),
    ('Home Improvement Masters', '678-789-8901', 'info@homeimprovementmasters.com', '101 Oak St',
     'New York', 'NY', '10001', 'Home Improvement', 'www.homeimprovementmasters.com', 2002, 95, 18),
    ('Outdoor Adventure Co.', '789-890-9012', 'contact@outdooradventureco.com', '234 Elm St',
     'Chicago', 'IL', '60001', 'Outdoor Recreation', 'www.outdooradventureco.com', 2003, 45, 22),
    ('Healthy Habits', '890-901-0123', 'info@healthyhabits.com', '567 Pine St', 'Los Angeles',
     'CA', '90001', 'Health & Lifestyle', 'www.healthyhabits.com', 2016, 70, 26),
    ('Tech Solutions Inc.', '901-012-1234', 'contact@techsolutionsinc.com', '101 Spruce St',
     'San Francisco', 'CA', '94101', 'Technology Services', 'www.techsolutionsinc.com', 2004, 55, 30),
    ('Home Renovation Experts', '012-123-2345', 'info@homerenovationexperts.com', '456 Birch St',
     'Miami', 'FL', '33101', 'Home Renovation', 'www.homerenovationexperts.com', 2009, 85, 6),
    ('Eco-Friendly Innovations', '123-234-3456', 'contact@ecofriendlyinnovations.com', '890 Cedar St',
     'Dallas', 'TX', '75201', 'Eco-Friendly Technology', 'www.ecofriendlyinnovations.com', 2001, 40, 10),
    ('Healthy You', '234-345-4567', 'info@healthyyou.com', '101 Oak St', 'New York',
     'NY', '10001', 'Health & Wellness', 'www.healthyyou.com', 2014, 60, 14),
    ('Tech Innovators', '345-456-5678', 'contact@techinnovators.com', '234 Elm St', 'Chicago',
     'IL', '60001', 'Technology Solutions', 'www.techinnovators.com', 2015, 75, 18),
    ('Green Living Co.', '456-567-6789', 'info@greenlivingco.com', '567 Pine St',
     'Los Angeles', 'CA', '90001', 'Green Living', 'www.greenlivingco.com', 2006, 90, 22),
    ('Travel Enthusiasts', '567-678-7890', 'contact@travelenthusiasts.com', '789 Cedar St',
     'San Francisco', 'CA', '94101', 'Travel & Adventure', 'www.travelenthusiasts.com', 2003, 40, 26),
    ('Home Improvement Gurus', '678-789-8901', 'info@homeimprovementgurus.com', '101 Oak St',
     'Miami', 'FL', '33101', 'Home Improvement', 'www.homeimprovementgurus.com', 2007, 70, 30),
    ('Fashion Forward', '789-890-9012', 'contact@fashionforward.com', '234 Elm St',
     'Dallas', 'TX', '75201', 'Fashion & Style', 'www.fashionforward.com', 2010, 55, 6),
    ('Digital Marketing Experts', '890-901-0123', 'info@digitalmarketingexperts.com', '567 Pine St',
     'New York', 'NY', '10001', 'Digital Marketing', 'www.digitalmarketingexperts.com', 2012, 65, 10),
    ('Outdoor Adventure Seekers', '901-012-1234', 'contact@outdooradventureseekers.com', '890 Cedar St',
     'Chicago', 'IL', '60001', 'Outdoor Recreation', 'www.outdooradventureseekers.com', 2008, 75, 14),
    ('Healthy Choices', '012-123-2345', 'info@healthychoices.com', '101 Oak St', 'Los Angeles',
     'CA', '90001', 'Health & Lifestyle', 'www.healthychoices.com', 2011, 50, 18),
    ('Tech Solutions Pro', '123-234-3456', 'contact@techsolutionspro.com', '234 Elm St',
     'San Francisco', 'CA', '94101', 'Technology Services', 'www.techsolutionspro.com', 2013, 80, 22),
    ('Eco-Friendly Innovators', '234-345-4567', 'info@ecofriendlyinnovators.com', '567 Pine St',
     'Miami', 'FL', '33101', 'Eco-Friendly Technology', 'www.ecofriendlyinnovators.com', 2005, 40, 26),
    ('Healthy Living Solutions', '345-456-5678', 'contact@healthylivingsolutions.com', '890 Cedar St',
     'Dallas', 'TX', '75201', 'Health & Wellness', 'www.healthylivingsolutions.com', 2016, 75, 30),
    ('Tech Innovations Group', '456-567-6789', 'info@techinnovationsgroup.com', '101 Oak St',
     'New York', 'NY', '10001', 'Technology Solutions', 'www.techinnovationsgroup.com', 2002, 60, 6),
    ('Green Energy Pioneers', '567-678-7890', 'contact@greenenergypioneers.com', '234 Elm St',
     'Chicago', 'IL', '60001', 'Green Energy', 'www.greenenergypioneers.com', 2001, 50, 10),
    ('Fashionistas United', '678-789-8901', 'info@fashionistasunited.com', '567 Pine St',
     'Los Angeles', 'CA', '90001', 'Fashion & Style', 'www.fashionistasunited.com', 2004, 90, 14),
    ('Digital Marketing Masters', '789-890-9012', 'contact@digitalmarketingmasters.com', '101 Oak St',
     'San Francisco', 'CA', '94101', 'Digital Marketing', 'www.digitalmarketingmasters.com', 2009, 45, 18),
    ('Home Improvement Specialists', '890-901-0123', 'info@homeimprovementspecialists.com', '234 Elm St',
     'Miami', 'FL', '33101', 'Home Improvement', 'www.homeimprovementspecialists.com', 2008, 80, 22),
    ('Outdoor Adventure Lovers', '901-012-1234', 'contact@outdooradventurelovers.com', '890 Cedar St',
     'Dallas', 'TX', '75201', 'Outdoor Recreation', 'www.outdooradventurelovers.com', 2015, 55, 26),
    ('Healthy Habits Inc.', '012-123-2345', 'info@healthyhabitsinc.com', '101 Oak St',
     'New York', 'NY', '10001', 'Health & Lifestyle', 'www.healthyhabitsinc.com', 2006, 70, 30),
    ('Tech Solutions Experts', '123-234-3456', 'contact@techsolutionsexperts.com', '234 Elm St',
     'Chicago', 'IL', '60001', 'Technology Services', 'www.techsolutionsexperts.com', 2003, 85, 6),
    ('Eco-Friendly Innovations', '234-345-4567', 'info@ecofriendlyinnovations.com', '567 Pine St',
     'Los Angeles', 'CA', '90001', 'Eco-Friendly Technology', 'www.ecofriendlyinnovations.com', 2007, 75, 10),
    ('Healthy Living Experts', '345-456-5678', 'contact@healthylivingexperts.com', '890 Cedar St',
     'San Francisco', 'CA', '94101', 'Health & Wellness', 'www.healthylivingexperts.com', 2010, 60, 14),
    ('Tech Innovations Pro', '456-567-6789', 'info@techinnovationspro.com', '101 Oak St',
     'Miami', 'FL', '33101', 'Technology Solutions', 'www.techinnovationspro.com', 2009, 50, 18),
    ('Green Energy Visionaries', '567-678-7890', 'contact@greenenergyvisionaries.com', '234 Elm St',
     'Dallas', 'TX', '75201', 'Green Energy', 'www.greenenergyvisionaries.com', 2004, 45, 22),
    ('Fashion Forward Trends', '678-789-8901', 'info@fashionforwardtrends.com', '567 Pine St',
     'New York', 'NY', '10001', 'Fashion & Style', 'www.fashionforwardtrends.com', 2012, 40, 26),
    ('Digital Marketing Gurus', '789-890-9012', 'contact@digitalmarketinggurus.com', '101 Oak St',
     'Chicago', 'IL', '60001', 'Digital Marketing', 'www.digitalmarketinggurus.com', 2015, 70, 30),
    ('Outdoor Adventure Enthusiasts', '890-901-0123', 'info@outdooradventureenthusiasts.com', '234 Elm St',
     'Los Angeles', 'CA', '90001', 'Outdoor Recreation', 'www.outdooradventureenthusiasts.com', 2005, 55, 6),
    ('Healthy Lifestyle Co.', '901-012-1234', 'contact@healthylifestyleco.com', '890 Cedar St',
     'San Francisco', 'CA', '94101', 'Health & Lifestyle', 'www.healthylifestyleco.com', 2011, 65, 10),
    ('Tech Solutions Specialists', '012-123-2345', 'info@techsolutionsspecialists.com', '101 Oak St',
     'Miami', 'FL', '33101', 'Technology Services', 'www.techsolutionsspecialists.com', 2006, 80, 14),
    ('Eco-Friendly Tech Innovations', '123-234-3456', 'contact@ecofriendlytechinnovations.com', '567 Pine St',
     'Dallas', 'TX', '75201', 'Eco-Friendly Technology', 'www.ecofriendlytechinnovations.com', 2008, 90, 18),
    ('Healthy Habits Experts', '234-345-4567', 'info@healthyhabitsexperts.com', '101 Oak St',
     'New York', 'NY', '10001', 'Health & Wellness', 'www.healthyhabitsexperts.com', 2013, 40, 22),
    ('Tech Innovations Visionaries', '345-456-5678', 'contact@techinnovationsvisionaries.com', '234 Elm St',
     'Chicago', 'IL', '60001', 'Technology Solutions', 'www.techinnovationsvisionaries.com', 2016, 60, 26),
    ('Green Energy Pioneers Inc.', '456-567-6789', 'info@greenenergypioneersinc.com', '567 Pine St',
     'Los Angeles', 'CA', '90001', 'Green Energy', 'www.greenenergypioneersinc.com', 2001, 70, 30),
    ('Fashion Forward Trends', '567-678-7890', 'contact@fashionforwardtrends.com', '101 Oak St',
     'San Francisco', 'CA', '94101', 'Fashion & Style', 'www.fashionforwardtrends.com', 2010, 75, 6),
    ('Digital Marketing Masters', '678-789-8901', 'info@digitalmarketingmasters.com', '890 Cedar St',
     'Miami', 'FL', '33101', 'Digital Marketing', 'www.digitalmarketingmasters.com', 2003, 85, 10),
    ('Home Improvement Specialists', '789-890-9012', 'contact@homeimprovementspecialists.com', '567 Pine St',
     'Dallas', 'TX', '75201', 'Home Improvement', 'www.homeimprovementspecialists.com', 2007, 55, 14),
    ('Outdoor Adventure Lovers Inc.', '890-901-0123', 'info@outdooradventureloversinc.com', '234 Elm St',
     'New York', 'NY', '10001', 'Outdoor Recreation', 'www.outdooradventureloversinc.com', 2004, 70, 18),
    ('Healthy Choices Co.', '901-012-1234', 'contact@healthychoicesco.com', '101 Oak St',
     'Chicago', 'IL', '60001', 'Health & Lifestyle', 'www.healthychoicesco.com', 2015, 60, 22),
    ('Tech Solutions Pros', '012-123-2345', 'info@techsolutionspros.com', '890 Cedar St',
     'San Francisco', 'CA', '94101', 'Technology Services', 'www.techsolutionspros.com', 2012, 50, 26),
    ('Eco-Friendly Innovations Group', '123-234-3456', 'contact@ecofriendlyinnovationsgroup.com', '567 Pine St',
     'Miami', 'FL', '33101', 'Eco-Friendly Technology', 'www.ecofriendlyinnovationsgroup.com', 2006, 80, 30),
    ('Healthy Living Solutions Inc.', '234-345-4567', 'info@healthylivingsolutionsinc.com', '101 Oak St',
     'Dallas', 'TX', '75201', 'Health & Wellness', 'www.healthylivingsolutionsinc.com', 2008, 60, 6),
    # Добавьте другие данные, которые вы хотите вставить
]

# Вставляем данные в таблицу
cursor.executemany(insert_query, data_to_insert)

# Подтверждаем изменения в базе данных
connection.commit()

# Закрываем соединение
cursor.close()
connection.close()

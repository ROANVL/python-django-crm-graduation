import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host='localhost',
    user='roanvl',
    password='!And487052!',
    database='co_crm'
)

# Create a cursor for executing SQL queries
cursor = connection.cursor()

# Example SQL query to insert data into the table
insert_query = "INSERT INTO co_crm.website_orderstatus (name, description) VALUES (%s, %s)"

# Example data to insert into the table
data_to_insert = [
    ('New', 'Order created, not processed'),
    ('Processing', 'Order being processed'),
    ('Shipped', 'Order shipped to customer'),
    ('Delivered', 'Order successfully delivered'),
    ('Cancelled', 'Order cancelled'),
    ('Refunded', 'Payment refunded'),
    ('On Hold', 'Order on hold'),
    ('Pending Payment', 'Awaiting payment'),
    ('Completed', 'Order completed'),
    ('Returned', 'Items returned'),
    ('Partially Shipped', 'Partial shipment'),
    ('Back Ordered', 'Items on back order'),
    ('Disputed', 'Order dispute'),
    ('In Review', 'Under review'),
    ('Pending Fulfillment', 'Waiting to fulfill'),
    ('Pending Pickup', 'Ready for pickup'),
    ('Awaiting Shipment', 'Ready to ship'),
    ('Partially Delivered', 'Partial delivery'),
    ('Partially Returned', 'Partial return'),
    ('Awaiting Review', 'Awaiting review/approval'),
    ('Other', 'Other status')
]


# Insert the data into the table
cursor.executemany(insert_query, data_to_insert)

# Commit the changes to the database
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

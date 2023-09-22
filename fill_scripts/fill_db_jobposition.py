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
insert_query = "INSERT INTO co_crm.website_jobposition (title) VALUES (%s)"

# Example data to insert into the table
data_to_insert = [
    ("Commercial Director",),
    ("Head of Department",),
    ("Sales manager",),
]

# Insert the data into the table
cursor.executemany(insert_query, data_to_insert)

# Commit the changes to the database
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

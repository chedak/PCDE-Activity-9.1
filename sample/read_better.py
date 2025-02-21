import yaml
import mysql.connector

# Load the database configuration from the YAML file
with open('db.yaml', 'r') as file:
    db = yaml.safe_load(file)

# Create a configuration dictionary for the MySQL connection
config = {
    'user':     db['user'],
    'password': db['pwrd'],
    'host':     db['host'],
    'database': db['database'],
    'auth_plugin': 'mysql_native_password'
}

# Connect to the MySQL database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Execute a query to select all records from the "colleges" table
query = "SELECT * FROM colleges"
cursor.execute(query)

# Print all the records
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()

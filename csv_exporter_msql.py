import csv
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="PW",
    database="DATABSE_NAME"
)

# Execute a SELECT query to retrieve the table data
query = "SELECT * FROM TABLE_NAME"
cursor = conn.cursor()
cursor.execute(query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Get the column names from the cursor description
column_names = [desc[0] for desc in cursor.description]

# Define the output CSV file path
csv_file_path = "PATH"

# Write the data to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the column names as the header
    writer.writerow(column_names)
    
    # Write the data rows
    writer.writerows(rows)

# Close the cursor and the database connection
cursor.close()
conn.close()

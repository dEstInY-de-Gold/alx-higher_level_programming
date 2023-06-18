#!/usr/bin/python3

'''
A script that lists all cities from the database hbtn_0e_4_usa
Format: python list_cities.py <username> <password> <database_name>
'''

import sys
import MySQLdb
# Execute the SQL query to fetch all cities
query = "SELECT cities.id cities.name state.name FROM cities JOIN states\
        ON cities.state_id = state.id ORDER BY cities.id ASC"
cursor.execute(query)

# Fetch all the rows returned by the query
rows = cursor.fetchall()
if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = ms.connect(host='localhost', port=3306, user=username,
                    passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    c.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]

# Close the cursor and database connection
cursor.close()
db.close()

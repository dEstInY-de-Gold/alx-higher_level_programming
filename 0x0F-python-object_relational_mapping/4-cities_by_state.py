#!/usr/bin/python3

'''
A script that lists all cities from the database hbtn_0e_4_usa
Format: python list_cities.py <username> <password> <database_name>
'''

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                        passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    for city in cursor.fetchall():
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()

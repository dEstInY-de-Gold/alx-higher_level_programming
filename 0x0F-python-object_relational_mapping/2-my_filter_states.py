#!/usr/bin/python3

'''
A script that takes in an argument and displays all \
      values in the states table of hbtn_0e_0_usa \
      where name matches the argument.
Format: python search_states.py <username> <password> \
        <database_name> <state_name>
'''

import sys
import MySQLdb

if __name__ == '__main__':
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states matching the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

#!/usr/bin/python3

'''
A script that lists all states with a name starting with N \
      (upper N) from the database hbtn_0e_0_usa
Format: python3 list_states.py <username> <password> <database_name>
'''

import sys
import MySQLdb as ms

if __name__ == '__main__':
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = ms.connect(host='localhost', port=3306, user=username,
                    passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

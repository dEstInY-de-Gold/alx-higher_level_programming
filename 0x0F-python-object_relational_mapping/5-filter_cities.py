#!/usr/bin/python3

'''
A script that takes in the name of a state as an argument and lists all cities\
        of that state, using the database hbtn_0e_4_usa
Format: python list_cities_by_state.py <username> <password> <database_name>\
        <state_name>
'''

import sys
import MySQLdb as ms

if __name__ == '__main__':
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = ms.connect(host='localhost', port=3306, user=username,
                    passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch cities of the specified state
    cursor.execute("""SELECT * FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id""")
    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        if row[4] == sys.argv[4]:
            print(row)
            print(row[2].join('[{}]'.format(', '.join([row[4]]))))

    # Close the cursor and database connection
    cursor.close()
    db.close()

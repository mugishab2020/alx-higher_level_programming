#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    import sys
    # declaring some vars
    my_host = 'localhost'
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]
    port = 3306

    # connect the db
    my_db = MySQLdb.connect(
            host=my_host, user=users, passwd=my_password, db=my_db, port=port
            )
    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )

    # fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors and then database
    my_cursor.close()
    my_db.close()

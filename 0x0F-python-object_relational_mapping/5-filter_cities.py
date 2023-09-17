#!/usr/bin/python3
"""
importing pythin3
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        """SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id"""
    )

    print(", ".join([city[2]
                     for city in my_cursor.fetchall()
                     if city[4] == sys.argv[4]])

          )

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()

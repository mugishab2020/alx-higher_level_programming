#!/usr/bin/python3
"""
importing python3
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # declaring the vars
    my_host = 'localhost'
    users = argv[1]
    passw = argv[2]
    my_db = argv[3]
    my_port = 3306

    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
             host=my_host, user=users, passwd=passw, db=my_db, port=my_port
        )

    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        "SELECT * FROM states  WHERE name=%s ORDER BY id", (argv[4], ))

    # fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()

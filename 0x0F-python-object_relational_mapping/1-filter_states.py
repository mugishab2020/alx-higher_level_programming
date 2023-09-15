#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect the db
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    # create the cusror && execute the query
    corse = database.cursor()
    corse.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%'ORDER BY states.id ASC
        """
        )

    # fetch the data queried
    my_data = corse.fetchall()

    # print a tuple
    for data in my_data:
        print(data)

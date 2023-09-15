#!/usr/bin/python3
#importing the python version 3

if __name__ == "__main__":
    
    import MySQLdb
    from sys import argv
    #opening of database
    database = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    #declaring the cursor
    curse = database.cursor()
    #executing the Querry
    curse.execute("SELECT * FROM states ORDER BY states.id ASC;")
    #fetching data
    data = curse.fetchall()
    #printing the elements
    for x in data:
        print (x)
    #closing cursor
    curse.close()
    #clossing database
    database.close()


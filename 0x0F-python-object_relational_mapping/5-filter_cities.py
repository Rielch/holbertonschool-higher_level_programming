#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    my_host = "localhost"
    my_user = argv[1]
    my_passwd = argv[2]
    my_db = argv[3]

    try:
        db = MySQLdb.connect(host=my_host, user=my_user,
                             passwd=my_passwd, db=my_db)
        cursor = db.cursor()
        cursor.execute("SELECT cities.name \
        FROM states INNER JOIN cities ON states.id = cities.state_id \
        WHERE states.name = %s ORDER BY cities.id", (argv[4], ))
        rows = cursor.fetchall()
        i = 0
        for row in rows:
            if i != 0:
                print(", ", end="")
            i += 1
            print(row[0], end="")
        print(end="\n")
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))

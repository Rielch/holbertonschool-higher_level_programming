#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

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
        cursor.execute("SELECT * FROM states ORDER BY id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))

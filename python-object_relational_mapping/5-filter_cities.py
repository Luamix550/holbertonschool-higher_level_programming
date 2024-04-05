#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa

"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM cities WHERE name = %s", (state_name_searched,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

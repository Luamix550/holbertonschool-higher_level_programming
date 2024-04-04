from sys import argv
import MySQLdb

if __name__ == '__main__':
    mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name 'N%'")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

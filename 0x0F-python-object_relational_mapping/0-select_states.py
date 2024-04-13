#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending
order by states id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    def list_states(username, password, database):
        db = MySQLdb.connect(
                host="localhost",
                port=3306, user=username,
                passwd=password,
                db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        results = cur.fetchall()
        for row in results:
            print(row)
        db.close()

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

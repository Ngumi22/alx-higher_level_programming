#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cur = conn.cursor()
    query = """
            SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cur.execute(query, (state_name,))
    row = cur.fetchone()

    if row is not None:
        print(row[0])

    cur.close()
    conn.close()

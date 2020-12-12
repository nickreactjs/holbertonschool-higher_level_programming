#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    i = 0
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                    FROM states
                    LEFT JOIN cities
                    ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row[0]), end='')
        i += 1
        if i < len(rows):
            print(", ", end='')
    print()
    cur.close()
    db.close()

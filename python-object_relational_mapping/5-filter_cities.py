#!/usr/bin/python3
""""
Lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
                    user=sys.argv[1],
                    password=sys.argv[2],
                    db=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute("SELECT cities.name \
                 FROM cities \
                INNER JOIN states \
                   ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id", (sys.argv[4],))

    cities_in_state = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities_in_state))

    cursor.close()
    connection.close()

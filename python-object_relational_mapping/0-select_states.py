#!/usr/bin/python3
# Module that lists all states from the database hbtn_0e_0_usa


import sys
import MySQLdb

if __name__ == "__main__":
    user_arg, password_arg, db_name_arg = sys.argv[1:4]
    connection = MySQLdb.connect(user=user_arg, passwd=password_arg, db=db_name_arg)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    states_data = cursor.fetchall()
    [print(state) for state in states_data]

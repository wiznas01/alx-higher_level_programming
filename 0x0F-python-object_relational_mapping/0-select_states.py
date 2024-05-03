#!/usr/bin/python3
"""Module that lists all states from MySQL database"""
import sys
import MySQLdb

def list_states(username, password, database):
    #connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    #Execute the SQL query from query result
    rows = cursor.fetchall()

    #print the results
    for row in rows:
        print(row)

    #close the database connection
    db.close()

#example usage
if __name__=='__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

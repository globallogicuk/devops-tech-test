#!/usr/bin/env python

import mysql.connector
db_connection = mysql.connector.connect(
  host="mysql_container",
  user="dev",
  passwd="123456",
  database="devopstt"
)
db_cursor = db_connection.cursor()
try:
    db_cursor.execute("SELECT version FROM versionTable;")
    results = db_cursor.fetchone()
    print("VERSION:", results[0])
    db_cursor.execute("SHOW tables;")
    for row in db_cursor:
        print("TABLES:", row[0].decode())
    # Check if anything at all is returned         
except mysql.connector.Error as err:
    print("ERROR %d IN CONNECTION: %s" % (err.args[0], err.args[1]))
db_cursor.close()
db_connection.close()
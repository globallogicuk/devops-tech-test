#!/usr/bin/env python
import json
import mysql.connector
import filecmp

db_connection = mysql.connector.connect(
  host="mysql_container",
  user="dev",
  passwd="123456",
  database="devopstt"
)
db_cursor = db_connection.cursor(dictionary=True)
try:
    db_cursor.execute("SELECT version FROM versionTable;")
    resultVersion = db_cursor.fetchone()
    f = open('versionTable.json')
    version = json.load(f)
    print("version: ", version)
    print("resultversion ", resultVersion)
    if resultVersion == version:
        print("The Version is updated correctly")
    else:
        print("ERROR: The Version is not updated correctly")
    f = open('tables.json',)
    content = json.load(f)
    for i in content['tables']:
        db_cursor.execute(f"SELECT * FROM {i['name']};")
        result = db_cursor.fetchone()
        name = i['name']
        fileoutput = open("{}.json".format(name))
        test = json.load(fileoutput)
        print("db result: ", result)
        print("Tested against: ", test)
        if result == test:
            print("The contents of {} updated correctly".format(name))
        else:
           print("ERROR: The contents of {} NOT updated correctly".format(name))
except ValueError:
    print("someTable has updated but the table is empty")
except mysql.connector.Error as err:
    print("ERROR %d IN CONNECTION: %s" % (err.args[0], err.args[1]))
db_cursor.close()
db_connection.close()

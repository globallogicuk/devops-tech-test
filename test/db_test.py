import json
import mysql.connector

db_connection = mysql.connector.connect(
  host="mysql_container",
  user="dev",
  passwd="123456",
  database="devopstt"
)
db_cursor = db_connection.cursor(dictionary=True)

def test_version():
    db_cursor.execute("SELECT version FROM versionTable;")
    resultVersion = db_cursor.fetchone()
    f = open('expecteddbstate/versionTable.json')
    version = json.load(f)
    assert resultVersion == version

def test_appTable():
    f = open('expecteddbstate/tables.json',)
    content = json.load(f)
    for i in content['tables']:
        db_cursor.execute(f"SELECT * FROM {i['name']};")
        result = db_cursor.fetchone()
        name = i['name']
        fileoutput = open("{path}{name}.json".format(name=name, path="expecteddbstate/"))
        test = json.load(fileoutput)
        assert result == test
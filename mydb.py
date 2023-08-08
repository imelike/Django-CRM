import mysql.connector

database = mysql.connector.connect(
    host='DB_HOST',
    user='DB_USER',
    passwd='DB_PASSWORD'

)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")

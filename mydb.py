import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",

)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")

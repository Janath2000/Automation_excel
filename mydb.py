import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Janath',

	)

#prepare the cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE cost")

print("All Done!")
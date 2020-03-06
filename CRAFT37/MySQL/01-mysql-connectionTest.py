import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jamie",
  passwd="mysqldb"
)

print(mydb)

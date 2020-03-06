import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jamie",
  passwd="mysqldb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pythonlearning")


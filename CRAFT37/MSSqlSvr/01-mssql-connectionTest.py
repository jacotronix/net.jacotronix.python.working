import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DEVVM;'
                      'Database=tempdb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE pythonlearning")

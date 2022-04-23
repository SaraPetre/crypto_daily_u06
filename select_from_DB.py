# import sqlite3 module
import sqlite3
# create database object to connect 
# the database DB_coins.db
database= sqlite3.connect("DB_coins.db")
# create the cursor object
cur = database.cursor()

# display the data in the table by 
# executing the cursor object
cur.execute("SELECT * from coins")

# fetch all the data
print(cur.fetchall())


cur.execute("SELECT * from coins")  
for i in range(len(cur.description)):
  # print("Column {}:".format(i+1))
  desc = cur.description[i]
  print("  column_name = {}".format(desc[0]))
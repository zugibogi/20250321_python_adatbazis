import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

#adatbazis letrehozasa
DATABASE = "my_database"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

#adatbazisok mutatasa
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#hasznald ezt az adatbazist
mycursor.execute(f"USE {DATABASE}")

#customers tabla letrehozasa
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
print("--------")

#tablak mutatasa
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
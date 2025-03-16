import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE university_db1")
print("Database created successfully!")

cursor.close()
conn.close()

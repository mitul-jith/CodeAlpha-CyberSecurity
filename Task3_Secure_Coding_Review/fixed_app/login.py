
import sqlite3

username = input("Enter Username: ")
password = input("Enter Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()

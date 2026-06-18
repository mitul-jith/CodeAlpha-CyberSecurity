
import sqlite3

username = input("Enter Username: ")
password = input("Enter Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

print("\nExecuting Query:")
print(query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()


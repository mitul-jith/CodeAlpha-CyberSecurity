import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT INTO users VALUES
('mitul','mitul123')
""")

conn.commit()
conn.close()

print("Database Created")
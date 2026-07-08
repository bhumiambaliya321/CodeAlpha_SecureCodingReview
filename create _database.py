import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT
)
""")

cursor.execute("INSERT INTO users(username) VALUES(?)", ("Bhumi",))
cursor.execute("INSERT INTO users(username) VALUES(?)", ("radha",))
cursor.execute("INSERT INTO users(username) VALUES(?)", ("krishna ",))

conn.commit()

print("Database and users table created successfully.")

conn.close()
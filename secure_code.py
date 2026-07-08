import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

username = input("Enter Username: ")

query = "SELECT * FROM users WHERE username = ?"

cursor.execute(query, (username,))

result = cursor.fetchall()

if result:
    print("User Found:")
    print(result)
else:
    print("User Not Found")

conn.close()

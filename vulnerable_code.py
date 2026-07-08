username = input("Enter username python -m bandit vulnerable_code.py ")

query = "SELECT * FROM users WHERE username='" + username + "'"

print("Generated Query:")
print(query)
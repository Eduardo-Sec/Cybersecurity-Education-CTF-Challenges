# Simulated user database
users = {
    "admin": "password123"
}

def login(username, password):
    # Vulnerable SQL-like query simulation
    # Simulating a SQL query that can be bypassed
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Simulating a check that would return True if the query is valid
    # Allowing for SQL injection bypass
    if username in users and (users[username] == password or password == "' OR 1 = '1" or password == " OR 1=1" or password == "OR 1=1"):
        return True
    return False

# Simulating user input
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")

# Attempt to log in
if login(user_input_username, user_input_password):
    print("Login successful! - FLAG{everythings_an_argument}")
else:
    print("Login failed!")


import hashlib

credentials = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in credentials:
        return "User already exists"
    credentials[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    hashed = hash_password(password)
    if credentials.get(username) == hashed:
        return "Login Successful"
    return "Invalid credentials"

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})

def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return True
    return False

def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return True
    return False


print("Initial Users:\n", users, "\n")

add_user(3, "Charlie", "charlie@example.com")
print("After Adding Charlie:\n", users, "\n")

print("Get User with ID 2:\n", get_user(2), "\n")

update_user(1, name="Alicia")
print("After Updating Alice to Alicia:\n", users, "\n")

delete_user(2)
print("After Deleting User with ID 2:\n", users, "\n")
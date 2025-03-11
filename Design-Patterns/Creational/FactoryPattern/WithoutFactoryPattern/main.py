from users import Member,Librarian,Admin
# As we see above if we are not using factory pattern,
# we would have to import the specific class we need everytime we want to use it.
# This is not a great practice.

users_data = [
    {"type": "member", "name": "Alice"},
    {"type": "librarian", "name": "Bob"},
    {"type": "admin", "name": "Charlie"}
]

user_objects = []

for user in users_data:
    if user["type"] == "member":
        user_objects.append(Member(user["name"]))
    elif user["type"] == "librarian":
        user_objects.append(Librarian(user["name"]))
    elif user["type"] == "admin":
        user_objects.append(Admin(user["name"]))
    else:
        raise ValueError(f"Invalid user type: {user['type']}")

# Adding to the above discussed points, this initialization is being handled by a file which actually 
# does not need to and this will be repetitve in other files trying to initialize objects as well

for user in user_objects:
    print(f"{user.name} is a {type(user).__name__}")
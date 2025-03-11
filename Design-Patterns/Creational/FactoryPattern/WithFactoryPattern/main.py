from factory import UserFactory
#simply importing the factory file will be enough no for loops or if conditions anymore
users_data = [
    {"type": "member", "name": "Alice"},
    {"type": "librarian", "name": "Bob"},
    {"type": "admin", "name": "Charlie"}
]

user_objects = [UserFactory.create_user(user["type"], user["name"]) for user in users_data]

for user in user_objects:
    print(f"{user.name} is a {type(user).__name__}")

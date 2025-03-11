from users import Admin
# As seen here when we need a specific type of user we are importing that and exposing our code 

admin = Admin("David")  # Directly creating an Admin object

print(f"Welcome, {admin.name}. You have administrative privileges.")

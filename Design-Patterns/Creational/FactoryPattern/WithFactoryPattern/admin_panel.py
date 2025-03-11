from factory import UserFactory

# Create an admin user
admin = UserFactory.create_user("admin", "David")

# Admin-specific logic
print(f"Welcome, {admin.name}. You have administrative privileges.")

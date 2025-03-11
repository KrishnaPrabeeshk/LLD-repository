from users import Member, Librarian, Admin
# This is the only method that will look at the specific implementation 
# while the other files just import this file and don't need the implementation

class UserFactory:
    user_types = {
        "member":Member,
        "librarian":Librarian,
        "admin":Admin
        }
    
    @staticmethod
    def create_user(user_type,name):
        if user_type.lower() in UserFactory.user_types:
            return UserFactory.user_types[user_type.lower()](name)
        raise ValueError(f"Invalid user type {user_type}")
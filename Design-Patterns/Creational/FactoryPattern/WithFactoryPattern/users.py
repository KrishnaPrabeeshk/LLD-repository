class User:
    def __init__(self,name):
        self.name = name

class Member(User):
    def __init__(self,name):
        super().__init__(name)

class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
        
class Admin(User):
    def __init__(self, name):
        super().__init__(name)
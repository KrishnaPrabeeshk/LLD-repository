class Database:
    _instance = None #Initially there will be no object created so the instance is none
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("New database connection created")
        return cls._instance
        # Since we are only creating a new instance if the instance is None 
        # we are only creating 1 instance at a time thus following the singeton design pattern.
    def query(self,q):
        print(f"Executing query {q}")
    
db1 = Database()
db2 = Database()
# I am creating 2 instances here let's see if they will be the same instance or not

db1.query("Select * from Users")
db2.query("DELETE FROM Books")

print(db1 is db2)
# Prints True if both instances are the same.
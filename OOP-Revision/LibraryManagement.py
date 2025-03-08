class Users:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id


class Members(Users):
    def __init__(self,name,user_id):
        super().__init__(name, user_id)


class Librarian(Users):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)



class Books:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def borrowBook(self):
        if self.is_available:
            self.is_available = False
            return True  # Successfully borrowed
        return False  # Already borrowed
    
    def returnBook(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}
    
    def addBook(self,book):
        self.books[book.isbn] = book

    def borrow_book(self,isbn,user):
        if isbn in self.books and self.books[isbn].borrowBook():
            self.borrowed_books[isbn] = user.user_id
            return f"Book {isbn} borrowed by {user.name} successfully"
        return "Book not available"
    
    def return_book(self,isbn,user):
        if isbn in self.books and isbn in self.borrowed_books:
            if self.borrowed_books[isbn] == user.user_id:
                self.books[isbn].returnBook()
                del self.borrowed_books[isbn]
                return f"Book {isbn} returned by {user.name} successfully"
            return f"Book {isbn} cannot be returned by another person(not borrowed by {user.name})"
        return "Invalid ISBN"


library = Library()

book1 = Books("Harry Potter","J.K. Rowling","123")
book2 = Books("The Hobbit","J.R.R. Tolkien","456")

member1 = Users("Alice","M101")
member2 = Users("Bob","M102")

library.addBook(book1)
library.addBook(book2)

print(library.borrow_book("123",member1))
print(library.borrow_book("123",member2))
print(library.return_book("123",member2))
print(library.return_book("123",member1))
print(library.borrow_book("123",member2))
        
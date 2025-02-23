class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"


class Librarian(User):
    def __init__(self, user_id, name, library_name):
        super().__init__(user_id, name)
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"'{book.title}' removed from the library.")
                return
        print(f"Book '{book_title}' not found in the library.")

    def view_books(self):
        print(f"Books in {self.library_name}:")
        for book in self.books:
            print(f"- {book.title} by {book.author} ({'Available' if book.available else 'Not Available'})")


class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def borrow_book(self, librarian, book_title):
        for book in librarian.books:
            if book.title == book_title and book.available:
                self.borrowed_books.append(book)
                book.available = False
                print(f"{self.name} borrowed '{book.title}'.")
                return
        print(f"'{book_title}' is either not available or already borrowed.")

    def return_book(self, librarian, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                librarian.add_book(book)
                book.available = True
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} doesn't have '{book_title}' to return.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"


librarian = Librarian(user_id=1, name="Alice", library_name="Programming Library")

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin")
book3 = Book("Introduction to Algorithms", "Thomas H. Cormen")

librarian.add_book(book1)
librarian.add_book(book2)
librarian.add_book(book3)

member = Member(user_id=101, name="Ram")

member.borrow_book(librarian, "Python Crash Course")

member.borrow_book(librarian, "Introduction to Algorithms")

member.return_book(librarian, "Python Crash Course")

librarian.remove_book("Clean Code: A Handbook of Agile Software Craftsmanship")

librarian.view_books()

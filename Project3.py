#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Vadym Didukh
# CIST2110-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv

# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:



# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. isbn (int)
#    b. title (string)
#    c. author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. check_out - sets borrowed to True and returns a message that the book has been checked out
#    c. check_in - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed

class Book:
    """Book class that has book in the library."""
    def __init__(self, title: str, author: str, isbn: int)-> None:        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def __str__(self) -> str:
        """Return a string description of the book."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Borrowed: {self.borrowed}"

    def check_out(self) -> str:
        """Check out the book."""
        if not self.borrowed:
            self.borrowed = True
            return f"The book {self.title} has been checked out."
        else:
            return f"The book {self.title} is already checked out."

    def check_in(self)-> str:
        """Check in the book."""
        if self.borrowed:
            self.borrowed = False
            return f"The book {self.title} has been checked in."
        else:
            return f"The book {self.title} is already checked in."

    def is_borrowed(self)-> bool:
        """Check if the book is borrowed."""
        return self.borrowed

# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. name (string)
#    c. member_id (int)
#    d. borrowed_books (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowed_books list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book object as a parameter)
#    c. return_book - removes the book from the borrowed_books list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book object as a parameter)
class User:
    """Class User describes a user of the library."""
    def __init__(self, name: str, member_id: int, )-> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self) -> str:
        """Return a string description of the user."""
        borrowed_book_titles = ', '.join([book.title for book in self.borrowed_books])
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_book_titles}"

    def borrow_book(self, book: Book) -> str:
        """Borrow a book."""
        if not book.borrowed:
            self.borrowed_books.append(book)
            book.borrowed = True
            return f"The book '{book.title}' has been checked out."
        else:
            return f"The book '{book.title}' is already checked out."

    def return_book(self, book: Book) -> str:
        """Return a book."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.borrowed = False
            return f"The book '{book.title}' has been checked in."
        else:
            return f"The book '{book.title}' is not borrowed by {self.name}."

# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book object as a parameter)
#    c. add_user - adds a user to the users list (should take a user object as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowed_books attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
class Library:
    """A class representing a library"""
    def __init__(self):
        """Initialize a Library object with empty lists for books and users."""
        self.books = []
        self.users = []
        
    def __str__(self) -> str:
        return f"Books: {len(self.books)}, Users: {len(self.users)}"    

    def add_book(self, book: Book)-> None:
        """Add a book to the library
        Args:
        book (Book): Book to add to the library.
        """
        self.books.append(book)
        
    def add_user(self, user: User)-> None:
        self.users.append(user)
        """Add a user to the library
        Args:
        user (User): User to add to the library.
        """
    def delete_book(self, isbn) -> str:
        """Delete a book from the library
        Args:
        book (Book): Book to delete
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"The book with ISBN {isbn} has been deleted."
        return "Book not found."

    def delete_user(self, member_id: int) -> str:
        """Delete a user from the library
        Args:
        user (User): Book to add
        """
        for user in self.users:
            if user.member_id == member_id:
                self.users.remove(user)
                return f"The user with ID {member_id} has been deleted."
        return "User not found."
    
    def borrow_book(self, member_id: int, isbn: int) -> str:
        """Book to borrow."""
        user = self.find_user(member_id)
        if user:
            book = self.find_book(isbn)
            if book:
                return user.borrow_book(book)
            else:
                return "Book not found."
        else:
            return "User not found."
        
    def return_book(self, member_id: int, isbn: int) -> str:
        """Book to retun."""
        user = self.find_user(member_id)
        if user:
            book = self.find_book(isbn)
            if book:
                return user.return_book(book)
            else:
                return "Book not found."
        else:
            return "User not found."
    
    def search_books(self, keyword: str):
        """Search for books based on a keyword in title or author."""
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books
    
    def check_book_availability(self, isbn: int) -> str:
        """Check the availability of a book."""
        book = self.find_book(isbn)
        if book:
            if book.is_borrowed():
                return f"The book {book.title} is not available."
            else:
                return f"The book {book.title} is available."
        else:
            return "Book not found."

    def search_users(self, keyword: str):
        """Search for users based on a keyword in their names.

    Args:
        keyword (str): The keyword to search for in user names.

    Returns:
        list: A list of User objects whose names contain the specified keyword.
    """
        found_users = []
        for user in self.users:
            if keyword.lower() in user.name.lower():
                found_users.append(user)
        return found_users  
    
    def find_book(self, isbn: int):
        """Find a book by its ISBN.
    Args:
        isbn (str): The ISBN of the book to find.
    Returns:
        Book or None: The Book object if found, None if not found.
    """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user(self, member_id: int):
        """Find a user by their member ID.
    Args:
        member_id (int): The member ID of the user to find.
    Returns:
        User or None: The User object if found, None if not found.
    """
        for user in self.users:
            if user.member_id == member_id:
                return user
        return None

    def export_books_to_csv(self, filename: str) -> None:
        """Export books to a csv file."""
        with open(filename, 'w', newline = '') as csvfile:
            fieldnames = ['ISBN', 'Title', 'Author', 'Borrowed']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({'ISBN': book.isbn, 'Title': book.title, 'Author': book.author, 'Borrowed': book.borrowed})

    def export_users_to_csv(self, filename: str) -> None:
        """Export users to a csv file."""
        with open(filename, 'w', newline = '') as csvfile:
            fieldnames = ['Name', 'ID', 'Borrowed Books']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for user in self.users:
                borrowed_books_titles = ', '.join([book.title for book in user.borrowed_books])
                writer.writerow({'Name': user.name, 'ID': user.member_id, 'Borrowed Books': borrowed_books_titles})

# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit

def menu() -> str:
    while True:
        try:
            print("\nMenu:")
            print("a. Add book")
            print("b. Add user")
            print("c. Delete book")
            print("d. Delete user")
            print("g. Borrow book")
            print("h. Return book")
            print("i. Search books")
            print("j. Check if book is available")
            print("k. Search users")
            print("l. Export books to csv")
            print("m. Export users to csv")
            print("z. Exit")
            choice = input("Enter a choice: ").lower()
            return choice
        except ValueError:
            print("Invalid choice. Please enter letter.")    

# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a Library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 13)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?
# 9. Did you create a test plan that thoroghly tests the program?

def main():
    library = Library()
    while True:
        choice = menu()        
        if choice == 'a':
            isbn = int(input("Enter ISBN: "))
            title = input("Enter title: ")
            author = input("Enter author: ")
            book = Book(isbn, title, author)
            library.add_book(book)
            print("Book added successfully.")
        elif choice == 'b':
            name = input("Enter name: ")
            member_id = int(input("Enter member ID: "))
            user = User(name, member_id)
            library.add_user(user)
            print("User added successfully.")
        elif choice == 'c':
            isbn = int(input("Enter ISBN of the book to delete: "))
            print(library.delete_book(isbn))
        elif choice == 'd':
            member_id = int(input("Enter member ID of the user to delete: "))
            print(library.delete_user(member_id))
        elif choice == 'g':
            member_id = int(input("Enter user ID: "))
            isbn = int(input("Enter ISBN of the book to borrow: "))
            print(library.borrow_book(member_id, isbn))
        elif choice == 'h':
            member_id = int(input("Enter user ID: "))
            isbn = int(input("Enter ISBN of the book to return: "))
            print(library.return_book(member_id, isbn))
        elif choice == 'i':
            keyword = input("Enter keyword to search books: ")
            found_books = library.search_books(keyword)
            if found_books:
                for book in found_books:
                    print(book)
            else:
                print("No books found.")
        elif choice == 'j':
            isbn = int(input("Enter ISBN of the book: "))
            print(library.check_book_availability(isbn))
        elif choice == 'k':
            keyword = input("Enter keyword to search users: ")
            found_users = library.search_users(keyword)
            if found_users:
                for user in found_users:
                    print(user)
            else:
                print("No users found.")
        elif choice == 'l':
            filename = input("Enter filename to export books: ")
            library.export_books_to_csv(filename)
            print("Books exported to CSV successfully.")
        elif choice == 'm':
            filename = input("Enter filename to export users: ")
            library.export_users_to_csv(filename)
            print("Users exported to CSV successfully.")
        elif choice == 'z':
            print("See you later.")
            break
        else:
            print("Invalid choice. Please try again.")        

if __name__ == "__main__":
    
    main()

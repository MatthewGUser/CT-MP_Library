import re
from book import Book
from user import User
from author import Author

class UserInterface:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}
        self.load_data()

    def load_data(self):
        """Load data from text files into the system."""
        self.load_books()
        self.load_users()
        self.load_authors()

    def save_data(self):
        """Save the current state of the system to text files."""
        self.save_books()
        self.save_users()
        self.save_authors()

    def load_books(self):
        """Load books from a text file."""
        try:
            with open('data/books.txt', 'r') as file:
                for line in file:
                    title, author, genre, publication_date, availability = line.strip().split('|')
                    book = Book(title, author, genre, publication_date)
                    book.availability = availability == 'True'
                    self.books[title] = book
        except FileNotFoundError:
            print("Books file not found. Starting with an empty book list.")

    def save_books(self):
        """Save books to a text file."""
        with open('data/books.txt', 'w') as file:
            for book in self.books.values():
                file.write(f"{book.title}|{book.author}|{book.genre}|{book.publication_date}|{book.availability}\n")

    def load_users(self):
        """Load users from a text file."""
        try:
            with open('data/users.txt', 'r') as file:
                for line in file:
                    name, user_id, borrowed_books = line.strip().split('|')
                    borrowed_books = borrowed_books.split(',')
                    user = User(name, user_id)
                    for book_title in borrowed_books:
                        if book_title:
                            user.borrow_book(book_title)
                    self.users[user_id] = user
        except FileNotFoundError:
            print("Users file not found. Starting with an empty user list.")

    def save_users(self):
        """Save users to a text file."""
        with open('data/users.txt', 'w') as file:
            for user in self.users.values():
                borrowed_books = ','.join(user.borrowed_books)
                file.write(f"{user.name}|{user.user_id}|{borrowed_books}\n")

    def load_authors(self):
        """Load authors from a text file."""
        try:
            with open('data/authors.txt', 'r') as file:
                for line in file:
                    name, biography = line.strip().split('|')
                    author = Author(name, biography)
                    self.authors[name] = author
        except FileNotFoundError:
            print("Authors file not found. Starting with an empty author list.")

    def save_authors(self):
        """Save authors to a text file."""
        with open('data/authors.txt', 'w') as file:
            for author in self.authors.values():
                file.write(f"{author.name}|{author.biography}\n")

    def print_main_menu(self):
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

    def print_book_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")

    def print_user_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")

    def print_author_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        publication_date = input("Enter publication date: ")
        book = Book(title, author, genre, publication_date)
        book.availability = True
        self.books[title] = book
        self.save_books()
        print("Book added successfully!")

    def borrow_book(self):
        user_id = input("Enter user ID: ")
        book_title = input("Enter book title: ")
        if book_title in self.books and self.books[book_title].availability:
            if user_id in self.users:
                self.users[user_id].borrow_book(book_title)
                self.books[book_title].availability = False
                self.save_users()
                self.save_books()
                print("Book borrowed successfully!")
            else:
                print("User not found.")
        else:
            print("Book not available or does not exist.")

    def return_book(self):
        user_id = input("Enter user ID: ")
        book_title = input("Enter book title: ")
        if book_title in self.books and user_id in self.users:
            self.users[user_id].return_book(book_title)
            self.books[book_title].availability = True
            self.save_users()
            self.save_books()
            print("Book returned successfully!")
        else:
            print("Invalid book or user.")

    def search_book(self):
        book_title = input("Enter book title: ")
        if book_title in self.books:
            print(self.books[book_title])
        else:
            print("Book not found.")

    def display_all_books(self):
        for book in self.books.values():
            print(book)

    def add_user(self):
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user = User(name, user_id)
        self.users[user_id] = user
        self.save_users()
        print("User added successfully!")

    def view_user_details(self):
        user_id = input("Enter user ID: ")
        if user_id in self.users:
            print(self.users[user_id])
        else:
            print("User not found.")

    def display_all_users(self):
        for user in self.users.values():
            print(user)

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        self.authors[name] = author
        self.save_authors()
        print("Author added successfully!")

    def view_author_details(self):
        name = input("Enter author name: ")
        if name in self.authors:
            print(self.authors[name])
        else:
            print("Author not found.")

    def display_all_authors(self):
        for author in self.authors.values():
            print(author)

    def run(self):
        while True:
            self.print_main_menu()
            choice = input("Select an option: ")
            if choice == '1':
                self.print_book_menu()
                book_choice = input("Select an option: ")
                if book_choice == '1':
                    self.add_book()
                elif book_choice == '2':
                    self.borrow_book()
                elif book_choice == '3':
                    self.return_book()
                elif book_choice == '4':
                    self.search_book()
                elif book_choice == '5':
                    self.display_all_books()
                else:
                    print("Invalid choice.")
            elif choice == '2':
                self.print_user_menu()
                user_choice = input("Select an option: ")
                if user_choice == '1':
                    self.add_user()
                elif user_choice == '2':
                    self.view_user_details()
                elif user_choice == '3':
                    self.display_all_users()
                else:
                    print("Invalid choice.")
            elif choice == '3':
                self.print_author_menu()
                author_choice = input("Select an option: ")
                if author_choice == '1':
                    self.add_author()
                elif author_choice == '2':
                    self.view_author_details()
                elif author_choice == '3':
                    self.display_all_authors()
                else:
                    print("Invalid choice.")
            elif choice == '4':
                print("Quitting the application.")
                self.save_data()
                break
            else:
                print("Invalid choice.")

# Library Management System
## Project Overview
Welcome to the Library Management System! This command-line-based Python application is designed to efficiently manage a library's collection of books and resources. With a focus on applying Object-Oriented Programming (OOP) principles, this system allows users to browse, borrow, return, and explore books while ensuring robust code organization and functionality.

The project is structured into multiple Python files and modules to enhance code readability, maintainability, and scalability. It features a user-friendly command-line interface (CLI) with dedicated menus for book operations, user operations, and author operations.

## Features
* Book Operations: Add, borrow, return, search for books, and display all books.
* User Operations: Add new users, view user details, and display all users.
* Author Operations: Add new authors, view author details, and display all authors.
* Enhanced CLI: Intuitive and interactive command-line interface with separate menus for each operation category.
* Encapsulation: Private attributes with getters and setters for controlled access and modification.
* Error Handling: Handling of input errors and file operations.
* Bonus Features (Optional): Text file handling, reservation system, and fine calculation for overdue books.

## File Structure
This project is organized into several key files and modules:

1. main.py - The main entry point for the application, handling the command-line interface and menu operations.
2. book.py - Contains the Book class representing individual books, with methods for book-related operations.
3. user.py - Contains the User class representing library users, with methods for user-related operations.
4. author.py - Contains the Author class representing book authors, with methods for author-related operations.
5. user_interface.py - Module for managing the user interface and command-line interactions.
6. file_handler.py - Module for handling file operations such as loading and saving data.
7. reservation.py - Module for managing book reservations and notifications.
8. fine_calculation.py - Module for calculating fines for overdue books.
9. README.md - This file, providing an overview of the project and instructions.
10. data/ - Directory containing optional text files for storing data:
* books.txt - book data.
* users.txt - user data.
* authors.txt - author data.

## How to Run the Application
1. Clone the Repository:

```
git clone https://github.com/MatthewGUser/CT-MP_Library
cd CT-MP_Library
```

2. Run the Application: In your terminal, run the contact_manager.py file to start the program:
```
python main.py
```

3. Menu Options: Once the program is running, you’ll be greeted with the following menu:
```
Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
```
4. Follow the Instructions: Choose the number corresponding to the action you want to take and follow the prompts to manage your contacts.

## Example Usage
Here’s a sample interaction with the Contact Management System:

```
Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Select an option (1-4): 1
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books

Select an option (1-5): 1
Enter book title: The Great Gatsby
Enter author name: F. Scott Fitzgerald
Enter genre: Fiction
Enter publication date (YYYY-MM-DD): 1925-04-10
Book added successfully!
```

## Input Validation
* Input Validation: Ensures correct formatting for user input using regular expressions (if implemented).
* Error Handling: The application gracefully manages invalid inputs and potential errors.

## Project Structure
```
library_management_system/
├── main.py                 # Main entry point for the application (UI and menu).
├── book.py                 # Class for managing book-related operations.
├── user.py                 # Class for managing user-related operations.
├── author.py               # Class for managing author-related operations.
├── user_interface.py       # Module for managing the user interface and command-line interactions.
├── file_handler.py         # Module for handling file operations such as loading and saving data.
├── reservation.py          # Module for managing book reservations and notifications.
├── fine_calculation.py     # Module for calculating fines for overdue books.
├── README.md               # Project overview and instructions.
└── data/                   # Text files for storing data.
    ├── books.txt           
    ├── users.txt           
    └── authors.txt         
```

## Conclusion
This Contact Management System allows you to manage your contacts with ease, featuring a modular code structure for better organization and maintainability. Feel free to explore the code and extend its functionalities!

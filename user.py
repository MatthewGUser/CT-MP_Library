class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
        else:
            raise ValueError("Book not found in borrowed list")

    def __str__(self):
        return f"User: {self.__name}, ID: {self.__user_id}, Borrowed Books: {', '.join(self.__borrowed_books)}"

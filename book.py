class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, status):
        if isinstance(status, bool):
            self.__availability = status
        else:
            raise ValueError("Availability must be a boolean")

    def __str__(self):
        status = "Available" if self.__availability else "Borrowed"
        return f"{self.__title} by {self.__author}, Genre: {self.__genre}, Published: {self.__publication_date}, Status: {status}"

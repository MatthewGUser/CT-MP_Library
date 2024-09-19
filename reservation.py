class Reservation:
    def __init__(self):
        self.reservations = {}

    def reserve_book(self, user_id, book_title):
        if book_title in self.reservations:
            self.reservations[book_title].append(user_id)
        else:
            self.reservations[book_title] = [user_id]

    def notify_users(self, book_title):
        if book_title in self.reservations:
            users = self.reservations.pop(book_title)
            for user in users:
                print(f"User {user} notified: '{book_title}' is now available.")

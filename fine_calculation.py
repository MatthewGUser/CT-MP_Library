from datetime import datetime, timedelta

class FineCalculation:
    def __init__(self):
        self.due_dates = {}
        self.fines = {}

    def assign_due_date(self, book_title, user_id):
        due_date = datetime.now() + timedelta(days=14)  # Assuming 14 days borrowing period
        self.due_dates[(book_title, user_id)] = due_date

    def calculate_fine(self, book_title, user_id):
        if (book_title, user_id) in self.due_dates:
            due_date = self.due_dates[(book_title, user_id)]
            if datetime.now() > due_date:
                overdue_days = (datetime.now() - due_date).days
                fine = overdue_days * 1  # Assuming $1 fine per day
                self.fines[user_id] = self.fines.get(user_id, 0) + fine
                return fine
        return 0

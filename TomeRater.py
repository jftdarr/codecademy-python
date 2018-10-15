import re
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

        print(f"{self.name}'s email address has been updated to {self.email}")

    def __repr__(self):
        return f"User: {self.name}\n    email: {self.email}\n   books read: {len(self.books)}"

    def __eq__(self, other_user):
        if self.name == other_user.name:
            if self.email == other_user.email:
                return True
            else:
                return False
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if new_isbn == self.isbn:
            return f"{self.isbn} is already in the catalog"
        else:
            self.isbn = new_isbn
            return f"{self.title} ISBN has been updated to {self.isbn}"

    def add_rating(self, rating):
        try:
            if 0 <= rating < 5:
                self.ratings.append(rating)
            else:
                return "Invalid Rating"

        except TypeError:
            "Invalid Type"

    def __eq__(self, other_book):
        if self.title == other_book.title:
            if self.isbn == other_book.isbn:
                return True
            else:
                return False
        else:
            return False

    def get_average_rating(self):
        return round(sum(self.ratings)/len(self.ratings),1)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr(self):
        return f"{self.title}, a {self.level} manual on {self.subject}"


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    @staticmethod
    def create_book(title, isbn):
        return Book(title,isbn)

    @staticmethod
    def create_novel(title, author, isbn):
        return Fiction(title, author, isbn)

    @staticmethod
    def create_non_fiction(title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, f"No user with email {email}!")

        if user:
            user.read_book(book, rating)
            book.add_rating(rating)

            self.books[book] = self.books.get(book, 0) + 1

    def add_user(self, name, email, user_books = None):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if match is None:
            print('Bad Syntax')
            raise ValueError('Bad Syntax')
        else:
            if email not in self.users:
                self.users[email] = User(name, email)
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print(f"user {email} already exists...")

    # Analysis methods
    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def get_most_read_book(self):
        return max(self.books, key=self.books.get)


    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())

        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')

    def most_positive_user(self):
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())

        return str([user for user in self.users.values() if user.get_average_rating() == highest_rated]).strip('[]')

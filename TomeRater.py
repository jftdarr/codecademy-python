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


class Book:
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return f"{self.name} ISBN has been updated to {self.isbn}"

    def add_rating(self,rating):
        if 0 <= rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title:
            if self.isbn == other_book.isbn:
                return True
            else:
                return False
        else:
            return False

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return f"{self.title} by {self.author}"


class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name=\'{self.name}\', pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        index = self.get_index_by_book_id(book_id)
        del self.books[index]
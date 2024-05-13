class Book():
    def __init__(self, name: str, title: str, writer: str, avaible: bool):
        self.name = name
        self.title = title 
        self.writer = writer
        self.avaible = avaible

class Library():    
    def __init__(self):
        self.books: list[Book] = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def get_avaible_books(self):
        result = []
        for i in range(len(self.books)):
            if self.books[i].avaible:
                result.append(self.books[i].title)
        return result
    
    def give_book(self, title):
        for i in range(len(self.books)):
            if self.books[i].avaible and self.books[i].title == title:
                self.books[i].avaible = False
                break
            elif i == len(self.books) - 1:
                print(f"Hazirda '{title}' kitab elimizde yoxdu.")

    def get_back_book(self, title: str):
        for i in range(len(self.books)):
            if self.books[i].title == title:
                self.books[i].avaible = True
    
    def get_not_avaible_books(self):
        result = []
        for i in range(len(self.books)):
            if not self.books[i].avaible:
                result.append(self.books[i].title)
            
        return result
    

book1 = Book('Book1', 'Book1', 'Writer1', True)
book2 = Book('Book2', 'Book2', 'Writer2', True)
book3 = Book('Book3', 'Book3', 'Writer3', False)
book4 = Book('Book4', 'Book4', 'Writer4', True)
book5 = Book('Book5', 'Book5', 'Writer5', False)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

print(library.get_avaible_books())
print(library.get_not_avaible_books())
library.get_back_book('Book3')
library.give_book('Book1')
print(library.get_avaible_books())
print(library.get_not_avaible_books())
        




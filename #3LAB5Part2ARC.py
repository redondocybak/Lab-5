#3LAB5Part2ARC

#book class and the functions
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def mark_as_read(self):
        self.read = True
        print(f"You have finished reading '{self.title}'.")
#EBookReader class and the functions
class EBookReader:
    def __init__(self):
        #list of books available for purchase
        self.available_books = []
        # List of books purchased by the user  
        self.purchased_books = []  

    def add_available_books(self, books):
        self.available_books.extend(books)

    def view_available_books(self):
        print("Available books for purchase:")
        for index, book in enumerate(self.available_books, 1):
            print(f"{index}. {book.description()}")

    def buy_book(self, book_index):
        if 0 <= book_index < len(self.available_books):
            book = self.available_books.pop(book_index)
            self.purchased_books.append(book)
            print(f"You have purchased '{book.title}'.")
            print("-----------------------------------------------------------------")

    def view_purchased_books(self):
        print("Your purchased books:")
        for index, book in enumerate(self.purchased_books, 1):
            print(f"{book.description()}, Read: {book.read}")

    def read_book(self, book_index):
        if 0 <= book_index < len(self.purchased_books):
            book = self.purchased_books[book_index]
            book.mark_as_read()

#instance of the EBookReader system
ebook_reader = EBookReader()

#available books
available_books = [
    Book("Edge of Survival: A Post-Apocalyptic", "Kyla Stone", 396),
    Book("The Wife Upstairs", "Freida McFadden ", 420),
    Book("Mercy Falls", " William Kent Krueger", 368)
]

#available books list
ebook_reader.add_available_books(available_books)

#view available books
ebook_reader.view_available_books()  # View available books

#buy book
ebook_reader.buy_book(0)

#view purchased books
ebook_reader.view_purchased_books()

#read book
ebook_reader.read_book(0)

#view purchased books again to see the 'read' status
ebook_reader.view_purchased_books()

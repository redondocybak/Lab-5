#3LAB5Part1ARC

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

#two invented book objects
book1 = Book("The Adventures of Jose Ricardo Cuadra ", "Alejandro Redondo Cyabk", 434)
book2 = Book("The Secret of Basketball", "Lebron James", 260)

# Print their descriptions and marking the first book as read
print(book1.description())
book1.mark_as_read()

print(book2.description())



from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    publication_year: int

    def display_details(self):
        return (f"Title: {self.title}\nAuthor: {self.author}\n"
                f"ISBN: {self.isbn}\nYear: {self.publication_year}")


# Sample usage
if __name__ == "__main__":
    book = Book("Atomic Habits", "James Clear", "9780735211292", 2018)
    print(book.display_details())

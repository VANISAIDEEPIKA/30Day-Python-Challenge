"""
✨ Day 28 – Clean Code Challenge ✨
📅 Date: June 24, 2025
🎯 Objective: Refactor an existing project using clean code principles.

🧪 Target Code:
Refactored a previous FastAPI project (book CRUD system) that used inconsistent naming, lacked modularity, and had minimal documentation.

✅ Improvements Applied:
- Meaningful function & variable names
- Type hints for clarity
- Docstrings for all functions
- List comprehensions for better readability
- Removed duplicated logic
- Consistent formatting

📍 Result: Code is now easier to read, debug, extend, and maintain.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(
    title="📚 Clean Code Book API",
    description="Refactored In-Memory CRUD API using Clean Code Principles",
    version="2.0.0"
)

# 🎨 Book model using Pydantic
class Book(BaseModel):
    id: Optional[str] = None
    title: str
    author: str
    isbn: str
    year: int

# 🧠 In-memory "database"
library_db: List[Book] = []

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    """
    Create a new book and assign it a unique ID.
    """
    book.id = str(uuid4())
    library_db.append(book)
    return book

@app.get("/books/", response_model=List[Book])
def get_books():
    """
    Retrieve all books from the library.
    """
    return library_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str):
    """
    Get a specific book by its ID.
    """
    book = next((b for b in library_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, updated_book: Book):
    """
    Update the details of an existing book.
    """
    for index, book in enumerate(library_db):
        if book.id == book_id:
            updated_book.id = book_id
            library_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    """
    Delete a book by its ID.
    """
    for index, book in enumerate(library_db):
        if book.id == book_id:
            del library_db[index]
            return {"message": "✅ Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

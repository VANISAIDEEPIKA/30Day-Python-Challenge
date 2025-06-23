from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# 📚 Book Schema using Pydantic
class Book(BaseModel):
    id: Optional[str] = None
    title: str
    author: str
    isbn: str
    year: int

# In-memory DB replacement 🧠
library_db: List[Book] = []


# 📥 Create a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    book.id = str(uuid4())
    library_db.append(book)
    return book


# 📤 Read all books
@app.get("/books/", response_model=List[Book])
def get_books():
    return library_db


# 🔍 Read a book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str):
    for book in library_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# 🔁 Update a book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, updated_book: Book):
    for i, book in enumerate(library_db):
        if book.id == book_id:
            updated_book.id = book_id
            library_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


# ❌ Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    for i, book in enumerate(library_db):
        if book.id == book_id:
            del library_db[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import database
import schemas

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Book Management API",
    description="A CRUD API for managing books using SQLAlchemy and SQLite",
    version="1.0.0"
)

# Root route ✅
@app.get("/", tags=["Welcome"])
def root():
    return {"message": "📚 Welcome to the Book Management API. Head over to /docs for API testing!"}

# DB dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📥 Create a new book
@app.post("/books/", response_model=schemas.BookResponse, status_code=201, tags=["Books"])
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    existing_book = db.query(models.Book).filter(models.Book.isbn == book.isbn).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists")

    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 📤 Get all books
@app.get("/books/", response_model=List[schemas.BookResponse], tags=["Books"])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Book).offset(skip).limit(limit).all()

# 🔍 Get a book by ID
@app.get("/books/{book_id}", response_model=schemas.BookResponse, tags=["Books"])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# 🔎 Search books
@app.get("/books/search/", response_model=List[schemas.BookResponse], tags=["Books"])
def search_books(q: str, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(
        (models.Book.title.contains(q)) | 
        (models.Book.author.contains(q))
    ).all()

# 🔁 Update book
@app.put("/books/{book_id}", response_model=schemas.BookResponse, tags=["Books"])
def update_book(book_id: int, updated_book: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if updated_book.isbn != book.isbn:
        existing_book = db.query(models.Book).filter(models.Book.isbn == updated_book.isbn).first()
        if existing_book:
            raise HTTPException(status_code=400, detail="Book with this ISBN already exists")

    for key, value in updated_book.dict().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book

# ❌ Delete book
@app.delete("/books/{book_id}", response_model=dict, tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": f"Book '{book.title}' deleted successfully"}

# 📊 Book stats
@app.get("/books/stats/summary", response_model=dict, tags=["Analytics"])
def get_books_stats(db: Session = Depends(get_db)):
    total_books = db.query(models.Book).count()
    unique_authors = db.query(models.Book.author).distinct().count()
    return {
        "total_books": total_books,
        "unique_authors": unique_authors,
        "message": f"Library contains {total_books} books by {unique_authors} different authors"
    }

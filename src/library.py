"""library.py

Core library logic for the Library Borrowing System.
"""

from __future__ import annotations

from book import Book
from borrower import Borrower


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.borrowers: list[Borrower] = []

    def add_book(self, book: Book) -> None:
        # Avoid duplicate ISBNs.
        existing = next((b for b in self.books if b.isbn == book.isbn), None)
        if existing is not None:
            # Update fields rather than creating a duplicate.
            existing.title = book.title
            existing.author = book.author
            return
        self.books.append(book)

    def add_borrower(self, borrower: Borrower) -> None:
        existing = next((br for br in self.borrowers if br.borrower_id == borrower.borrower_id), None)
        if existing is not None:
            existing.name = borrower.name
            return
        self.borrowers.append(borrower)

    def search_books(self, keyword: str) -> list[Book]:
        kw = (keyword or "").strip().lower()
        if not kw:
            return list(self.books)
        results: list[Book] = []
        for b in self.books:
            if kw in b.title.lower() or kw in b.author.lower() or kw in b.isbn.lower():
                results.append(b)
        return results


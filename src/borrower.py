"""borrower.py

Borrower model for the Library Borrowing System.
"""

from __future__ import annotations

from book import Book


class Borrower:
    def __init__(self, name: str, borrower_id: str):
        self.name = (name or "").strip()
        self.borrower_id = (borrower_id or "").strip()

    def borrow_book(self, book: Book) -> bool:
        if book.is_borrowed:
            return False
        book.is_borrowed = True
        book.borrower_id = self.borrower_id
        return True

    def return_book(self, book: Book) -> bool:
        # Allow return only if this borrower currently holds it.
        if not book.is_borrowed:
            return False
        if book.borrower_id != self.borrower_id:
            return False
        book.is_borrowed = False
        book.borrower_id = None
        return True

    def __repr__(self) -> str:
        return f"Borrower(name={self.name!r}, borrower_id={self.borrower_id!r})"


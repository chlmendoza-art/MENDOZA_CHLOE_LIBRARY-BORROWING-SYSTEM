"""book.py

Book model used by the Library Borrowing System.
"""

from __future__ import annotations


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = (title or "").strip()
        self.author = (author or "").strip()
        self.isbn = (isbn or "").strip()
        self.is_borrowed = False
        self.borrower_id: str | None = None

    def __repr__(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book(title={self.title!r}, author={self.author!r}, isbn={self.isbn!r}, status={status})"


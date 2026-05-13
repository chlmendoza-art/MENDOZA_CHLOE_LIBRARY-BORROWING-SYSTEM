"""
main.py
CLI entry point for the Library Borrowing System.
"""

from book import Book
from borrower import Borrower
from library import Library

def menu():
    print("\n=== Library Borrowing System ===")
    print("1. Add Book")
    print("2. Add Borrower")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

def main():
    library = Library()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            name = input("Borrower name: ")
            borrower_id = input("Borrower ID: ")
            library.add_borrower(Borrower(name, borrower_id))
            print("Borrower added!")

        elif choice == "3":
            keyword = input("Enter title/author keyword: ")
            results = library.search_books(keyword)
            for b in results:
                print(b)

        elif choice == "4":
            borrower_id = input("Borrower ID: ")
            isbn = input("Book ISBN: ")
            borrower = next((br for br in library.borrowers if br.borrower_id == borrower_id), None)
            book = next((bk for bk in library.books if bk.isbn == isbn), None)
            if borrower and book and borrower.borrow_book(book):
                print("Book borrowed successfully!")
            else:
                print("Borrow failed.")

        elif choice == "5":
            borrower_id = input("Borrower ID: ")
            isbn = input("Book ISBN: ")
            borrower = next((br for br in library.borrowers if br.borrower_id == borrower_id), None)
            book = next((bk for bk in library.books if bk.isbn == isbn), None)
            if borrower and book and borrower.return_book(book):
                print("Book returned successfully!")
            else:
                print("Return failed.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# 📚 Library Borrowing System

## 📖 Project Description
The Library Borrowing System is a Python‑based command‑line application designed to simulate the essential operations of a modern library. It replaces the inefficiencies of traditional, paper‑based borrowing with a fast, reliable, and user‑friendly digital solution.  

Users can register new books and borrowers, search for books by title, author, or ISBN, and handle borrowing and returning transactions with clear confirmations and error handling. By enforcing rules such as preventing duplicate ISBNs or borrower IDs, and ensuring that only the correct borrower can return a book, the program maintains data integrity and reduces common errors found in manual systems.  

This project demonstrates key programming concepts such as **object‑oriented design**, **data validation**, and **state management**. It highlights how technology can streamline everyday tasks, making book borrowing more convenient and efficient.  

---

## ✨ Features
- **Add Book** – Register new books with title, author, and ISBN. Prevents duplicate ISBNs.  
- **Add Borrower** – Register borrowers with a unique ID. Updates existing borrower info if ID already exists.  
- **Search Books** – Search by keyword across titles, authors, or ISBNs. Displays availability status.  
- **Borrow Book** – Borrowers can borrow available books. Error handling prevents invalid or duplicate borrowing.  
- **Return Book** – Borrowers can return books they borrowed. Ensures only the correct borrower can return.  
- **Exit** – Closes the program gracefully with a farewell message.  

---

## ⚙️ Installation & Setup
1. Install **Python 3.10+** on your system.  
2. Clone the repository:
   ```bash
   git clone https://github.com/chlmendoza-art/MENDOZA_CHLOE_LIBRARY-BORROWING-SYSTEM.git
   cd LibraryBorrowingSystem
3. python main.py

# SAMPLE CLI USAGE

 # ADDING A BOOK
 === Library Borrowing System ===
1. Add Book
2. Add Borrower
3. Search Books
4. Borrow Book
5. Return Book
6. Exit
Enter choice: 1
Book title: Accidents Happen
Author: FH Batacan
ISBN: 978164129516
Book added

# ADDING A BORROWER
Enter choice: 2
Borrower name: Chloe Mendoza
Borrower ID: 2412998
Borrower added!

# SEARCHING BOOKS
Enter choice: 3
Enter title/author keyword: FH Batacan
Book(title='Accidents Happen', author='FH Batacan', isbn='978164129516', status=Available)

# BORROWING AND RETURNING
Enter choice: 4
Borrower ID: 2412998
Book ISBN: 978164129516
Book borrowed successfully!

Enter choice: 5
Borrower ID: 2412998
Book ISBN: 978164129516
Book returned successfully!

# EXITING 
Enter choice: 6
Goodbye!

## 📸 Screenshots

### Add Book Example
![Add Book Screenshot]( images/add_book.jfif)

### Borrow Book Example
![Borrow Book Screenshot](images/borrow_book.jfif)

### Search Book Example
![Search Book Screenshoot](images/search_book.jfif)
### Return Book Example
![Return Book Screenshot](images/return_book.jfif)

### Exit Example
![Exit Screenshot](images/return_book.jfif)

## 🎥 Demo Video

Watch the full demo here: [Library Borrowing System Demo](https://youtu.be/r3LNBz7z1r0?si=5FJKP6FKlBIv8yb8)


🚀 Future Enhancements
Persistent storage using a database or JSON/CSV files

Due date and overdue tracking

Borrowing history reports

Graphical User Interface (GUI) or web application version

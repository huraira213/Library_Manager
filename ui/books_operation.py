from model.library_model import (add_book_db, get_all_books_db, borrow_book_db, return_book_db, search_by_name_db,
                                 search_by_id_db, delete_book_id_db)

def add_book():
    """Get book name and author from user and call function to add it to the database."""
    try:
        print(" -- Welcome to the add book menu -- ")
        print("-" *40)
        book_name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        if not book_name or not author:
            print("Invalid input. Please enter both the book name and author.")
            return

        print("Adding book...")
        add_book_db(book_name, author)
        print("Book added successfully!")
    except Exception as e:
        print(e)

def delete_book_id():
    """Delete a book from the database by ID."""
    try:
        print(" -- Welcome to the delete book menu -- ")
        print("-" * 50)
        id = int(input("Enter the ID of the book you want to delete: "))
        delete_book_id_db(id)
        print("Book deleted successfully!")
    except Exception as e:
        print(f"Error deleting book: {e}")
        return

def borrow_book(user_id):
    """Borrow a book from the database."""
    print(" -- Welcome to the borrow book menu -- ")
    print("-" *40)
    try:
        book_id = int(input("Enter the ID of the book you want to borrow: "))
        borrow_book_db(book_id, user_id)
    except Exception as e:
        print(f" Error borrowing book: {e}")
        return

def return_book(user_id):
    """Return a borrowed book."""
    try:
        print(" -- Welcome to the return book menu -- ")
        print("-" *40)
        book_id = int(input("Enter the ID of the book you want to return: "))
        return_book_db(book_id, user_id)
    except Exception as e:
        print(f" Error returning book: {e}")
        return


def search_by_name():
    """Search for a book by name and display the results."""
    book_name = input("Enter the name of the book you want to search: ")
    if not book_name:
        print("Invalid input. Please enter the name of the book you want to search.")
    books = search_by_name_db(book_name)
    if not books:
        print("No books found with the given name.")
    else:
        print("-" * 70)
        for book in books:
            book_id, name, author, available, borrow_by = book
            status = " Available" if available else " Checked Out"
            print(f"ID: {book_id:2} | {name:<25} | {author:<20} | {status}")
        print("-" * 70)


def search_by_id():
    """Search for a book by ID and display the result."""
    book_id = int(input("Enter the ID of the book you want to search: "))
    if not book_id:
        print("Invalid input. Please enter the ID of the book you want to search.")
    book = search_by_id_db(book_id)
    if not book:
        print("No book found with the given ID.")
    else:
        book_id, name, author, available, borrow_by = book
        status = " Available" if available else " Checked Out"
        print(f"ID: {book_id:2} | {name:<25} | {author:<20} | {status}")

def search_book():
    """Search for a book by name or ID."""
    try:
        print(" -- Welcome to the search book menu -- ")
        print("-" *40)
        print("What would you like \n 1. Search by name \n 2. Search by ID")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            search_by_name()
        elif choice == 2:
            search_by_id()
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f" Error searching book: {e}")


def view_books():
    """Display all books with proper formatting"""
    try:
        print("\n -- View All Books -- ")
        print("=" * 90)

        books = get_all_books_db()

        if not books:
            print(" No books found in the library.")
        else:
            for book in books:
                book_id, name, author, available, borrow_by = book
                status = " Available" if available else " Checked Out"
                print(f"ID: {book_id:2} | {name:<25} | {author:<20} | {status:<20} | Borrowed by: {borrow_by}")

        print("=" * 90)

    except Exception as e:
        print(f" Error displaying books: {e}")

def delete_book():
    """Delete a book from the database."""
    print(" -- Welcome to the delete book menu -- ")
    print("-" *40)
    print("What would you like \n 1. Delete book by id \n 2. Delete books by name")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = int(input("Enter the ID of the book you want to delete: "))
        if not book_id:
            print("Invalid input. Please enter the ID of the book you want to delete.")



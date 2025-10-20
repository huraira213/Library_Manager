from db.connection import get_connection


def add_book_db(book_name, author):
    """Add a book to the database"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (book_name, author))
                conn.commit()
                conn.close()
    except Exception as e:
        print(f"Error adding book to database: {e}")


def get_all_books_db():
    """Display all books with proper formatting"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM books ORDER BY book_id")
                return cursor.fetchall()
    except Exception as e:
        print(f" Error displaying books: {e}")



def borrow_book_db(book_id):
    """Borrow a book from the database"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Check if the book exists
                cursor.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
                book = cursor.fetchone()

                if not book:
                    print("Book not found in the database.")
                    return

                available = book[0]

                if not available:
                    print("Book is already borrowed.")
                    return

                # Borrow it
                cursor.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
                conn.commit()
                print("Book borrowed successfully!")
    except Exception as e:
        print(f"Error borrowing book: {e}")


def return_book_db(book_id):
    """Return a borrowed book"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
                book = cursor.fetchone()

                if not book:
                    print("Book not found in the database.")
                    return

                available = book[0]

                if available:
                    print("Book is already returned.")
                    return

                cursor.execute("UPDATE books SET available = TRUE WHERE book_id = %s", (book_id,))
                conn.commit()
                print("Book returned successfully!")
    except Exception as e:
        print(f"Error returning book: {e}")

def search_by_name_db(book_name):
    """Search for a book by name and display the results"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM books WHERE title LIKE %s ORDER BY book_id", (f"%{book_name}%",))
                return cursor.fetchall()
    except Exception as e:
        print(f"Error searching book: {e}")
        return []

def search_by_id_db(book_id):
    """Search for a book by ID and display the result"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
                return cursor.fetchone()
    except Exception as e:
        print(f"Error searching book: {e}")
        return []

def delete_book_id_db(book_id):
    """Delete a book from the database by ID"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
                if cur.rowcount == 0:
                    print(f"Book not found with {book_id} in the database.")
                else:
                    print(f"Book with ID {book_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting book: {e}")


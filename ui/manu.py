from ui.books_operation import (add_book, view_books, borrow_book, return_book, search_book, delete_book_id)
from ui.users_operation import (register_user, view_all_users, login, delete_user)

def user_manu():
    try:
        print(" -- Welcome to the main menu -- ")
        print("-" *40)
        while True:
            print("1. Already registered(Login)")
            print("2. Create new Account(Signup)")
            print("3. View users")
            print("4. Delete user")
            print("5. Exist")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user_id, role = login()
                book_manu(user_id, role)
            elif choice == 2:
                register_user()
            elif choice == 3:
                view_all_users()
            elif choice == 4:
                delete_user()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f" Error user manu: {e}")

def book_manu(user_id, role):
    """check is admin or user and call the function"""
    if role == "admin":
        admin_ui(user_id)
    elif role == "user":
        user_ui(user_id)
    else:
        print("Invalid role.")

def admin_ui(user_id):
    """check is admin or user and call the function"""
    try:
        print(" -- Welcome to the book menu -- ")
        print("-" * 40)
        while True:
            print("1. Add book")
            print("2. Delete book")
            print("3. Borrow book")
            print("4. Return book")
            print("5. Search book")
            print("6. View books")
            print("7. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()
            elif choice == 2:
                delete_book_id()
            elif choice == 3:
                borrow_book(user_id)
            elif choice == 4:
                return_book(user_id)
            elif choice == 5:
                search_book()
            elif choice == 6:
                view_books()
            elif choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(e)

def user_ui(user_id):
    """check is admin or user and call the function"""
    try:
        print(" -- Welcome to the book menu -- ")
        print("-" * 40)
        while True:
            print("1. Borrow book")
            print("2. Return book")
            print("3. Search book")
            print("4. View books")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                borrow_book(user_id)
            elif choice == 2:
                return_book(user_id)
            elif choice == 3:
                search_book()
            elif choice == 4:
                view_books()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(e)

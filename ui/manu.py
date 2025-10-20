from ui.operation import add_book, view_books, borrow_book, return_book, search_book

def main_manu():
    try:
        print(" -- Welcome to the main menu -- ")
        print("-" *40)
        while True:
            print("1. Add book")
            print("2. Borrow book")
            print("3. Return book")
            print("4. Search book")
            print("5. View books")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()
            elif choice == 2:
                borrow_book()
            elif choice == 3:
                return_book()
            elif choice == 4:
                search_book()
            elif choice == 5:
                view_books()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(e)
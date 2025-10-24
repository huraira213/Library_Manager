from model.user_model import register_user_db, view_users_db, user_login_db, delete_user_db


def register_user():
    try:
        """get user info and register"""
        print(" -- Welcome to the Register page --")
        print("-" * 40)
        # User inputs
        name = input("Enter your name: ").strip()
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        role = input("Enter your role(Admin/User): ").lower().strip()

        # Validations
        if not name or not password or not confirm_password or not role:
            print("Please enter all the required fields.")
            return
        if password != confirm_password:
            print("Passwords do not match.")
            return

        register_user_db(name, password, role)
    except Exception as error:
        print(f"Error register_user: {error}")

def delete_user():
    try:
        """Delete user"""
        print(" -- Welcome to the Delete page --")
        print("-" * 40)
        user_id = int(input("Enter the ID of the user you want to delete: "))
        delete_user_db(user_id)
    except Exception as error:
        print(f"Error delete_user: {error}")

def view_all_users():
    try:
        """View all registered users"""
        print(" -- Welcome to the Register page --")
        print("-" * 40)

        users = view_users_db()
        for user_id, username, password, role in users:
            #print(f"Id: {user_id} \nName: {username} \n pass: {password}\nRole: {role}")
            print(f"ID: {user_id:2} | {username:<25} | {password:<25} | {role:<20}")


    except Exception as error:
        print(f"Error view_all_users: {error}")
def login():
    """Login user"""
    try:
        print("-- Welcome to the Login page --")
        print("-" * 40)

        # User inputs
        name = input("Enter your name: ").strip()
        password = input("Enter your password: ")

        if not name or not password:
            print("Please enter all required fields.")
            return False

        user = user_login_db(name, password)

        if not user:
            print("No user with that username.")
            return False

        user_id, username_db, password_hash, role = user

        print(f"Welcome back, {username_db}!")
        return user_id, role


    except Exception as e:
        print(f"Error login: {e}")
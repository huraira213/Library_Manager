import bcrypt
from db.connection import get_cursor

def hash_password(password: str) -> str:
    """Generate bcrypt hash for a password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def check_password(plain_password: str, hashed_password: str) -> bool:
    """Check bcrypt password."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def register_user_db(name, password, role):
    """Register new user with hashed password."""
    if not name or not password or not role:
        raise ValueError("Missing fields")

    pass_hash = hash_password(password)

    try:
        with get_cursor() as cur:
            cur.execute("""
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """, (name, pass_hash, role))
    except Exception as e:
        raise ValueError(f"Error registering user: {e}")

def delete_user_db(user_id):
    """Delete user from database by ID."""
    try:
        with get_cursor() as cur:
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            if cur.rowcount == 0:
                print(f"User not found with {user_id} in the database.")
            else:
                print(f"User with ID {user_id} deleted successfully.")
    except Exception as e:
        raise ValueError(f"Error deleting user: {e}")


def user_login_db(username, password):
    """Login user by verifying username and password."""
    try:
        with get_cursor() as cur:
            cur.execute("SELECT user_id, username, password, role FROM users WHERE username = %s", (username,))
            user = cur.fetchone()

            if not user:
                return None

            user_id, username, hashed_password, role = user

            # Verify password
            if check_password(password, hashed_password):
                #return {"user_id": user_id, "username": username, "role": role}
                return user
            else:
                return None  # incorrect password

    except Exception as e:
        raise ValueError(f"Error logging in: {e}")


def view_users_db():
    """- View all users -"""
    with get_cursor() as cur:
        cur.execute("SELECT * FROM users order by user_id ")
        users = cur.fetchall()
        if not users:
            print("No registered users.")
        else:
            return users
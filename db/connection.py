import psycopg2
from contextlib import contextmanager

def initialize_database():
    """Initialize database"""
    create_user_table()
    create_books_table()
    print("Database initialized successfully.")

def recreate_books_table():
    with get_cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS books CASCADE;")
        cur.execute("""CREATE TABLE books (
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL UNIQUE,
            author VARCHAR(200) NOT NULL,
            available BOOLEAN DEFAULT TRUE,
            borrow_by INTEGER REFERENCES users(user_id) ON DELETE SET NULL
        );""")
    print("Books table recreated with borrow_by column.")


def get_connection():
    """Establish and return postgresql connection"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="libraryManager",
            user="postgres",
            password="ali33",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


@contextmanager
def get_cursor():
    conn = get_connection()
    cur = conn.cursor()
    try:
        yield cur         # give control to your query code
        conn.commit()     # if no error → commit
    except Exception as e:
        conn.rollback()   # if error → rollback
        print(f"Error: {e}")
    finally:
        cur.close()       # always runs
        conn.close()      # always runs

def create_user_table():
    """Create users table in database if it doesn't exist"""
    with get_cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                              user_id SERIAL PRIMARY KEY,
                              username VARCHAR(200) NOT NULL UNIQUE,
                              password VARCHAR(200) NOT NULL,
                              role VARCHAR(200) NOT NULL );
        """)

def create_books_table():
    """Create books table in database if it doesn't exist"""
    with get_cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS books (
                              book_id SERIAL PRIMARY KEY,
                              title VARCHAR(200) NOT NULL UNIQUE,
                              author VARCHAR(200) NOT NULL,
                              available BOOLEAN DEFAULT TRUE,
                              borrow_by INTEGER REFERENCES users(user_id) ON DELETE SET NULL
                               ); """)






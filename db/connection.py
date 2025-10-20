import psycopg2


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

def create_table():
    """Create books table in database if it doesn't exist"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS books (
                              book_id SERIAL PRIMARY KEY,
                              title VARCHAR(200) NOT NULL,
                              author VARCHAR(200) NOT NULL,
                              available BOOLEAN DEFAULT TRUE 
                               ); """)

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating table: {e}")



# Mini Library Manager (CLI + PostgreSQL)
A simple Command-Line (CLI) Library Management System built with Python and PostgreSQL.  
It allows users to borrow and return books while admins can manage books and users.  
Designed with clean code principles and modular architecture.

# Features
- **User Authentication**
  - Login / Signup
  - Role-based access (Admin / User)

- **Book Management (Admin)**
  - Add new books
  - Delete books
  - View all books

- **Book Borrowing (User)**
  - Borrow available books
  - Return borrowed books
  - Search books by title

- **Database Management**
  - PostgreSQL integration
  - Proper foreign key relationships (`books.borrow_by → users.user_id`)

```
Mini_Library_Manager/
│
├── db/
│ └── connection.py # PostgreSQL connection setup
│
├── model/
│ ├── library_model.py # CRUD logic for books
│ └── user_model.py # CRUD logic for users
│
├── ui/
│ ├── menu.py # Main CLI menu
│ ├── books_operation.py # Book-related CLI actions
│ └── users_operation.py # User-related CLI actions
│
├── main.py # Entry point of the program
└── README.md
```

1. Clone the repository
   ```bash
   git clone https://github.com/huraira213/Library_Manager.git
   cd Mini_Library_Manager
2. Install dependencies 
    ```bash
    pip install bcrypt psycopg2-binary

   
3. database connection
    ```bash
    connection = psycopg2.connect(
    host="localhost",
    database="library_db",
    user="postgres",
    password="your_password"
)

**Huraira Khurshid**  
Intern at SKAI Worldwide | Aspiring Software Architect  



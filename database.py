import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        enable_foreign_keys(conn)  # Enable foreign key support
    except sqlite3.Error as e:
        print(e)
    return conn

def enable_foreign_keys(conn):
    """Enable foreign key support in SQLite."""
    conn.execute("PRAGMA foreign_keys = ON;")

def setup_database(conn):
    """Create tables without foreign key constraints for initial testing."""
    users_table = """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        phone_number TEXT,
                        address TEXT,
                        bio TEXT
                    );"""
    quizzes_table = """CREATE TABLE IF NOT EXISTS quizzes (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        category TEXT NOT NULL,
                        number_of_questions INTEGER
                    );"""
    questions_table = """CREATE TABLE IF NOT EXISTS questions (
                          id INTEGER PRIMARY KEY,
                          quiz_id INTEGER NOT NULL,
                          question_text TEXT NOT NULL,
                          correct_answer TEXT NOT NULL,
                          answer_a TEXT NOT NULL,
                          answer_b TEXT NOT NULL,
                          answer_c TEXT NOT NULL,
                          answer_d TEXT NOT NULL,
                          FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
                      );""" 
    results_table = """CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY,
                        quiz_id INTEGER NOT NULL,
                        user_id INTEGER NOT NULL,
                        score INTEGER NOT NULL,
                        FOREIGN KEY (quiz_id) REFERENCES quizzes(id),
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    );""" 

    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(users_table)
            c.execute(quizzes_table)
            c.execute(questions_table)
            c.execute(results_table)
            print("Tables created successfully with foreign keys.")
        except sqlite3.Error as e:
            print(e)


if __name__ == "__main__":
    conn = create_connection("quiz_application.db")
    if conn is not None:
        setup_database(conn)
        print("Database setup completed.")
    else:
        print("Error! cannot create the database connection.")

import sqlite3

def setup_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                         id INTEGER PRIMARY KEY,
                         title TEXT NOT NULL,
                         author TEXT NOT NULL,
                         copies INTEGER NOT NULL
                     )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         member_id TEXT NOT NULL UNIQUE
                     )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books (
                         member_id TEXT NOT NULL,
                         book_id INTEGER NOT NULL,
                         quantity INTEGER NOT NULL,
                         issue_date TEXT NOT NULL,
                         FOREIGN KEY(member_id) REFERENCES members(member_id),
                         FOREIGN KEY(book_id) REFERENCES books(id)
                     )''')

    conn.commit()
    conn.close()

setup_database()

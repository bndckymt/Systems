import sqlite3 as a

open = a.connect('database.db')
cur = open.cursor()



books_to_add = [
            ("The C++ Programming Language", "Bjarne Stroustrup"),
            ("The Python Coding Book-First Edition", "Stephen Gruppetta"),
            ("Head First Java: A Brain-Friendly Guide", "Kathy Sierra"),
            ("R for Data Science", "Hadley Wickham"),
            ("Clean Code", "Robert Cecil Martin"),
            ("The Pragmatic Programmer", "Dave Thomas"),
            ("Code Complete", "Steve McConnell"),
            ("Structure and Interpretation of Computer Programs", "Harold Abelson"),
            ("Introduction to Algorithms", "Thomas H. Cormen"),
            ("JavaScript: The Good Parts", "Douglas Crockford")]

for item in books_to_add:
    cur.execute("""CREATE TABLE IF NOT EXISTS shelves(ID INTEGER PRIMARY KEY,
    BOOKNAME TEXT,
    AUTHOR TEXT
    )""")
    cur.execute("INSERT INTO shelves(BOOKNAME, AUTHOR) VALUES (?, ?)", (item[0], item[1]))
    open.commit()
cur.close()
open.close()

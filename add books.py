import sqlite3


class Library:
    def add_book_to_db(self, title, author, copies):
        try:
            copies = int(copies)
            if copies < 1:
                raise ValueError("There must be at least one copy.")

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO books (title, author, copies) VALUES (?, ?, ?)', (title, author, copies))
            conn.commit()
            conn.close()

            print(f'Book "{title}" by {author} with {copies} copies added successfully.')
        except ValueError as e:
            print(f"Invalid input: {e}")


# Example usage



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

copies = 5
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
for item in books_to_add:
    cursor.execute("INSERT INTO books(title, author, copies) VALUES (?, ?, ?)", (item[0], item[1], copies))
    conn.commit()
cursor.close()
conn.close()

Library()
import re
import sqlite3
from datetime import datetime

class Book:
    def __init__(self, title, author, copies=5):
        self.title = title
        self.author = author
        self.copies = copies
        self.date_issued = None

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.fetch_books_from_db()
        self.fetch_members_from_db()

    def fetch_books_from_db(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, author, copies FROM books')
        rows = cursor.fetchall()
        self.books = [Book(row[1], row[2], row[3]) for row in rows]
        conn.close()
        print("Fetched books from database.")

    def fetch_members_from_db(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, member_id FROM members')
        rows = cursor.fetchall()
        self.members = [Member(row[0], row[1]) for row in rows]
        conn.close()
        print("Fetched members from database.")

    def add_book(self, title, author, copies):
        try:
            copies = int(copies)
            if copies < 5:
                raise ValueError("Must be at least 5 copies.")
            new_book = Book(title, author, copies)
            self.books.append(new_book)

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO books (title, author, copies) VALUES (?, ?, ?)', (title, author, copies))
            conn.commit()
            conn.close()

            print(f'Book "{title}" added successfully.')
        except ValueError as e:
            print(f"Invalid input: {e}")

    def validate_name(self, name):
        pattern = r"^[A-Z][a-z]*(?: [A-Z][a-z]*){1,2}$"
        return re.match(pattern, name) is not None

    def format_name(self, name):
        return ' '.join(part.capitalize() for part in name.split())

    def add_member(self):
        while True:
            name = input("Enter your name: ")
            formatted_name = self.format_name(name)

            if not self.validate_name(formatted_name):
                print("Invalid name format. Please use the sentence format. Thank you!")
                continue

            member_id = input("Enter your ID number (format XX-XXXX, e.g., 21-1484): ")
            while not re.match(r"^\d{2}-\d{4}$", member_id):
                print("Invalid ID number format. Please use the format XX-XXXX (e.g., 21-1484).")
                member_id = input("Enter your ID number again: ")

            # Check if the member is already registered
            if any(member.member_id == member_id for member in self.members):
                print("Already registered! Please go to Membership.")
                break

            new_member = Member(formatted_name, member_id)
            self.members.append(new_member)

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO members (name, member_id) VALUES (?, ?)', (formatted_name, member_id))
            conn.commit()
            conn.close()

            print(f'Member "{formatted_name}" registered successfully.')
            break

    def verify_member(self, member_id):
        while not re.match(r"^\d{2}-\d{4}$", member_id):
            print("Invalid ID number format. Please use the format XX-XXXX (e.g., 21-1484).")
            member_id = input("Enter your ID number again: ")

        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book_by_letter(self, letter):
        index = ord(letter.upper()) - 65
        if 0 <= index < len(self.books):
            return self.books[index]
        return None

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            print(f'{"Letter":<8} {"Title":<45} {"Author":<30} {"Copies Available":<15}')
            print('-' * 100)
            for i, book in enumerate(self.books):
                letter = chr(65 + i)
                print(f'{letter:<8} {book.title:<45} {book.author:<30} {book.copies:<15}')
        else:
            print("No books available in the library.")

    def display_members(self):
        if self.members:
            print("\nRegistered Members:")
            for member in self.members:
                print(f'ID: {member.member_id} | Name: {member.name}')
        else:
            print("No members registered yet. Please register.")
            return False
        return True

    def borrow_books(self, member):
        while True:
            self.display_books()
            selected_books = []
            book_letters = input("Enter the letters of the books you want to borrow (e.g., A B C): ").upper().split()

            for letter in book_letters:
                selected_book = self.find_book_by_letter(letter)
                if selected_book:
                    if selected_book.copies == 0:
                        print(f"No available copies of '{selected_book.title}'.")
                        break
                    copies_to_borrow = int(input(f"How many copies of '{selected_book.title}' would you like to borrow? (Available: {selected_book.copies}): "))
                    if 0 < copies_to_borrow <= selected_book.copies:
                        selected_books.append((selected_book, copies_to_borrow))
                    else:
                        print(f"Invalid number of copies for '{selected_book.title}'. Please select again.")
                        break
                else:
                    print(f"No book found for '{letter}'. Please select again.")
                    break

            if len(selected_books) == len(book_letters):
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                for book, quantity in selected_books:
                    book.copies -= quantity
                    issue_date = datetime.now().strftime('%Y-%m-%d')
                    book.date_issued = issue_date
                    member.borrowed_books.append((book, quantity, issue_date))

                    cursor.execute('UPDATE books SET copies = ? WHERE title = ? AND author = ?', (book.copies, book.title, book.author))
                    cursor.execute('INSERT INTO borrowed_books (member_id, book_id, quantity, issue_date) VALUES (?, ?, ?, ?)', (member.member_id, book.title, quantity, issue_date))

                conn.commit()
                conn.close()

                print(f'You have successfully borrowed {quantity} copies of "{book.title}". Date Issued: {issue_date}')

                more_borrowing = input("Do you want to borrow more books? (y/n): ").lower()
                if more_borrowing == 'n':
                    break
            else:
                print("Please enter the letters of the books you want to borrow again.")
                continue

    def return_books(self, member):
        if not member.borrowed_books:
            print("No books borrowed yet.")
        else:
            while True:
                print("You have borrowed the following books:")
                for i, (borrowed_book, quantity, issue_date) in enumerate(member.borrowed_books):
                    print(f"{i + 1}. {borrowed_book.title} (Quantity: {quantity}, Issued on: {issue_date})")

                return_books = input("Enter the numbers of the books you want to return (comma-separated): ")
                return_indices = list(map(str.strip, return_books.split(',')))

                valid_indices = [str(i + 1) for i in range(len(member.borrowed_books))]
                to_remove = []

                invalid_selection = False
                for index in return_indices:
                    if index in valid_indices:
                        index = int(index) - 1
                        borrowed_book, quantity, issue_date = member.borrowed_books[index]

                        while True:
                            copies_to_return = int(input(f"How many copies of '{borrowed_book.title}' would you like to return? (You have borrowed {quantity}): "))
                            if 0 < copies_to_return <= quantity:
                                borrowed_book.copies
                                borrowed_book.copies += copies_to_return
                                member.borrowed_books[index] = (borrowed_book, quantity - copies_to_return, issue_date)
                                if quantity - copies_to_return == 0:
                                    to_remove.append(index)
                                print(f'Thank you for returning {copies_to_return} copies of "{borrowed_book.title}".')
                                break
                            else:
                                print("Invalid number of copies. Please enter a valid amount.")
                        else:
                            print(f"Invalid selection: {index}. Please choose from the list of borrowed books.")
                            invalid_selection = True

                    if not invalid_selection:
                        conn = sqlite3.connect('library.db')
                        cursor = conn.cursor()
                        for index in sorted(to_remove, reverse=True):
                            borrowed_book, quantity, issue_date = member.borrowed_books[index]
                            cursor.execute(
                                'DELETE FROM borrowed_books WHERE member_id = ? AND book_id = ? AND issue_date = ?',
                                (member.member_id, borrowed_book.title, issue_date))
                            member.borrowed_books.pop(index)

                        conn.commit()
                        conn.close()
                        break
                    else:
                        continue

    def librarian_section(self, member):
        while True:
            print(f"\n|-----------------------------------------------------|")
            print(
                f"| WELCOME TO THE LIBRARY MANAGEMENT SYSTEM - LIBRARIAN SECTION, {member.name: <35}|")
            print(f"|-----------------------------------------------------|")
            print(f"| 1. Borrow Books                                     |")
            print(f"| 2. Return Books                                     |")
            print(f"| 3. Exit                                             |")
            print(f"|-----------------------------------------------------|")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.borrow_books(member)
            elif choice == '2':
                self.return_books(member)
            elif choice == '3':
                print("Thank you for using the Library Management System. Come Again!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


def main():
    library = Library()

    while True:
        print("|-----------------------------------------------------|")
        print("|             LIBRARY MANAGEMENT SYSTEM               |")
        print("|-----------------------------------------------------|")
        print("| 1. Membership                                       |")
        print("| 2. New Member                                       |")
        print("| 3. Display All Members                              |")
        print("| 4. Exit                                             |")
        print("|-----------------------------------------------------|")

        choice = input("Enter your choice: ")

        if choice == '1':
            member_id = input("Enter your ID number (format XX-XXXX): ")
            member = library.verify_member(member_id)
            if member:
                library.librarian_section(member)
            else:
                print("Member not found. Please register first.")

        elif choice == '2':
            library.add_member()
        elif choice == '3':
            library.display_members()
        elif choice == '4':
            print("Thank you for using the Library Management System.")
            exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

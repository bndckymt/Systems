import re
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
        self.initialize_books()

    def initialize_books(self):
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
            ("JavaScript: The Good Parts", "Douglas Crockford")
        ]

        for title, author in books_to_add:
            self.books.append(Book(title, author, copies=5))  # Ensure at least 5 copies

    def add_book(self, title, author, copies):
        try:
            copies = int(copies)
            if copies < 5:
                raise ValueError("Must be at least 5 copies.")
            new_book = Book(title, author, copies)
            self.books.append(new_book)
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
                break  # Exit the registration loop

            new_member = Member(formatted_name, member_id)
            self.members.append(new_member)
            print(f'Member "{formatted_name}" registered successfully.')
            self.librarian_section(new_member)
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
        if 0 <= index < len(self.books[:10]):
            return self.books[index]
        return None

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            print(f'{"Letter":<8} {"Title":<45} {"Author":<30} {"Copies Available":<15}')
            print('-' * 100)
            for i, book in enumerate(self.books[:10]):
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

    def librarian_section(self, member):
        while True:
            print(f"\n|-----------------------------------------------------|")
            print(f"| WELCOME TO THE LIBRARY MANAGEMENT SYSTEM - LIBRARIAN SECTION, {member.name: <35}|")
            print(f"|-----------------------------------------------------|")
            print(f"| 1. Borrow Books                                     |")
            print(f"| 2. Return Books                                     |")
            print(f"| 3. Exit                                             |")
            print(f"|-----------------------------------------------------|")

            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    self.display_books()
                    selected_books = []
                    book_letters = input(
                        "Enter the letters of the books you want to borrow (e.g., A B C): ").upper().split()

                    for letter in book_letters:
                        selected_book = self.find_book_by_letter(letter)
                        if selected_book:
                            if selected_book.copies == 0:
                                print(f"No available copies of '{selected_book.title}'.")
                                break  # Break to re-prompt for selection
                            copies_to_borrow = int(input(
                                f"How many copies of '{selected_book.title}' would you like to borrow? (Available: {selected_book.copies}): "))
                            if 0 < copies_to_borrow <= selected_book.copies:
                                selected_books.append((selected_book, copies_to_borrow))
                            else:
                                print(f"Invalid number of copies for '{selected_book.title}'. Please select again.")
                                break  # Break to re-prompt for selection
                        else:
                            print(f"No book found for '{letter}'. Please select again.")
                            break

                    if len(selected_books) == len(book_letters):  # All selected books are valid
                        for book, quantity in selected_books:
                            book.copies -= quantity
                            issue_date = datetime.now().strftime('%Y-%m-%d')
                            book.date_issued = issue_date
                            member.borrowed_books.append((book, quantity, issue_date))
                            print(
                                f'You have successfully borrowed {quantity} copies of "{book.title}". Date Issued: {issue_date}')

                        more_borrowing = input("Do you want to borrow more books? (y/n): ").lower()
                        if more_borrowing == 'n':
                            break  # Exit borrowing loop
                    else:
                        print("Please enter the letters of the books you want to borrow again.")
                        continue  # Go back to book selection if any book is unavailable

                        # ...
            elif choice == '2':
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
                                    copies_to_return = int(input(
                                        f"How many copies of '{borrowed_book.title}' would you like to return? (You have borrowed {quantity}): "))
                                    if 0 < copies_to_return <= quantity:
                                        borrowed_book.copies += copies_to_return
                                        member.borrowed_books[index] = (
                                        borrowed_book, quantity - copies_to_return, issue_date)  # Update the quantity
                                        if quantity - copies_to_return == 0:
                                            to_remove.append(index)  # Use the index for removal
                                        print(
                                            f'Thank you for returning {copies_to_return} copies of "{borrowed_book.title}".')
                                        break
                                    else:
                                        print("Invalid number of copies. Please enter a valid amount.")

                            else:
                                print(f"Invalid selection: {index}. Please choose from the list of borrowed books.")
                                invalid_selection = True

                        if not invalid_selection:
                            # Remove books marked for removal using their index
                            for index in sorted(to_remove,
                                                reverse=True):  # Remove in reverse order to avoid index shifting
                                member.borrowed_books.pop(index)
                            break

                    if member.borrowed_books:
                        while True:  # Loop to handle returning unreturned books
                            return_remaining = input(
                                "You have unreturned books. Do you want to return the remaining books? (y/n): ").lower()
                            if return_remaining == 'y':
                                # Display unreturned books again
                                print("You have borrowed the following books:")
                                for i, (borrowed_book, quantity, issue_date) in enumerate(member.borrowed_books):
                                    print(
                                        f"{i + 1}. {borrowed_book.title} (Quantity: {quantity}, Issued on: {issue_date})")
                                continue  # Go back to returning books
                            elif return_remaining == 'n':
                                print("Thank you for coming! Hope you enjoy reading.")
                                break
                            else:
                                print("Invalid input. Please enter 'y' or 'n'.")
                    else:
                        print("All books returned. Thank you!")
                        while True:
                            go_back = input("Do you want to go back to the main menu? (y/n): ").lower()
                            if go_back == 'y':
                                return  # Go back to main function
                            elif go_back == 'n':
                                print("Thank you for using the Library Management System.")
                                exit()
                            else:
                                print("Invalid input. Please enter 'y' or 'n'.")

            elif choice == '3':
                print("Thank you for using the Library Management System. Come Again!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


def main():
    while True:
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
                    library.librarian_section(member)  # Proceed to librarian section
                else:
                    print("Member not found. Please register first.")

            elif choice == '2':
                library.add_member()  # Proceed to member registration
            elif choice == '3':
                library.display_members()  # Show all registered members
            elif choice == '4':
                print("Thank you for using the Library Management System.")
                exit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
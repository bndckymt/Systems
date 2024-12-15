import sqlite3 as tab
import system
def data(amount):
    dat = tab.connect('example.db')
    cursor = dat.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(ID INTEGER PRIMARY KEY,
                   NAME TEXT NOT NULL,
                   ADDRESS TEXT NOT NULL,
                   NUMBER INTEGER NOT NULL,
                   AMOUNT INTEGER NOT NULL)""")
    while True:
        try:
            cash = int(input("Your Cash: "))
            if cash>=amount:
                break
            else:
                print("Invalid amount, please enter the right amount")
        except ValueError:
            print("invalid input")

    while True:
        try:
            name = input("What is your name? ")
            if len(name) < 5:
                print("Invalid input: Name must be at least 5 characters long.")
            elif any(char.isdigit() for char in name):
                print("Invalid input: Name should not contain numbers.")
            elif 6 <= len(name) <= 15:
                break
            else:
                print("Invalid input: Name must be between 6 and 15 characters long.")
        except ValueError:
            print("Invalid input")

    address = input("Your address: ").strip()
    if not address:
        address = "No address provided"
    print(f"Stored address: {address}")

    while True:
        number = input("CP Number: ")
        if len(number) == 11 and number.isdigit():
            break
        else:
            print("Invalid input: CP Number must be exactly 11 digits long and consist only of numbers.")
    cursor.execute("INSERT INTO user(NAME, ADDRESS, NUMBER, AMOUNT) VALUES(?, ?, ?, ?)", (name, address, number, amount))
    dat.commit()
    cursor.close()
    dat.close()

    system.close()
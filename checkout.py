import output
import sqlite3


def customer(amount):
    name = input("Our dear customer, may i know whats your name: ")
    print(f"Thank you {name} for using our system, i hope you enjoy shopping in our store")
    address = input(f"Dear {name} our online grocery offers free delivery so may i know your address? ")
    print("here are the list of your purchases")
    paid = amount
    print(output.goods())
    save(name, address, paid)
    while True:
        payment = int(input(f"You need to pay {amount}, Enter your payment amount :"))
        if payment >= amount:
            print("Thank you...")
            break
        else:
            print("Invalid Input")

def save(name, address, paid):
    data = sqlite3.connect("MSMdatabase.db")
    on = data.cursor()
    on.execute('''CREATE TABLE IF NOT EXISTS customers (
                ID INTEGER PRIMARY KEY,
                NAME TEXT,
                ADDRESS TEXT,
                PAID INTEGER
                )''')

    on.execute("INSERT INTO customers (NAME, ADDRESS, PAID) VALUES (?, ?, ?)", (name, address, paid))
    data.commit()
    on.close()
    data.close()

import sqlite3 as Access
import cart

def Type(product, selected):
    select = selected
    products = product
    open = Access.connect('example.db')
    load = open.cursor()
    load.execute("SELECT DISTINCT NAME, PRICE FROM products WHERE PRODUCT = ? AND TYPE = ?", (products, select))
    rows = load.fetchall()
    load.close()
    open.close()
    category = [row[0] for row in rows]
    price = [row[1] for row in rows]
    count = 1
    print("ID  |     PRODUCT     | PRICE")
    print("--- | --------------- | --------")
    for item in category:
        print(f"{count: < 3} | {item: <15} | {price[count-1]:<10}")
        count += 1
    while True:
        try:
            get = int(input("Please choose the product you want to buy: "))
            if get < 1 or get > count - 1:
                print("invalid input")
            elif get >= 1 and get <= count - 1:
                cart.buy(category[get - 1], price[get - 1])
                break
            else:
                print("invalid input")
        except ValueError:
            print("invalid input")
def select(product):
    products = product
    open = Access.connect('example.db')
    load = open.cursor()
    load.execute("SELECT DISTINCT TYPE FROM products WHERE PRODUCT = ?", (products,))
    rows = load.fetchall()
    load.close()
    open.close()
    category = [row[0] for row in rows]
    count = 1
    for item in category:
        print(f"[{count}] {item}")
        count += 1

    while True:
        try:
            ans = int(input("Please choose the product you want to buy: "))
            if ans < 1 or ans > count - 1:
                print("invalid input")
            elif ans >= 1 and ans <= count - 1:
                Type(product, category[ans - 1])
                break
            else:
                print("invalid input")
        except ValueError:
            print("invalid input")

def product():
    open = Access.connect('example.db')
    load = open.cursor()
    load.execute("SELECT DISTINCT PRODUCT FROM products")
    rows = load.fetchall()
    load.close()
    open.close()
    category = [row[0] for row in rows]
    count = 1
    for item in category:
        print(f"[{count}] {item}")
        count += 1

    while True:
        try:
            ans = int(input("Please choose the product you want to buy: "))
            if ans < 1 or ans > count:
                print("invalid input")
            elif ans >=1 and ans <=count - 1:
                select(category[ans - 1])
                break
            else:
                print("invalid input")
        except ValueError:
            print ("invalid input")





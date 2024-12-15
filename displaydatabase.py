import sqlite3
import selection

selected_item = []
selected_price = []

def display():
    conn = sqlite3.connect('MSMdatabase.db')

    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    # Print the data
    print("ID  |    Category        |         Name        |  Price")
    print("--- | ------------------ | ------------------- | --------")
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<18} | {row[2]:<19} | {row[3]:<8}")
    conn.close()


def selected_type(item):
    conn = sqlite3.connect('MSMdatabase.db')

    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, product_price FROM product WHERE product_type = ?", (item,))
    rows = cursor.fetchall()
    count = 1
    print("ID  |        product      |   price")
    print("--- | ------------------- | ----------")
    for row in rows:
        print(f"{count:<3} |{row[0]:<20} | {row[1]:<10}")
        count += 1
        item = row[0]
        price = row[1]
        selected_item.append(item)
        selected_price.append(price)
    conn.close()
    selection.want(count - 1)

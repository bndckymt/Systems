import sqlite3

# Connect to a database
conn = sqlite3.connect('MSMdatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS product (
                number Integer PRIMARY KEY,
                product_type TEXT,
                product_name TEXT,
                product_price INTEGER)
                ''')
product_type = input('Enter type of product(beverage, cleaners,'
                     ' canned_dairies, junk_food_crackers, seasonings): ')
product_name = input('Enter name of the product: ')
product_price = input('enter price of the product: ')

# Insert data into the table
cursor.execute("INSERT INTO product (product_type, product_name, product_price) VALUES (?, ?, ?)",
               (product_type, product_name, product_price))

# Commit the changes
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM product")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

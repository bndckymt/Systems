import sqlite3

# Connection function to the SQLite database
def connect_to_db():
    return sqlite3.connect('menu.db')

# Function to initialize the database
def initialize_db():
    with connect_to_db() as conn:
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS menu (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            type TEXT NOT NULL,
                            item TEXT NOT NULL
                        )''')
        print("Database initialized and table created if it didn't exist.\n")

        # Check if the table is empty, and if so, insert predefined menu items
        cursor.execute("SELECT COUNT(*) FROM menu")
        count = cursor.fetchone()[0]
        if count == 0:
            menus = {
                1: ["Hotdog w/ Egg", "Corned Beef w/ Potato", "Sopas"],  # Breakfast
                2: ["Porkchop", "Salmon", "Lasagna"],                    # Lunch
                3: ["Grilled Chicken Salad", "Spaghetti Carbonara", "Pares"]  # Dinner
            }
            for menu_type, items in menus.items():
                for item in items:
                    if menu_type == 1:
                        cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Breakfast', item))
                    elif menu_type == 2:
                        cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Lunch', item))
                    elif menu_type == 3:
                        cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Dinner', item))
            print("Predefined menu items inserted into the database.\n")

# Function to load menu items from the database
def load_menus():
    menus = {1: [], 2: [], 3: []}  # Breakfast, Lunch, Dinner
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT type, item FROM menu")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 'Breakfast':
                menus[1].append(row[1])
            elif row[0] == 'Lunch':
                menus[2].append(row[1])
            elif row[0] == 'Dinner':
                menus[3].append(row[1])
    return menus

# Function to add a new menu item
def add_menu_item(menu_type, item):
    with connect_to_db() as conn:
        cursor = conn.cursor()
        if menu_type == 1:
            cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Breakfast', item))
        elif menu_type == 2:
            cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Lunch', item))
        elif menu_type == 3:
            cursor.execute("INSERT INTO menu (type, item) VALUES (?, ?)", ('Dinner', item))
        print(f"{item} added to the menu.")

# Function to delete a menu item
def delete_menu_item(item):
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu WHERE item = ?", (item,))
        print(f"{item} deleted from the menu.")

# Function to update a menu item
def update_menu_item(old_item, new_item):
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE menu SET item = ? WHERE item = ?", (new_item, old_item))
        print(f"{old_item} updated to {new_item}.")

# Function to search for a menu item
def search_menu_item(search_term):
    found = False
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT item FROM menu WHERE item LIKE ?", ('%' + search_term + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(f"Found: {row[0]}")
            found = True
    if not found:
        print("-----Item not found-----")

# Function to display all menu items
def display_menu():
    menus = load_menus()
    for menu_type, items in menus.items():
        print(f"\nMenu {menu_type}:")
        if not items:
            print("\tNo items available.")
        else:
            for i, item in enumerate(items):
                print(f"\t{i + 1}. {item}")

# Main program
print("--------------------------------------")
print("\tBienvenidos a sa hungry")
print("--------------------------------------\n")

initialize_db()  # Initialize the database and table
menus = load_menus()  # Load existing menu items from the database

opt = ""
while True:
    opt = input("Do you want to see the menu? y/n: ").lower()
    if opt not in ["y", "n"]:
        print("\n-----Invalid input. Please enter 'y' or 'n'.-----")
    else:
        break

while opt == "y":
    # Prompt user for menu selection
    menu_1 = 0
    while True:
        menu_1 = input("\nMENU \n\t1. Breakfast\n\t2. Lunch\n\t3. Dinner\n\nI want to order: ")
        if menu_1.isdigit() and 1 <= int(menu_1) <= 3:
            menu_1 = int(menu_1)
            break
        else:
            print("\n-----Invalid menu selection. Please enter 1, 2, or 3.-----")

    # Display the selected menu
    if menu_1 == 1:  # Breakfast Menu
        print("\nBreakfast Menu:")
        for i, item in enumerate(menus[1], start=1):
            print(f"\t{i}. {item}")

    elif menu_1 == 2:  # Lunch Menu
        print("\nLunch Menu:")
        for i, item in enumerate(menus[2], start=1):
            print(f"\t{i}. {item}")

    elif menu_1 == 3:  # Dinner Menu
        print("\nDinner Menu:")
        for i, item in enumerate(menus[3], start=1):
            print(f"\t{i}. {item}")

    # Ask user for action
    action = input("\nWhat would you like to do? (order/add/delete/update/search/display/exit): ").lower()

    if action == "order":
        item_number = int(input("Enter the item number you want to order: "))
        if menu_1 == 1 and item_number <= len(menus[1]):
            print(f"You ordered: {menus[1][item_number - 1]}")
        elif menu_1 == 2 and item_number <= len(menus[2]):
            print(f"You ordered: {menus[2][item_number - 1]}")
        elif menu_1 == 3 and item_number <= len(menus[3]):
            print(f"You ordered: {menus[3][item_number - 1]}")
        else:
            print("Invalid item number.")

    elif action == "add":
        new_item = input("Enter the name of the item to add: ")
        add_menu_item(menu_1, new_item)

    elif action == "delete":
        item_to_delete = input("Enter the name of the item to delete: ")
        delete_menu_item(item_to_delete)

    elif action == "update":
        old_item = input("Enter the name of the item to update: ")
        new_item = input("Enter the new name of the item: ")
        update_menu_item(old_item, new_item)

    elif action == "search":
        search_term = input("Enter the name of the item to search: ")
        search_menu_item(search_term)

    elif action == "display":
        display_menu()

    elif action == "exit":
        print("-----Thank you for visiting us! Have a great day!-----")
        break

    else:
        print("-----Invalid action. Please try again.-----")
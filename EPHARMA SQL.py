#Wendy Ortega
#Janelle Gattoc
#Khate Cassandra Pailognaa

import sqlite3

class PharmacySystem:
    def __init__(self):
        self.stores = {
            "1": "JGO Pharmacy",
            "2": "JP Rosette Pharmacy",
            "3": "Balauags Pharmacy",
            "4": "Jenny Pharmacy",
            "5": "Farmacia Marites",
            "6": "Catillo's Drug And Enterprises",
            "7": "Go Pharmacy",
            "8": "TGP The Generics Pharmacy",
            "9": "KC Pharmacy",
            "10": "RYT Pharmacy"
        }
        self.products = {
            "JGO Pharmacy": {
                "Contraceptives": ["Trust Pills", "Condoms Durex", "NuvaRing", "Postinor", "Implanon"],
                "First Aids": ["Band-Aid", "Betadine", "Antihistamines", "Tweezers", "Cotton Balls"],
                "Personal Hygiene": ["Colgate Toothpaste", "PH Care Feminine Wash", "Listerine", "Crest", "Palmolive Shampoo"],
                "Skincare/Beauty": ["Cetaphil Facial Cleanser", "Vaseline Lip Therapy", "Garnier Cleaner", "Aveeno Lotion", "Belo Sunscreen"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
            },
            "JP Rosette Pharmacy": {
                "Contraceptives": ["Postinor", "NuvaRing", "Trust Pills", "Condoms Durex", "Itraurine Devices"],
                "First Aids": ["Gauze Pads", "Thermometers", "Scissors", "Band-Aid", "Betadine", "Cotton Balls "],
                "Personal Hygiene": ["Sensodyne Toothpaste", "Dove Conditioner", "Colgate Toothpaste","Palmolive Shampoo", "PH Care Feminine Wash"],
                "Skincare/Beauty": ["Garnier Makeup Remover", "Belo Sunscreen", "The Ordinary Serum", "L'Oreal Mask", "Luxe Organic Toner"],
                "Medicines": ["Advil Ibuprofen", "Amoxicillin", "Noezep", "Decolgen", "Bonamin"]
            },
            "Balauags Pharmacy": {
                "Contraceptives": ["Itraurine Devices", "Implanon", "Ortho Tri-Cyclen", "Ortho Evra", "Mirena"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Disposable Gloves", "Triangular Bandages", "Safety Pins"],
                "Personal Hygiene": ["Head and Shoulders Shampoo", "Rexona Deodorant", "PH Care Feminine Wash","Whisper Napkin", "Herbal Essences"],
                "Skincare/Beauty": ["Cetaphil Facial Cleanser", "Vaseline Lip Therapy", "Garnier Cleaner","Aveeno Lotion", "Belo Sunscreen"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
            },
            "Jenny Pharmacy": {
                "Contraceptives": ["Nexplanon", "Conceptrol", "Kimono", "Sronyx", "Xulane"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Band-Aid", "Betadine", "Antihistamines"],
                "Personal Hygiene": ["Head and Shoulders Shampoo", "Rexona Deodorant", "PH Care Feminine Wash", "Whisper Napkin", "Herbal Essences"],
                "Skincare/Beauty": ["Cetaphil Facial Cleanser", "Vaseline Lip Therapy", "Garnier Cleaner", "Aveeno Lotion", "Belo Sunscreen"],
                "Medicines": ["Advil Ibuprofen", "Amoxicillin", "Noezep", "Decolgen", "Bonamin"]
            },
            "Farmacia Marites": {
                "Contraceptives": ["Nexplanon", "Conceptrol", "Kimono", "Sronyx", "Xulane"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Disposable Gloves", "Triangular Bandages", "Safety Pins"],
                "Personal Hygiene": ["Sensodyne Toothpaste", "Dove Conditioner", "Colgate Toothpaste", "Palmolive Shampoo", "PH Care Feminine Wash"],
                "Skincare/Beauty": ["Garnier Makeup Remover", "Belo Sunscreen", "The Ordinary Serum", "L'Oreal Mask", "Luxe Organic Toner"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
            },
            "Go Pharmacy": {
                "Contraceptives": ["Postinor", "NuvaRing", "Trust Pills", "Condoms Durex", "Itraurine Devices"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Disposable Gloves", "Triangular Bandages", "Safety Pins"],
                "Personal Hygiene": ["Sensodyne Toothpaste", "Dove Conditioner", "Colgate Toothpaste", "Palmolive Shampoo", "PH Care Feminine Wash"],
                "Skincare/Beauty": ["Garnier Makeup Remover", "Belo Sunscreen", "The Ordinary Serum", "L'Oreal Mask", "Luxe Organic Toner"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
            },
            "TGP The Generics Pharmacy": {
                "Contraceptives": ["Trust Pills", "Condoms Durex", "NuvaRing", "Postinor", "Implanon"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Antihistamines", "Tweezers", "Cotton Balls "],
                "Personal Hygiene": ["Colgate Toothpaste", "PH Care Feminine Wash", "Listerine", "Crest", "Palmolive Shampoo"],
                "Skincare/Beauty": ["Cetaphil Facial Cleanser", "Vaseline Lip Therapy", "Garnier Cleaner", "Aveeno Lotion", "Belo Sunscreen"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
                },
            "KC Pharmacy": {
                "Contraceptives": ["Postinor", "NuvaRing", "Trust Pills", "Condoms Durex", "Itraurine Devices"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Antihistamines", "Tweezers", "Cotton Balls "],
                "Personal Hygiene": ["Colgate Toothpaste", "PH Care Feminine Wash", "Listerine", "Crest","Palmolive Shampoo"],
                "Skincare/Beauty": ["Garnier Makeup Remover", "Belo Sunscreen", "The Ordinary Serum", "L'Oreal Mask", "Luxe Organic Toner"],
                "Medicines": ["Advil Ibuprofen", "Amoxicillin", "Noezep", "Decolgen", "Bonamin"]
            },
            "RYT Pharmacy": {
                "Contraceptives": ["Itraurine Devices", "Implanon", "Ortho Tri-Cyclen", "Ortho Evra", "Mirena"],
                "First Aids": ["Hydrogen Peroxide", "Medical Tape", "Antihistamines", "Tweezers", "Cotton Balls "],
                "Personal Hygiene": ["Sensodyne Toothpaste", "Dove Conditioner", "Colgate Toothpaste", "Palmolive Shampoo", "PH Care Feminine Wash"],
                "Skincare/Beauty": ["Cetaphil Facial Cleanser", "Vaseline Lip Therapy", "Garnier Cleaner","Aveeno Lotion", "Belo Sunscreen"],
                "Medicines": ["Biogesic Paracetamol", "Metformin", "Advil Ibuprofen", "Amoxicillin", "Solmux For Cough"]
            },
        }

        self.conn = sqlite3.connect('Epharma2_system.db')
        self.cursor = self.conn.cursor()
        self.initialize_db()
        self.user = None

    def initialize_db(self):
        # Create tables for stores, products, and users
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        ''')
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            store_id INTEGER,
            category TEXT,
            name TEXT,
            FOREIGN KEY (store_id) REFERENCES stores(id) ON DELETE CASCADE
        )
        ''')
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            address TEXT
        )
        ''')
        self.conn.commit()
        self.populate_initial_data()

    def populate_initial_data(self):
    # Insert stores into the database
        for store_id, store_name in self.stores.items():
            self.cursor.execute("SELECT id FROM stores WHERE id = ?", (store_id,))
            store = self.cursor.fetchone()
        if not store:
            self.cursor.execute("INSERT INTO stores (id, name) VALUES (?, ?)", (store_id, store_name))

    # Insert products and categories for each store
        for store_name, categories in self.products.items():
            self.cursor.execute("SELECT id FROM stores WHERE name = ?", (store_name,))
            store = self.cursor.fetchone()
            store_id = store[0] if store else None

            if store_id:
                for category, products in categories.items():
                # Insert each product in the corresponding category
                    for product in products:
                        self.cursor.execute("SELECT * FROM products WHERE store_id = ? AND category = ? AND name = ?",
                                        (store_id, category, product))
                    existing_product = self.cursor.fetchone()
                    if not existing_product:
                        self.cursor.execute("INSERT INTO products (store_id, category, name) VALUES (?, ?, ?)",
                                             (store_id, category, product))
            self.conn.commit()


    def welcome_message(self):
        print("Welcome to the Pharmacy Management System!")

    def proceed_prompt(self):
        print("\n1. Proceed with an action\n2. Exit")
        return input("Enter your choice: ")

    def register_user(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        self.cursor.execute("INSERT INTO users (name, age, address) VALUES (?, ?, ?)", (name, age, address))
        self.conn.commit()
        print("User registered successfully!")

    def edit_registration(self):
        self.cursor.execute("SELECT * FROM users")
        user = self.cursor.fetchone()  # Get the first user for editing (if any)
        
        if not user:
            print("No user registered yet.")
            return

        self.user = user  # Store the user's details
        print(f"Current details: Name: {self.user[1]}, Age: {self.user[2]}, Address: {self.user[3]}")
        
        new_name = input("Enter new name (leave blank to keep current): ")
        new_age = input("Enter new age (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")

        # Update only the fields that the user has entered
        if new_name:
            self.cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, self.user[0]))
        if new_age:
            self.cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, self.user[0]))
        if new_address:
            self.cursor.execute("UPDATE users SET address = ? WHERE id = ?", (new_address, self.user[0]))
        
        self.conn.commit()
        print("User information updated successfully!")

    def choose_store(self):
        self.cursor.execute("SELECT id, name FROM stores")
        stores = self.cursor.fetchall()
        if not stores:
            print("No stores available.")
            return None
        print("Available Stores:")
        for store in stores:
            print(f"{store[0]}. {store[1]}")
        try:
            store_id = int(input("Enter the store ID to choose: "))
            store = next((store for store in stores if store[0] == store_id), None)
            if store:
                print(f"You chose {store[1]}.")
                return store[0]  # Return the store ID
            else:
                print("Store not found.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    def choose_product(self, store_id):
        self.cursor.execute("SELECT category, name FROM products WHERE store_id = ?", (store_id,))
        products = self.cursor.fetchall()

        if not products:
            print("No products available in this store.")
            return
        
        print("Available Products:")
        categories = set([product[0] for product in products])  
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. Category: {category}")

        category_choice = int(input("Choose a category by number: ")) - 1
        selected_category = list(categories)[category_choice]

        print(f"\nAvailable products in '{selected_category}' category:")
        products_in_category = [product[1] for product in products if product[0] == selected_category]
        for idx, product in enumerate(products_in_category, start=1):
            print(f"{idx}. {product}")

        product_choice = int(input("Choose a product by number: ")) - 1
        selected_product = products_in_category[product_choice]
        print(f"You chose '{selected_product}' from category '{selected_category}'.")

    def add_store(self):
        store_name = input("Enter new store name: ")
        store_id = len(self.stores) + 1
        self.stores[str(store_id)] = store_name
        self.cursor.execute("INSERT INTO stores (id, name) VALUES (?, ?)", (store_id, store_name))
        self.conn.commit()
        print(f"Store '{store_name}' added successfully!")

    def add_category(self):
        store_id = self.choose_store()
        if store_id is None:
            print("Store not found.")
            return
        category_name = input("Enter new category name: ")
        self.cursor.execute("INSERT INTO products (store_id, category, name) VALUES (?, ?, ?)", (store_id, category_name, ""))
        self.conn.commit()
        print(f"Category '{category_name}' added to store.")

    def add_product(self):
        store_id = self.choose_store()
        if store_id is None:
            print("Store not found.")
            return
        category_name = input("Enter category name for the product: ")
        product_name = input("Enter product name: ")
        self.cursor.execute("INSERT INTO products (store_id, category, name) VALUES (?, ?, ?)", (store_id, category_name, product_name))
        self.conn.commit()
        print(f"Product '{product_name}' added to category '{category_name}'.")

    def delete_store(self):
        store_id = int(input("Enter store ID to delete: "))
        self.cursor.execute("DELETE FROM stores WHERE id = ?", (store_id,))
        self.conn.commit()
        print(f"Store with ID {store_id} deleted successfully.")

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: "))
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        print(f"Product with ID {product_id} deleted successfully.")

    def delete_category(self):
        store_id = self.choose_store()
        if store_id is None:
            print("Store not found.")
            return
        category_name = input("Enter category name to delete: ")
        self.cursor.execute("DELETE FROM products WHERE store_id = ? AND category = ?", (store_id, category_name))
        self.conn.commit()
        print(f"Category '{category_name}' deleted from store.")

    def view_stores(self):
        self.cursor.execute("SELECT id, name FROM stores")
        stores = self.cursor.fetchall()
        if not stores:
            print("No stores available.")
            return
        print("Stores:")
        for store in stores:
            print(f"{store[0]}. {store[1]}")

    def start(self):
        self.welcome_message()
        while True:
            action = self.proceed_prompt()
            if action == "1":
                print("\n1. Register\n2. Edit Registration\n3. Choose Store\n4. View Stores\n5. Add Store\n6. Add Category\n7. Add Product\n8. Delete Store\n9. Delete Product\n10. Delete Category\n11. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.register_user()
                elif choice == "2":
                    self.edit_registration()
                elif choice == "3":
                    store_id = self.choose_store()
                    if store_id:
                        self.choose_product(store_id)
                elif choice == "4":
                    self.view_stores()
                elif choice == "5":
                    self.add_store()
                elif choice == "6":
                    self.add_category()
                elif choice == "7":
                    self.add_product()
                elif choice == "8":
                    self.delete_store()
                elif choice == "9":
                    self.delete_product()
                elif choice == "10":
                    self.delete_category()
                elif choice == "11":
                    print("Thank you visting E-pharma!")
                    break
            elif action == "2":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = PharmacySystem()
    system.start()

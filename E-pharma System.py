#Wendy Ortega
#Janelle Gattoc
#Ghrielle Khate Cassandra Pailogna

import json

class PharmacySystem:
    def __init__(self):
        self.load_data()
        self.user_info = {}

    def load_data(self):
        try:
            with open('pharmacy_data.json', 'r') as file:
                data = json.load(file)
                self.stores = data['stores']
                self.products = data['products']
        except FileNotFoundError:
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

    def save_data(self):
        with open('pharmacy_data.json', 'w') as file:
            json.dump({'stores': self.stores, 'products': self.products}, file)

    def welcome_message(self):
        print("Welcome to E-pharma: Your Trusted Online Pharmacy")

    def proceed_prompt(self):
        choice = input("Do you want to proceed? " "Press 1 if yes, 2 if no: ")
        return choice

    def register_user(self):
        self.user_info = {}
        self.user_info['name'] = input("Enter your name: ")
        self.user_info['age'] = input("Enter your age: ")
        self.user_info['address'] = input("Enter your address: ")
        print("Your registration was successful!")

    def edit_registration(self):
        print("Edit Registration Details:")
        for key in self.user_info:
            new_value = input(f"Enter new {key} (leave blank to keep current): ")
            if new_value:
                self.user_info[key] = new_value
        print("Registration details updated successfully!")

    def choose_store(self):
        print("E-Pharmacy stores:")
        for key, value in self.stores.items():
            print(f"{key}. {value}")
        store_choice = input("Choose your preferable store (1-10): ")
        store_name = self.stores.get(store_choice)
        return store_name

    def display_categories(self, store_name):
        print(f"Available product categories for {store_name}:")
        categories = self.products.get(store_name, {})
        if categories:
            for idx, category in enumerate(categories.keys(), start=1):
                print(f"{idx}. {category}")
        else:
            print("No categories available.")

    def choose_category(self, store_name):
        categories = self.products.get(store_name, {})
        if not categories:
            print("No categories available.")
            return None
        while True:
            try:
                choice = int(input("Choose a category by number: "))
                category = list(categories.keys())[choice - 1]
                return category
            except (IndexError, ValueError):
                print("Invalid choice. Please enter a number corresponding to the category.")

    def display_products(self, store_name, category):
        print(f"Products in the '{category}' category at {store_name}:")
        products = self.products.get(store_name, {}).get(category, [])
        if products:
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product}")
        else:
            print("No products available in this category.")

    def choose_product(self, store_name, category):
        products = self.products.get(store_name, {}).get(category, [])
        if not products:
            print("No products available.")
            return None
        while True:
            try:
                choice = int(input("Enter the product number to purchase: "))
                product = products[choice - 1]
                return product
            except (IndexError, ValueError):
                print("Invalid choice. Please enter a valid product number.")

    def add_store(self):
        store_id = input("Enter new store ID: ")
        store_name = input("Enter new store name: ")
        if store_id in self.stores:
            print("Store ID already exists.")
        else:
            self.stores[store_id] = store_name
            self.products[store_name] = {}  # Initialize with an empty category dictionary
            print(f"Store '{store_name}' added successfully!")

    def add_category(self, store_name):
        if store_name not in self.products:
            print("Store not found.")
            return

        category = input("Enter the category name to add: ")
        if category in self.products[store_name]:
            print("Category already exists.")
        else:
            self.products[store_name][category] = []
            print(f"Category '{category}' added successfully to {store_name}.")

    def add_product(self, store_name, category):
        if store_name not in self.products or category not in self.products[store_name]:
            print("Store or category not found.")
            return

        product = input("Enter the product name to add: ")
        if product in self.products[store_name][category]:
            print("Product already exists in this category.")
        else:
            self.products[store_name][category].append(product)
            print(f"Product '{product}' added successfully to category '{category}' in {store_name}.")

if __name__ == "__main__":
    system = PharmacySystem()
    system.welcome_message()

    while True:
        proceed = system.proceed_prompt()
        if proceed == "1":
            action = input(
                " 1. Register User\n 2. Edit Registration\n 3. Choose Store\n 4. Add Store\n 5. Add Category\n 6. Add Product\n 7. Exit\n Choose action: ")
            if action == "1":
                system.register_user()
            elif action == "2":
                system.edit_registration()
            elif action == "3":
                store_name = system.choose_store()
                if store_name:
                    system.display_categories(store_name)
                    category = system.choose_category(store_name)
                    if category:
                        system.display_products(store_name, category)
                        product = system.choose_product(store_name, category)
                        if product:
                            print(f"You have chosen to purchase: {product}")
            elif action == "4":
                system.add_store()
            elif action == "5":
                store_name = system.choose_store()
                if store_name:
                    system.add_category(store_name)
            elif action == "6":
                store_name = system.choose_store()
                if store_name:
                    category = system.choose_category(store_name)
                    if category:
                        system.add_product(store_name, category)
            elif action == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        elif proceed == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
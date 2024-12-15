# Display the category

import sqlite3 as FS


def connect():
    database = FS.connect('feby.db')
    return database

def initialized():
    ring = connect()
    cursor = ring.cursor()
    ring.execute("""CREATE TABLE DATA (
                CUSTOMER TEXT NOT NULL,
                AMOUNT_PAID REAL NOT NULL
                )""")
    ring.commit()
    cursor.close()
    ring.close()

def customers(AMOUNT_PAID):
    while True:
        CUSTOMER = input("Enter your name: ")
        ADDRESS = input("Enter your address: ")
        ring = connect()
        cursor = ring.cursor()
        sql = "INSERT INTO DATA (CUSTOMER, ADDRESS, AMOUNT_PAID) VALUES (?, ?, ?)"

        cursor.execute(sql, (CUSTOMER,ADDRESS, AMOUNT_PAID))
        ring.commit()
        cursor.close()
        ring.close()
        print("THANKS!\n")
        break

def line():
    print("-" * 50)

line()
print("Welcome to the Fashion Store!")
line()

cart = []

def payment(amount):
    customers(amount)
    while True:
        try:
            line()
            print("You have to pay a total amount of", amount)
            cash = int(input("please enter your cash amount: "))
            if cash >= amount:
                cash -= amount
                print("Change:", cash)
                print("thank you for buying")
                break
            elif amount < cash:
                print("Invalid input... please enter the right amount of your purchase")
        except ValueError:
            print("Invalid input... please try again")
        break

def your_cart(val):
    if val == 1:
        line()
        print("   item                 value")
        total = 0
        count = 1
        for item, value in cart:
            print(f"{count} {item:<21} {value:.2f}")
            count += 1
            total += value
        print(f"                  total:{total:.2f}")
        mainmenu(1)
    elif val == 2:
        print("   item                 value")
        total = 0
        count = 1
        for item, value in cart:
            print(f"{count} {item:<21} {value:.2f}")
            count += 1
            total += value
        print(f"                  total:{total:.2f}")
        print("Thank you for buying")
        payment(total)
    elif val == 3:
        print("   item                 value")
        total = 0
        count = 1
        for item, value in cart:
            print(f"{count} {item:<21} {value:.2f}")
            count += 1
            total += value
        print(f"                  total:{total:.2f}")
        print("\n\nWhat product would you like to remove? ")
        answer = int(input("anwer: "))
        cart.pop(answer-1)
        mainmenu(1)
def mainmenu(value):
    # initialized()
    if value == 1:
        while True:
            try:
                line()
                again = input("Would you like to buy more product?\n"
                              "[1] Your cart\n"
                              "[2] Remove a product\n"
                              "[y] Yes\n"
                              "[n] no\n"
                              "answer: ")
                if again.lower() == 'y':
                    value = 0
                    break
                elif again.lower() == 'n':
                    your_cart(2)
                    break
                elif again == '1':
                    your_cart(1)
                elif again == '2':
                    your_cart(3)
                else:
                    print("invalid input")
            except ValueError:
                print("Invalid input")
    if value == 0:
        line()
        print("Please select a category:")
        print("1. Clothes")
        print("2. Bags")
        print("3. Perfumes")
        print("4. Shoes or Sandals")
        print("5. Jewelry")
        print("6. Cosmetics")
        print("7. Hair Treatment")
        while True:
            try:
                selection = int(input("Enter your choice: "))
                if selection == 1:
                    Clothes()
                    break
                elif selection == 2:
                    Bags()
                    break
                elif selection == 3:
                    Perfumes()
                    break
                elif selection == 4:
                    ShoesorSandals()
                    break
                elif selection == 5:
                    Jewelry()
                    break
                elif selection == 6:
                    Cosmetics()
                    break
                elif selection == 7:
                    HairTreatment()
                    break
                else:
                    print("Invalid choice. Enter a number between 1-7.")
            except ValueError:
                print("Invalid input. Please enter a number.")



def display_submenu(category_number):
    subcategories = {
        1: ["T-shirts", "Jeans", "Jackets", "Suits", "Sweaters"],
        2: ["Backpacks", "Handbags", "Totes", "Clutches", "Messenger bags"],
        3: ["Eau de toilette", "Eau de parfum", "Cologne", "Body spray"],
        4: ["Sneakers", "Loafers", "Boots", "Sandals", "Dress shoes"],
        5: ["Necklaces", "Bracelets", "Earrings", "Rings", "Brooches"],
        6: ["Foundation", "Lipstick", "Mascara", "Eye shadow", "Blush"],
        7: ["Hair dryer", "Straightener", "Curling iron", "Hair brush", "Hair serum"]
    }
    product = category_number
    options = subcategories.get(category_number, [])
    print("\nAvailable options: ")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    while True:
        try:
            line()
            item_choice = int(input("\nEnter the number of the item you want to learn more about: "))
            if category_number == 1 or 2 or 3 or 4 or 5 or 6 or 7:
                display_brands(product, item_choice)  # For Clothes, show brands after item selection
            else:
                description = display_item_description(category_number, item_choice)
                print(f"\nDescription: {description}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_brands(subcategory_number, items):
    brands = {}
    if subcategory_number == 1:
        brands = {
            1: [["Nike", 2195], ["Adidas", 1800], ["H&M", 399], ["Zara", 1900]],  # T-shirts
            2: [["Levi's", 1729], ["Wrangler", 2000], ["Diesel", 11000], ["Guess", 3999]],  # Jeans
            3: [["The North Face", 4000], ["Patagonia", 2380], ["Canada Goose", 6798], ["Columbia", 5490]],  # Jackets
            4: [["Hugo Boss", 27000], ["Armani", 200000], ["Ralph Lauren", 83994], ["Gucci", 196000]],  # Suits
            5: [["Tommy Hilfiger", 6500], ["Gap", 1500], ["Uniqlo", 1490], ["Calvin Klein", 5565]]  # Sweaters
        }
    elif subcategory_number == 2:
        brands = {
            1: [["Osprey", 16990], ["Jansport", 800], ["Dueter", 6536], ["Adidas", 2490], ["Baggu", 4633]],
            2: [["Hermes", 6699], ["Loui Vuitton", 82204], ["Prada", 11550],
                ["Saint Laurent", 67086], ["Channel", 12950]],
            3: [["Gucci", 60000], ["Channel", 11550], ["Prada", 11244], ["Adidas", 2000], ["Jansport", 2490]],
            4: [["Dior", 2500], ["Cole Haan", 3990], ["Hollow rose diamond", 3690],
                ["New pearl small", 1099], ["Pedro Studio", 9100]],
            5: [["DVL Iusso", 1999], ["Converse", 2290], ["Crumpler", 3900], ["Puma", 1800], ["World traveller", 2190]]
        }
    elif subcategory_number == 3:
        brands = {
            1: [["Dior",1500], ["Oxygn",413], ["Triumph",299], ["Os man thus",3900], ["Cool water",5098]],
            2: [["Estee lauder",5029], ["Chanel",5000], ["Void",4500], ["Sigl",4999], ["Dansesauvage",3900]],
            3: [["Dorin",11000], ["Bench", 100], ["Calvin",3395], ["Escape",1250]],
            4: [["Jo Malone", 1128], ["SPRIG", 1404], ["Shea", 850], ["LUSH Authentic", 2544], ["Paco Rabanne", 1583]]
            }
    elif subcategory_number == 4:
        brands = {
            1: [["Nike gamma force", 4995], ["ordan1 retro low dior", 1322648], ["Vans knu", 2980], ["Arc brothers", 2559]],
            2: [["Mario D boro", 2760], ["Dr. Martens", 1270], ["Bigstrut loafers", 3000],["Alta penny loafers", 950], ["Tassel martin", 399]],
            3: [["Dr. Martens", 1800], ["Mardini", 1900], ["Chelsea", 1443], ["Marquins", 2990], ["Surgut vancat", 2698]],
            4: [["Arizona", 1329], ["Skechers", 3795], ["Birkenstock", 2228], ["Sperry", 1195], ["Michaela velcro", 1499]],
            5: [["Marquins", 2990],["Mario D boro", 1990],["Bibo",2749],["Christen", 1000]]}
    elif subcategory_number == 5:
        brands = {
            1: [["Amethyst heart", 1146], ["Daniel wellington", 4950], ["Saudi gold VCA", 5200],
                ["PRYA Jewelry", 2648], ["Valentino", 20364]],
            2: [["Daniel wellington", 10960], ["Tory Burch kira", 8392], ["Valentino", 23489], ["Louis Vuitton", 18000],
                ["Unclou Bracelet", 277537]],
            3: [["Ross-simons", 8871], ["CUOKA MIRACLE", 2116], ["Zel", 2450], ["Michael Kors", 7187],
                ["Setéur Paris", 18832]],
            4: [["Moonstone Lab", 26300], ["Messika", 167000], ["LIV 18k gold", 10500], ["Aramis", 44850],
                ["Illios", 29394]],
            5: [["EMEGCY", 1336], ["Mooclife", 2784], ["Dolce & gabbana", 19357], ["Chanel", 57778], ["Elite", 4978]]
        }
    elif subcategory_number == 6:
        brands = {
            1: [["Tarte", 2399], ["Clinique", 3355], ["E.L.F", 1960], ["The Ordinary", 5206], ["Uoma", 3559]],
            2: [["Carslan", 1002], ["Clinique", 1702], ["Sephora", 2087], ["Rituel De Fille", 1394],
                ["Souffle Matte", 1450]],
            3: [["Maybelline", 1390], ["Guerlain Noir", 1800], ["Pere Perez", 1616], ["Kaja", 1321],
                ["Oreal", 2845]],
            4: [["Maybelle", 1199], ["Urban Decay", 2249], ["NYX", 2328], ["MAC", 3400], ["The Zodiac", 1389]],
            5: [["Clinique", 1620], ["Dior", 2369], ["Nars", 2500], ["Sasa", 1506], ["Suqqu", 1899]]}
    elif subcategory_number == 7:
        brands = {
            1: [["Philips", 1299], ["Gladking", 1350], ["Beauty Star", 1650], ["Remington", 2125],
                      ["Super professional", 2477]],
            2: [["Philips", 4599], ["MAC", 2000], ["Remington", 3732], ["Titanium", 1778], ["JML Supra", 3120]],
            3: [["Philips", 3955], ["Conair", 1579], ["Dreame", 4880], ["Babyliss", 1259], ["W Elite", 3999]],
            4: [["Goody Smooth Blends", 1199], ["Morrocanoil", 1800], ["Denman", 1995], ["Jill Stuart", 2844],
                      ["AZH", 2304]],

            5: [["Creamsilk", 219], ["L’Oreal paris", 909], ["Kerastase", 3231], ["Mise En Scene", 1856],
                      ["Argan oil", 1116]]}

    selected_brands = brands.get(items, [])
    if not selected_brands:
        print("Invalid subcategory.")
        return
    line()
    print("\nAvailable brands: \n"
          "   item                           price")
    for idx, brand in enumerate(selected_brands, 1):
        print(f"{idx}. {brand[0]:<25}", f"{f"{brand[1]:.2f}":>10}")

    while True:
        try:
            brand_choice = int(input("\nSelect a brand to view its description: "))
            if 1 <= brand_choice <= len(selected_brands):
                description = display_brand_description(subcategory_number, brand_choice)
                print(f"\nDescription: {description}")
            else:
                print("Invalid brand selection.")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    item = brands[items][brand_choice - 1]
    cart.append(item)


    mainmenu(1)


def display_brand_description(subcategory_number, brand_number):
    brand_descriptions = {
        1: ["Nike T-shirts: Comfortable and sporty.", "Adidas T-shirts: Stylish and casual.",
            "H&M T-shirts: Affordable fashion.", "Zara T-shirts: Trendy and chic."],
        2: ["Levi's Jeans: Iconic denim wear.", "Wrangler Jeans: Durable and rugged.",
            "Diesel Jeans: Premium quality.", "Guess Jeans: Fashion-forward designs."],
        3: ["The North Face Jackets: High-performance outdoor wear.", "Patagonia Jackets: Eco-friendly and durable.",
            "Canada Goose Jackets: Extreme weather protection.", "Columbia Jackets: Affordable outdoor gear."],
        4: ["Hugo Boss Suits: Classic formal wear.", "Armani Suits: Luxury and sophistication.",
            "Ralph Lauren Suits: Timeless elegance.", "Gucci Suits: High-fashion statement."],
        5: ["Tommy Hilfiger Sweaters: Classic American style.", "Gap Sweaters: Everyday comfort.",
            "Uniqlo Sweaters: Simple and functional.", "Calvin Klein Sweaters: Modern and sleek."]
    }

    descriptions_list = brand_descriptions.get(subcategory_number, [])
    if 1 <= brand_number <= len(descriptions_list):
        return descriptions_list[brand_number - 1]
    else:
        return "Invalid brand number."


def display_item_description(category_number, item_number):
    descriptions = {
        1: ["soft classic.", "casual versatile.", "perfect for colder weather.",
            "tailored elegance.", "cozy warmth."],
        2: ["functional style.", "stylish and elegant.", "roomy and practical.",
            "compact and chic.", "smart carry."],
        3: ["light and refreshing.", "long-lasting and intense.", "for a more personal touch.",
            "classic scent.", "instant refresh."],
        4: ["casual and sporty.", "comfortable for daily wear.", "durable and stylish.",
            "ideal for warm weather.", "elegant and formal."],
        5: ["adds elegance to outfits.", "stylish and versatile.", "enhances features.",
            "classic and timeless.", "sophisticated touch."],
        6: ["evens skin tone.", "colorful lips.", "lengthens lashes.", "colorful eyes.",
            "adds color to cheeks."],
        7: ["dries hair quickly.", "smooths and straightens.", "curls hair easily.",
            "detangles and styles.", "adds shine and reduces frizz."]
    }

    descriptions_list = descriptions.get(category_number, [])

    if 1 <= item_number <= len(descriptions_list):
        return descriptions_list[item_number - 1]
    else:
        return "Invalid item number."


def Clothes():
    print("You selected Clothes.")
    display_submenu(1)


def Bags():
    print("You selected Bags.")
    display_submenu(2)


def Perfumes():
    print("You selected Perfumes.")
    display_submenu(3)


def ShoesorSandals():
    print("You selected Shoes or Sandals.")
    display_submenu(4)


def Jewelry():
    print("You selected Jewelry.")
    display_submenu(5)


def Cosmetics():
    print("You selected Cosmetics.")
    display_submenu(6)


def HairTreatment():
    print("You selected Hair Treatment.")
    display_submenu(7)


mainmenu(0)


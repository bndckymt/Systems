

cart = []
cost = []
amount = []


# Check out function
def check_out(fees):
    while True:
        total_amount = sum(cost)
        if fees == 0:
            item_in_cart(value=2)
            break
        if fees == 1:
            while True:
                try:
                    line()
                    space()
                    line()
                    print(f"Dear customer you've bought a product with a total amount of {total_amount}")
                    cash = float(input("Please enter your cash amount: "))
                    if cash >= total_amount:
                        cash = cash - total_amount
                        print(f"Change: {cash}")
                        fees = 2
                        break
                    elif cash < total_amount:
                        print("Cash insufficient....\nplease enter the right amount")
                    else:
                        print("Invalid input\n")
                except ValueError:
                    print("Invalid input\nPlease try again")
        elif fees == 2:
            address = input("Enter your address: ")
            line()
            space()
            line()
            print("Thank you for shopping with us!\n")
            print("Your address: ", address)
            break
        else:
            print("Closing the system")
            break


# remove a product
def remove(delete):
    if delete == 0:
        item_in_cart(value=0)
        print("What product would you like to remove from your cart?\n")
        delete = 1
    if delete == 1:
        choose = int(input("Answer: "))
        cart.pop(choose-1)
        amount.pop(choose-1)
        cost.pop(choose-1)
        item_in_cart(value=1)


# item in your cart
def item_in_cart(value):
    line()
    print("here are the list of the items in your cart:\n")
    count = 1
    print(f"    {"quantity":>5}", f"{"  item":<11}", f"     {"cost":>5}")
    for items in cart:
        print(f"[{count}]", f"{amount[count - 1]}    ", f"{items:<15}",
              f"{f"{cost[count - 1]:.2f}":>10}")
        count += 1
    print("                      total: ", f"{sum(cost):.2f}")
    if value == 0:
        remove(delete=1)
    if value == 1:
        again()
    if value == 2:
        check_out(fees=1)


# print a line
def line():
    print("-" * 50)


# print a space
def space():
    print("\n" * 2)


# for looping if the user want to buy more product or edit his/her purchase
def again():
    line()
    space()
    line()
    print("Do you want to continue buying more products?\n"
          "[1] Yes\n"
          "[0] No\n"
          "[R] Remove a product\n"
          "[Y] Your cart\n"
          "[C] Check out\n")
    while True:
        response = input("Answer: ")
        try:
            if response == '1':
                introduction()
                break
            elif response == '0':
                print("Closing the system")
                break
            elif response == 'Y':
                item_in_cart(value=1)
                break
            elif response == 'R':
                remove(delete=0)
                break
            elif response == 'C':
                check_out(fees=0)
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")


# display the item, price, and quantity of your total purchase
def purchase(item, price, quantity):
    if quantity != 0:
        amount.append(quantity)
    if item != 0:
        cart.append(item)
    if price != 0:
        price = price * quantity
        cost.append(price)
    total = list(cost)
    count = 1
    print(f" {"quantity":>5}", f"{"  item":<11}", f"     {"cost":>5}")
    for items in cart:
        print(f"[{count}]", f"{amount[count - 1]}    ", f"{items:<15}",
              f"{f"{cost[count - 1]:.2f}":>10}")
        count += 1
    print("                      total: ", f"{sum(total):.2f}")
    again()


# A list of beverage products
def beverage():
    line()
    space()
    line()
    beverage_products = ('Coke', 'Sprite', 'Royal', 'Gin', 'Alfonso', 'Red Horse')
    beverage_price = [192.00, 190.00, 190.00, 1464.00, 3180.00, 720.00]
    count = 1
    for item in beverage_products:
        print(f"[{count}]", f"{item:<15}", f"{f"{beverage_price[count - 1]:.2f}":>10}")
        count += 1
    line()
    while True:
        try:
            get = int(input("answer: "))
            if get > count-1:
                print("invalid Input")
            else:
                break
        except ValueError:
            print("invalid Input")
    line()
    space()
    line()
    quantity = int(input(f"How many {beverage_products[get - 1]} would you like to buy? "))
    purchase(beverage_products[get - 1], beverage_price[get - 1], quantity)


# A list of cleaning products
def cleaners():
    line()
    space()
    line()
    cleaners_products = ('Safeguard', 'Colgate', 'Cream silk', 'Palmolive', 'Tide', 'Surf', 'Downy')
    cleaners_price = [20.00, 8.00, 5.00, 5.00, 10.00, 6.00, 6.00]
    count = 1
    for item in cleaners_products:
        print(f"[{count}]", f"{item:<15}", f"{f"{cleaners_price[count - 1]:.2f}":>10}")
        count += 1
    line()
    while True:
        try:
            get = int(input("answer: "))
            if get > count-1:
                print("invalid Input")
            else:
                break
        except ValueError:
            print("invalid Input")
    line()
    space()
    line()
    quantity = int(input(f"How many {cleaners_products[get - 1]} would you like to buy? "))
    purchase(cleaners_products[get - 1], cleaners_price[get - 1], quantity)


# A list of canned products
def canned_dairies():
    line()
    space()
    line()
    canned_dairies_products = ('Youngstown', 'Wow ulam', 'Corned beef', 'Meatloaf', 'Pure foods',
                               'Egg', 'Cheese', 'Milk', 'Butter', 'Palm oil', 'Sugar')
    canned_dairies_price = [20.00, 25.00, 30.00, 28.00, 35.00, 270.00, 35.00, 30.00, 35.00, 23.00, 18.00]
    count = 1
    for item in canned_dairies_products:
        if count < 10:
            print(f"[{count}]", f"{item:<15}", f"{f"{canned_dairies_price[count - 1]:.2f}":>10}")
            count += 1
        else:
            print(f"[{count}]", f"{item:<15}", f"{f"{canned_dairies_price[count - 1]:.2f}":>9}")
            count += 1
    line()
    while True:
        try:
            get = int(input("answer: "))
            if get > count-1:
                print("invalid Input")
            else:
                break
        except ValueError:
            print("invalid Input")
    line()
    space()
    line()
    quantity = int(input(f"How many {canned_dairies_products[get - 1]} would you like to buy? "))
    purchase(canned_dairies_products[get - 1], canned_dairies_price[get - 1], quantity)


# A list of junk food products
def junk_food_crackers():
    line()
    space()
    line()
    junk_food_crackers_products = ('Cracklings', 'Mang juan', 'Loaded', 'Pewee', 'Onion rings',
                               'Fita', 'Cheese cake', 'Choco mucho')
    junk_food_crackers_price = [6.00, 6.00, 7.00, 7.00, 6.00, 55.00, 70.00, 90.00]
    count = 1
    for item in junk_food_crackers_products:
        print(f"[{count}]", f"{item:<15}", f"{f"{junk_food_crackers_price[count - 1]:.2f}":>10}")
        count += 1
    line()
    while True:
        try:
            get = int(input("answer: "))
            if get > count-1:
                print("invalid Input")
            else:
                break
        except ValueError:
            print("invalid Input")
    line()
    space()
    line()
    quantity = int(input(f"How many {junk_food_crackers_products[get - 1]} would you like to buy? "))
    purchase(junk_food_crackers_products[get - 1], junk_food_crackers_price[get - 1], quantity)


# A list of seasoning products
def seasonings():
    line()
    space()
    line()
    seasonings_products = ('Magic sarap', 'Aji nomoto', 'Knor cubes', 'Sinigang mix', 'Oyster sauce',
                               'Soy sauce', 'Vinegar')
    seasonings_price = [4.00, 3.00, 5.00, 10.00, 5.00, 10.00, 10.00,]
    count = 1
    for item in seasonings_products:
        print(f"[{count}]", f"{item:<15}", f"{f"{seasonings_price[count - 1]:.2f}":>10}")
        count += 1
    line()
    while True:
        try:
            get = int(input("answer: "))
            if get > count-1:
                print("invalid Input")
            else:
                break
        except ValueError:
            print("invalid Input")
    line()
    space()
    line()
    quantity = int(input(f"How many {seasonings_products[get - 1]} would you like to buy? "))
    purchase(seasonings_products[get - 1], seasonings_price[get - 1], quantity)


# A list of information of products
def more_info():
    line()
    print("Beverage: Beverages refer to any liquid that you can drink.\n"
          " They come in various forms, including soft drinks, juices,\n"
          " coffee, tea, and even alcoholic drinks like beer and wine.\n"
          " These are typically consumed for refreshment or hydration.\n\n"
          "Cleaners: Cleaners are household products used for \n"
          " cleaning and maintaining hygiene. They include items like dishwashing\n"
          " liquid, surface cleaners, laundry detergent, and disinfectants. \n"
          " Keeping things spick and span! \n"
          "Personal Care: Personal care products are all about self-care. They\n"
          " include toiletries like shampoo, soap, toothpaste, and skincare\n"
          " items. Taking care of yourself is essential, whether it’s a relaxing\n"
          " bath or brushing your teeth before bed.\n\n"
          "Canned: Canned goods are food items preserved in metal containers.\n"
          " They have a long shelf life and are convenient for storage. \n"
          " Examples include canned vegetables, soups, and fruits. Just be\n"
          " mindful of sodium content in some canned products.\n\n" 
          "Dairy: Dairy products come from milk. They include items like cheese,\n"
          " yogurt, butter, and milk itself. Dairy provides essential nutrients \n"
          " like calcium and protein. Plus, it’s a staple in \n"
          " many cuisines around the world.\n\n"
          "Junk Foods: Junk foods are tasty but often less nutritious\n"
          " snacks. They’re usually high in calories, sugar, salt, and\n"
          " unhealthy fats. Think of potato chips, candy bars, and sugary \n"
          " sodas. While they’re enjoyable as occasional treats, it’s essential\n"
          " to balance them with healthier options.\n\n"
          "Seasonings: Seasonings are flavor enhancers used to make food more \n"
          " delicious. They include herbs, spices, and condiments. Think of \n"
          " salt, pepper, garlic powder, cinnamon, and oregano. They add \n"
          " depth and character to your dishes.\n\n")
    line()
    introduction()


# Display the categories
def introduction():
    print("here is our products\n"
          "[1] Beverage\n"
          "[2] Cleaners\n"
          "[3] Canned and Dairies\n"
          "[4] Junk food and Crackers\n"
          "[5] Seasonings\n"
          "[6] More info\n"
          "[7] Back to cart\n"
          "[x] Exit")

    while True:
        line()
        pick = input("Answer: ")
        try:
            if pick == '1':
                beverage()
                break
            elif pick == '2':
                cleaners()
                break
            elif pick == '3':
                canned_dairies()
                break
            elif pick == '4':
                junk_food_crackers()
                break
            elif pick == '5':
                seasonings()
                break
            elif pick == '6':
                more_info()
                break
            elif pick == '7':
                item_in_cart(value=1)
                break
            elif pick == 'x':
                print("Closing the system")
                break
            else:
                line()
                print("Invalid input\n"
                      "Please try again\n"
                      "here is our product\n"
                      "[1] Beverage\n"
                      "[2] Cleaners\n"
                      "[3] Canned and Dairies\n"
                      "[4] Junk food and Cracker\n"
                      "[5] Seasonings\n"
                      "[6] More info\n"
                      "[7] Back to cart\n"
                      "[x] Exit")

        except ValueError:
            print("Invalid input\n"
                  "Please try again\n"
                  "here is our product\n"
                  "[1] Beverage\n"
                  "[2] Cleaners\n"
                  "[3] Canned and Dairies\n"
                  "[4] Junk food and Cracker\n"
                  "[5] Seasonings\n"
                  "[6] More info\n"
                  "[7] Back to cart\n"
                  "[x] Exit")


# Greet the user
line()
print(f"Good day,welcome to MSM"
      " online grocery \n"
      "Do you want to buy some products?\n"
      "[1] yes\n"
      "[0] no\n")

while True:
    line()
    answer = input("answer: ")
    line()
    try:
        if answer == '1':
            introduction()
            break
        elif answer == '0':
            print("Have a nice day!\n")
            break
        elif answer == 'x':
            print("Closing the system")
            break
        else:
            print("Invalid input\n"
                  "Please try again\n"
                  "Do you want to buy some products?\n"
                  "[1] Yes\n"
                  "[0] No\n"
                  "[x] Exit\n")
    except ValueError:
        print("Invalid input\n"
              "Please try again\n"
              "Do you want to buy some products?\n"
              "[1] Yes\n"
              "[0] No\n"
              "[x] Exit\n")

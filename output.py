import displaydatabase
import moreinfo
import selection
import checkout
import suggestion


def main():
    print("""Hello dear User....
          welcome to MSM Online grocery where??...
          
          you can buy your needs online, 
                we sell varieties of products such us
          
                beverage
                cleaners
                canned products
                junkfoods
                and seasonings
          
          does it fulfill your needs? if not.. why not try to write your suggestions and
          place it in our suggestion box...
          
          """)
    suggest = input('is there something you want to suggest(press 1|press any key to continue)?')
    if suggest == '1':
        suggestion.concern()
    answer = input("do you want to see our available products(yes/no)?  ")
    if answer.lower() == 'yes' or answer.lower() == 'y':
        list()
        shop()
    else:
        proceed()

def proceed():
    while True:
        get = input("""What would you like to do? 
                        [1] leave
                        [2] go to shop
                        answer: """)
        if get == '1':
            close()
            break
        elif get == '2':
            shop()
            break
        else:
            print("Invalid Input")
def shop():
    while True:
        get = input("""Do you want to buy some product(yes/no)?
                        [1] yes
                        [2] no
                        [3] your cart
                        [4] check out
                        """)
        if get.lower() == 'yes' or get.lower() == 'y' or get == '1':
            print(selection.cart_item)
            menu()
            break
        elif get == '3':
            print(goods())
            shop()
            break
        elif get == '4':
            amount = 0
            for price in selection.cart_price:
                amount += price
            checkout.customer(amount)
            close()
            break

        elif get.lower() == 'no' or get.lower() == 'n' or get == '2':
            close()
            break
        else:
            print("Invalid Input")


def menu():
    global ptype
    print("""Dear user... thank you for proceeding in our online grocery shop...
    here are the variety of product we sell...
    [1] beverage
    [2] cleaners
    [3] canned_dairies
    [4] junk_food_crackers
    [5] seasonings
    [6] more info
    [7] Cancel
    """)
    while True:
        type_of_product = int(input("What type of product you want to buy? "))
        if type_of_product == 1:
            ptype = 'beverage'
            break
        elif type_of_product == 2:
            ptype = 'cleaners'
            break
        elif type_of_product == 3:
            ptype = 'canned_dairies'
            break
        elif type_of_product == 4:
            ptype = 'junk_food_crackers'
            break
        elif type_of_product == 5:
            ptype = 'seasonings'
            break
        elif type_of_product == 6:
            moreinfo.more_info()
            break
        elif type_of_product == 7:
            close()
            break
        else:
            print("Invalid Input")
    displaydatabase.selected_type(ptype)
    shop()


def goods():
    count = 0
    output = ["ID  |        Product       |   Price", "--- | -------------------- | ----------"]
    for item in selection.cart_item:
        output.append(f"{count + 1: <3} | {item: <20} | {selection.cart_price[count]: <10}")
        count += 1
    return "\n".join(output)


def list():
    displaydatabase.display()


def close():
    print("""

            Thank you for using out system....

                ---------------------------------------------
                             Closing the system
                ---------------------------------------------""")

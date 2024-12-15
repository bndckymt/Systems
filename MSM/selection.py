import displaydatabase

cart_item = []
cart_price = []

def want(last):
    while True:
        get = int(input("Enter the ID of product you want to buy:"))
        if 0 < get <= last:
            item = displaydatabase.selected_item[get - 1]
            price = displaydatabase.selected_price[get - 1]
            cart_item.append(item)
            cart_price.append(price)
            displaydatabase.selected_item = []
            displaydatabase.selected_price = []
            break
        else:
            print("Product not found.. please try again")

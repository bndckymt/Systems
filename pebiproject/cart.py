import customer
items = []
prices = []

def buy(item, price):
    items.append(item)
    prices.append(price)

def cart():
    print('ID  |        Product       | Price')
    print('--- | -------------------- | ----------')
    count = 0
    for product in items:
        print(f"{count+1:<3} | {product:<20} | {prices[count]:<10}")
        count += 1

def checkout():
    i = 0
    amount = 0
    for price in prices:
        amount += int(price)
        i += 1

    print("you need to pay ", amount)

    customer.data(amount)

def remove():
    cart()
    if items != []:
        answer = int(input("Which item do you want to remove?"))
        items.pop(answer - 1)
        prices.pop(answer - 1)
    else:
        print("Your cart is empty")


import cart
import screenout
def close():
    print("Thank you for using our system...\n"
          "\n"
          "---------------------------------\n"
          "      closing the program\n"
          "---------------------------------")




def main():
    while True:
        get = int(input("""Would you like to buy more product?
            [1] yes
            [2] no
            [3] cart
            [4] checkout
            [5] remove
            [6] cancel
            """))

        if get == 1:
            screenout.product()

        elif get == 2:
            ans = int(input("Thank you for using our system:\n"
                            "[1] checkout\n"
                            "[2] close\n"))
            if ans == 1:
                cart.cart()
                cart.checkout()
                break
            elif ans == 2:
                close()
                break
            else:
                close()
                break

        elif get == 3:
            cart.cart()

        elif get == 4:
            cart.checkout()
            break


        elif get == 5:
            cart.remove()

        elif get == 6:
            close()
            break
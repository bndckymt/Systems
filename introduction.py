import sqlite3 as db

import screenout


def intro():
    print("Hello welcome to our online fashion shop")
    print("""Here are the type of products that we sell:
    [1] Clothes
    [2] Bags
    [3] Perfumes
    [4] ShoesorSandals
    [5] Jewelry
    [6] Cosmetics
    [7] HairTreatment
    """)


def proceed():

    while True:
        try:
            answer = input("press [1] if you want to proceed: ")
            if answer == '1':
                screenout.product()
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("invalid input")


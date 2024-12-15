import intro
import count
import candidate
import add
import delete


def line():
    print('-'*20)
    print("""
    
    
    """)
def close():
    print("----------closing the system---------")


def system():
    print("""Welcome Admin, what would you like to do?

    [1] count the number of votes
    [2] delete or eliminate a candidate
    [3] add a candidate
    [4] delete the data
    [5] cancel
    """)

    select = int(input("select 1-5: "))

    if select == 1:
        count.vote()
        line()

    elif select == 2:
        candidate.candidate()
        line()

    elif select == 3:
        add.candidate()
        line()
    elif select == 4:
        delete.table()
        line()

    elif select == 5:
        close()

    else:
        close()


while True:
    ans = input("Greetings\n"
                "-----logging in-----\n"
                "[1] User\n"
                "[2] Admin\n")

    if ans == '1':
        intro.intro()
        break
    elif ans == '2':
        get = input("Enter Password: ")
        if get == '12345':
            system()
        else:
            print("wrong password")
    else:
        print("Invalid Input")

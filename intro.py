import re
import database
import vote

def intro():
    print("Hello there... are here to place your vote? ")

    while True:
        answer = input("Do you want to vote(yes|no)? ").lower()
        if answer == 'yes' or answer == 'y':
            getdata()
            break
        elif answer == 'no' or answer == 'n':
            close()
            break
        else:
            print("Invalid Input")

def close():
    print("""Thank your for using the system

       -------------------------------
            closing the system
       -------------------------------
       """)


def getdata():
    print("Hello there... To proceed we need to gather your"
          " personal information to confirm if your eligible to cast a vote.... ")

    while True:
        fname = input("Firstname: ")
        if re.search(r'\d', fname):
            print("Invalid input: Firstname should not contain any digits. Please try again.")
        else:
            break

    while True:
        mname = input("Middle Name: ")
        if re.search(r'\d', mname):
            print("Invalid input: Midname should not contain any digits. Please try again.")
        else:
            break

    while True:
        lname = input("last Name: ")
        if re.search(r'\d', lname):
            print("Invalid input: Lastname should not contain any digits. Please try again.")
        else:
            break

    while True:
        gmail = input("Your gmail address: ")
        if "@" not in gmail:
            print("Invalid input: Gmail address must include '@'. Please try again.")
        else:
            break

    def get_valid_age():
        while True:
            age_input = input("Age: ").strip()
            if age_input == "":
                print("You must enter your age. Please try again.")
            elif age_input.isdigit():
                age = int(age_input)
                return age
            else:
                print("Invalid input: Age must be a number. Please try again.")

    age = get_valid_age()

    def get_valid_gender():
        while True:
            gender = input("Gender (male/m or female/f): ").strip().lower()
            if gender in ['male', 'm', 'female', 'f']:
                return gender
            else:
                print("Invalid input: Please enter 'male', 'm', 'female', or 'f'.")

    gender = get_valid_gender()
    fullname = fname + ' ' + mname + ' ' + lname
    database.save(fullname, age, gender, gmail)

    if age >= 18 and age < 110:
        print("You are now eligble to cast a vote")
        enter = input("press [1] if you want to proceed and cast a vote: ")
        if enter == '1':
            vote.cast()
    else:
        print("Invalid Input")

    print("""Thank you for voting
    
    Please wait for the result of your voting, will be posted soon
    """)


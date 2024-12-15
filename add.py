import sqlite3 as db

def candidate():
    on = db.connect('votedatabase.db')
    open = on.cursor()

    name = input("Enter the name of the candidate: ")

    while True:
        positions = input("""enter the position:"
                             "[1] PRESIDENT"
                             "[2] VICE_PRESIDENT"
                             "[3] SECRETARY""")
        if positions == '1':
            position = 'PRESIDENT'
            break
        elif positions == '2':
            position = 'VICE_PRESIDENT'
            break
        elif positions == '3':
            position = 'SECRETARY'
            break
        else:
            print("Invalid Input")

    if position == "PRESIDENT" or position == "VICE_PRESIDENT" or position == "SECRETARY":
        open.execute("INSERT INTO candidate (NAME, POSITION) VALUES (?, ?)", (name, position))
        print("New candidate was added to the list")
    else:
        print("sorry you've entered an invalid position")
    on.commit()
    open.close()
    on.close()
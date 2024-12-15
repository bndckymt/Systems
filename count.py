import sqlite3 as db


def baiting(name):
    open = db.connect('votedatabase.db')
    on = open.cursor()

    on.execute('SELECT COUNT(*) FROM vote WHERE PRESIDENT = ?',(name,))
    count = on.fetchone()[0]

    print(f"there are {count}  vote for {name}.")
    on.close()
    open.close()


def baiting2(name):
    open = db.connect('votedatabase.db')
    on = open.cursor()

    on.execute('SELECT COUNT(*) FROM vote WHERE VICE_PRESIDENT = ?', (name,))
    count = on.fetchone()[0]

    print(f"there are {count}  vote for {name}.")
    on.close()
    open.close()


def baiting3(name):
    open = db.connect('votedatabase.db')
    on = open.cursor()

    on.execute('SELECT COUNT(*) FROM vote WHERE SECRETARY = ?', (name,))
    count = on.fetchone()[0]

    print(f"there are {count}  vote for {name}.")
    on.close()
    open.close()

def vote():

    print("----------PRESIDENT-----------")
    baiting('Emjay Servan')
    baiting('June Garcia')
    baiting('Alexis Balmores')

    print("--------VICE PRESIDENT--------")
    baiting2('Rhengel Argal')
    baiting2('Heven Calica')
    baiting2("Justine Sauli")

    print("----------SECRETARY-----------")
    baiting3('Wendy Ortega')
    baiting3('June Garcia')
    baiting3('Gracia Balaoag')


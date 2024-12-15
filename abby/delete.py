import sqlite3 as A

def table():
    conn = A.connect('votedatabase.db')
    op = conn.cursor()

    choose = input("""What table would you like to clear?
    candidate
    login
    vote

    Please type exactly the name of the table you want to remove: """)

    op.execute(f"DROP TABLE IF EXISTS {choose}")
    conn.commit()
    op.close()
    conn.close()

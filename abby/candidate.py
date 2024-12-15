import sqlite3 as db


def candidate():
    conn = db.connect('votedatabase.db')
    cursor = conn.cursor()
    column_name = 'PRESIDENT'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    candidates_president = [row[0] for row in rows]

    column_name = 'VICE_PRESIDENT'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    candidates_vice_president = [row[0] for row in rows]

    column_name = 'SECRETARY'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    candidates_secretary = [row[0] for row in rows]
    cursor.close()
    conn.close()

    print("here are the list of candidates for president")
    for i in range(1,len(candidates_president) + 1):
        print(f"{i} {candidates_president[i-1]}")
    print("here are the list of candidates for president")
    for i in range(1, len(candidates_vice_president) + 1):
        print(f"{i} {candidates_vice_president[i - 1]}")
    print("here are the list of candidates for president")
    for i in range(1, len(candidates_secretary) + 1):
        print(f"{i} {candidates_secretary[i - 1]}")

    name = input('Who would you like to remove[enter his/her whole name]? ')
    select = int(input("what  his|her position? \n"
                       "[1] President\n"
                       "[2] Vice President\n"
                       "[3] Secretary\n"
                       "Answer: "))
    if select == 1:
        if any(name.upper() == candidate.upper() for candidate in candidates_president):
            candidates_president.remove(name)
            open = db.connect('votedatabase.db')
            cursor = open.cursor()
            cursor.execute("DELETE FROM candidate WHERE NAME = ?", (name,))
            open.commit()
            cursor.close()
            open.close()
        else:
            print("Name not found in candidate list")
    if select == 2:
        if any(name.upper() == candidate.upper() for candidate in candidates_vice_president):
            candidates_vice_president.remove(name)
            open = db.connect('votedatabase.db')
            cursor = open.cursor()
            cursor.execute("DELETE FROM candidate WHERE NAME = ?", (name,))
            open.commit()
            cursor.close()
            open.close()
        else:
            print("Name not found in candidate list")

    if select == 3:
        if any(name.upper() == candidate.upper() for candidate in candidates_secretary):
            candidates_secretary.remove(name)
            open = db.connect('votedatabase.db')
            cursor = open.cursor()
            cursor.execute("DELETE FROM candidate WHERE NAME = ?", (name,))
            open.commit()
            cursor.close()
            open.close()
        else:
            print("Name not found in candidate list")



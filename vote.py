import database
import sqlite3 as db


def name_candidates_president():
    conn = db.connect('votedatabase.db')
    cursor = conn.cursor()
    column_name = 'PRESIDENT'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    candidates_president = [row[0] for row in rows]

    cursor.close()
    conn.close()
    print("Candidates for President:")
    for i, candidate in enumerate(candidates_president, start=1):
        print(f"[{i}] {candidate}")

    # Function to display candidates for Vice President
def name_candidates_vice_president():
    conn = db.connect('votedatabase.db')
    cursor = conn.cursor()
    column_name = 'VICE_PRESIDENT'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    candidates_vice_president = [row[0] for row in rows]
    print("\nCandidates for Vice President:")
    for i, candidate in enumerate(candidates_vice_president, start=1):
        print(f"[{i}] {candidate}")

    # Function to display candidates for Secretary
def name_candidates_secretary():
    conn = db.connect('votedatabase.db')
    cursor = conn.cursor()
    column_name = 'SECRETARY'
    cursor.execute(f"SELECT NAME FROM candidate  WHERE POSITION = ?", (column_name,))
    rows = cursor.fetchall()
    candidates_secretary = [row[0] for row in rows]
    cursor.close()
    conn.close()
    print("\nCandidates for Secretary:")
    for i, candidate in enumerate(candidates_secretary, start=1):
        print(f"[{i}] {candidate}")



votes = {
        "president": [0, 0, 0],  # Emjay, June, Alexis
        "vice_president": [0, 0, 0],  # Rhengel, Ian, Justine
        "secretary": [0, 0, 0],  # Wendy, Heven, Gracia
    }

def cast():
    while True:
        name_candidates_president()
        try:
            vote_president = int(input("Enter the number of the candidate you would like to vote for (President): "))
            if 1 <= vote_president <= 3:
                votes["president"][vote_president - 1] += 1
                print(f"You voted for candidate {vote_president}!")
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Vote for Vice President
    while True:
        name_candidates_vice_president()
        try:
            vote_vice_president = int(
                input("Enter the number of the candidate you would like to vote for (Vice President): "))
            if 1 <= vote_vice_president <= 3:
                votes["vice_president"][vote_vice_president - 1] += 1
                print(f"You voted for candidate {vote_vice_president}!")
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Vote for Secretary
    while True:
        name_candidates_secretary()
        try:
            vote_secretary = int(input("Enter the number of the candidate you would like to vote for (Secretary): "))
            if 1 <= vote_secretary <= 3:
                votes["secretary"][vote_secretary - 1] += 1
                print(f"You voted for candidate {vote_secretary}!")
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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
    database.votes(candidates_president[vote_president - 1],
                   candidates_vice_president[vote_vice_president - 1],
                   candidates_secretary[vote_secretary - 1])


def results():
    print("\nElection Results:")
    print("\nTotal Votes for Presidential Candidates:")
    print(f"Emjay Servan: {votes['president'][0]}")
    print(f"June Garcia: {votes['president'][1]}")
    print(f"Alexis Balmores: {votes['president'][2]}")

    print("\nTotal Votes for Vice Presidential Candidates:")
    print(f"Rhengel Argal: {votes['vice_president'][0]}")
    print(f"Ian Quilala: {votes['vice_president'][1]}")
    print(f"Justine Sauli: {votes['vice_president'][2]}")

    print("\nTotal Votes for Secretary Candidates:")
    print(f"Wendy Ortega: {votes['secretary'][0]}")
    print(f"Heven Calica: {votes['secretary'][1]}")
    print(f"Gracia Balaoag: {votes['secretary'][2]}")
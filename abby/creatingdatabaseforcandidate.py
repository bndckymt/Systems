# import sqlite3 as database
#
# conn = database.connect('votedatabase.db')
# open = conn.cursor()
#
# # open.execute('DROP TABLE IF EXISTS candidate')
# # conn.commit()
#
# open.execute("""CREATE TABLE IF NOT EXISTS candidate(ID INTEGER PRIMARY KEY,
# POSITION TEXT,
# NAME TEXT)
# """)
#
# candidates_president = ["Emjay Servan", "June Garcia", "Alexis Balmores"]
# candidates_vice_president = ["Rhengel Argal", "Ian Quilala", "Justine Sauli"]
# candidates_secretary = ["Wendy Ortega", "Heven Calica", "Gracia Balaoag"]
# count = 0
# POSITION = 'SECRETARY'
# for candidate in candidates_president:
#     open.execute("INSERT INTO candidate( POSITION, NAME) VALUES(?, ?)", (POSITION, candidates_secretary[count]))
#     count += 1
#     conn.commit()
#
# open.close()
# conn.close()
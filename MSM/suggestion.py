import sqlite3 as db

def concern():
    conn = db.connect('MSMdatabase.db')
    on = conn.cursor()
    suggestion = input("what do you want to recommend? ")
    on.execute("""CREATE TABLE IF NOT EXISTS suggestion (Suggestion TEXT)""")
    on.execute("INSERT INTO suggestion(Suggestion) VALUES(?)", (suggestion,))
    conn.commit()
    on.close()
    conn.close()

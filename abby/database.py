import sqlite3 as sql


def save(name, age, gender, gmail):
    conn = sql.connect('votedatabase.db')
    open = conn.cursor()

    open.execute("""CREATE TABLE IF NOT EXISTS login(ID INTEGER PRIMARY KEY,
    NAME TEXT,
    AGE INTEGER,
    GENDER TEXT,
    GMAIL TEXT)
    """)
    open.execute("INSERT INTO login(NAME, AGE, GENDER, GMAIL) VALUES(?, ?, ?, ?)", (name, age, gender, gmail))
    conn.commit()
    open.close()
    conn.close()

def votes(president, vice_president, secretary):
    conn = sql.connect('votedatabase.db')
    open = conn.cursor()

    open.execute("""CREATE TABLE IF NOT EXISTS vote(ID INTEGER PRIMARY KEY,
        PRESIDENT TEXT,
        VICE_PRESIDENT TEXT,
        SECRETARY TEXT)
        """)
    open.execute("INSERT INTO vote(PRESIDENT, VICE_PRESIDENT, SECRETARY) VALUES(?, ?, ?)", (president, vice_president, secretary))
    conn.commit()
    open.close()
    conn.close()
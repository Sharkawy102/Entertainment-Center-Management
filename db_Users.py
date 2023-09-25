import sqlite3


def userData():
    con = sqlite3.Connection("user.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXIST users (
                userID INTEGER PRIMARY KEY INCREMENT,
                userName TEXT,
                password TEXT,
                shiftTimeStarts TEXT,
                shiftTimeEnds TEXT,
                
    )""")

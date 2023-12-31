import sqlite3


def units():
    con = sqlite3.Connection("units.db")
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS units (
                UnitId INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,
                UnitName TEXT UNIQUE,
                HourlyRate REAL DEFAULT '0',
                AvailabilityStatus BOOLEAN 
    )""")
    con.commit()
    con.close()


def addUnits(UnitName, HourlyRate, AvailabilityStatus=False):
    con = sqlite3.Connection("units.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO units (UnitName, HourlyRate, AvailabilityStatus) VALUES (?,?,?)""",
                (UnitName, HourlyRate, AvailabilityStatus))
    con.commit()
    con.close()


def viewUnits():
    con = sqlite3.Connection("units.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM units")
    unitsShow = cur.fetchall()
    con.commit()
    con.close()
    return unitsShow


def updateStatus(UnitName="", AvailabilityStatus=False):
    try:
        con = sqlite3.connect("units.db")
        cur = con.cursor()
        cur.execute("UPDATE units SET AvailabilityStatus = ? WHERE UnitName=?",
                    (AvailabilityStatus, UnitName))
        con.commit()
        print("Update successful")
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        con.close()

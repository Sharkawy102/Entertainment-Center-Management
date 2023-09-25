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


def addUnits(UnitName, HourlyRate, AvailabilityStatus):
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


def updateStatus(AvailabilityStatus=""):
    con = sqlite3.Connection("units.db")
    cur = con.cursor()
    cur.execute("UPDATE units SET AvailabilityStatus = ?",
                (AvailabilityStatus))
    con.commit()
    con.close()

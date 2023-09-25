import sqlite3


def reportData():
    con = sqlite3.Connection("Reports.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXIST reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                unit INTEGER,
                startTime TEXT,
                endTime TEXT,
                date TEXT,
                items array,
                totalAmount REAL,
                employeeID INTEGER
    )""")
    con.commit()
    con.close()


def addReport(unit, startTime, endTime, date, items, totalAmount, employeeID):
    con = sqlite3.Connection("Reports.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO reports (unit, startTime, endTime, date, items, totalAmount, employeeID) VALUES (?,?,?,?,?,?,?)", (unit, startTime, endTime, date, items, totalAmount, employeeID))
    con.commit()
    con.close()


def viewReports():
    con = sqlite3.Connection("Reports.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM reports")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

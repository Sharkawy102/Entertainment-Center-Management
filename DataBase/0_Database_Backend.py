import sqlite3


def studentDta():
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    # Use triple-quotes for multiline SQL statements
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            stdID TEXT,
            firstName TEXT,
            surName TEXT,
            BoD TEXT,
            Age TEXT,
            Gender TEXT,
            Address TEXT,
            Mobile TEXT
        )
    """)
    con.commit()
    con.close()


def addStdRec(stdID, firstName, surName, BoD, Age,  Gender, Address, Mobile):
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",
                (stdID, firstName, surName, BoD, Age, Gender, Address, Mobile))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    rows = cur.fetchall()
    con.commit()
    con.close()


def serchData(stdID="", firstName="", surName="", BoD="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE stdID=? OR firstName=? OR surName=? OR BoD=? OR Age=?  OR Gender=? OR Address=? OR Mobile=? ",
                (stdID, firstName, surName, BoD, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows


def ubdateData(id, stdID="", firstName="", surName="", BoD="", Age="",  Gender="", Address="", Mobile=""):
    con = sqlite3.Connection("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET stdID=? OR firstName=? OR surName=? OR BoD=? OR Age=? OR text=? OR Gender=? OR Address=? OR Mobile=? ",
                (stdID, firstName, surName, BoD, Age,  Gender, Address, Mobile, id))
    rows = cur.fetchall()
    con.commit()
    con.close()

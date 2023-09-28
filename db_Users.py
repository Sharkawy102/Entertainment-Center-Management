import sqlite3


def userData():
    con = sqlite3.Connection("user.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                userID INTEGER PRIMARY KEY AUTOINCREMENT,
                userName TEXT,
                password TEXT,
                role TEXT REQUIRED
                
    )""")
    con.commit()
    con.close()


def addUser(userName, password, role):
    con = sqlite3.Connection("user.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (userName, password, role ) VALUES (?, ?, ?)", (userName, password, role))
    con.commit()
    con.close()


def viewUsers(role):
    con = sqlite3.Connection("user.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE role=?", (role,))
    users = cur.fetchall()
    con.commit()
    con.close()
    return users


def login(username, password, role):
    # Check if the entered username and password match a record for the given role
    users = viewUsers(role)
    for user in users:
        if user[1] == username and user[2] == password and user[3] == "Admin":
            role = "Admin"
            return role
            # Login successful
        elif user[1] == username and user[2] == password and user[3] == "Employee":
            role = "Employee"
            return role  # Login Successful
        else:
            # Username or Password is incorrect
            return print("Invalid Username or Password")
    return False  # Login failed


# userData()
# addUser('admin1@entertainment.com', '1234567890', "Admin")
# addUser('Employe1@entertainment.com', '1234567890', "Employee")
# login("admin1@entertainment.com", "1234567890", "Admin")
# login("admin1@entertainment.com", "1234567890", "Employee")
# login("Employe1@entertainment.com", "1234567890", "Employee")
print(viewUsers("Admin"))
# print(viewUsers("Employee"))

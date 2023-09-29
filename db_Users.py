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


def viewUsers():
    con = sqlite3.Connection("user.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    con.commit()
    con.close()
    return users


def login(username, password):
    # Check if the entered username and password match a record for the given role
    users = viewUsers()
    for user in users:
        if user[1] == username and user[2] == password:
            # role = "Admin"
            role = user[3]
            return role
        #     # Login successful
        # elif user[1] == username and user[2] == passwor:
        #     role = "Employee"
        #     return role  # Login Successful
        else:
            # Username or Password is incorrect
            return print("Invalid Username or Password")
    return False  # Login failed


resut = login("Mohamed11@entertainment.com", "0123456789")
print(resut)
userData()
# addUser("Admin@gmail.com", "aaa12345", "Employer")
# addUser("Employe@gmail.com", "aaa12345", "Employee")
print(viewUsers())

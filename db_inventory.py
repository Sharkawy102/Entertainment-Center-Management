import sqlite3


def itemsData():
    con = sqlite3.Connection("items.db")
    cur = con.cursor()
    # Use triple-quotes for multiline SQL statements
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER,
                price REAL DEFAULT 0
        )
    """)
    con.commit()
    con.close()


def addItem(name, category, quantity, price):
    con = sqlite3.Connection("items.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO items (name, category, quantity, price ) VALUES (?, ? , ? , ?)", (name, category, quantity, price))
    con.commit()
    con.close()


def view_items(category):
    con = sqlite3.Connection("items.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM items WHERE category = ?", (category,))
    items = cur.fetchall()
    con.commit()
    con.close()
    return items


def updateData(name="", new_quantity=None, new_price=None):
    con = sqlite3.Connection("items.db")
    cur = con.cursor()
    if new_quantity is not None:
        cur.execute("UPDATE items SET quantity=? WHERE name=?",
                    (new_quantity, name))
    if new_price is not None:
        cur.execute("UPDATE items SET price=? WHERE name=?", (new_price, name))

    con.commit()
    con.close()

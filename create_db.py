import sqlite3

def create_db():
    # Connect to the SQLite database, if it doesn't exist, it will be created
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()

    # Create employee table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            pass TEXT,
            utype TEXT,
            address TEXT,
            salary TEXT
        )
    """)
    
    # Create supplier table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier (
            invoice INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            desc TEXT
        )
    """)
    
    # Create category table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    
    # Create product table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product (
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            supplier TEXT,
            name TEXT,
            price REAL,
            qty INTEGER,
            status TEXT
        )
    """)
    
    # Create product_transaction table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product_transaction (
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            type TEXT,
            qty INTEGER,
            date TEXT,
            description TEXT,
            FOREIGN KEY (product_id) REFERENCES product(pid)
        )
    """)

    # Commit the changes and close the connection
    con.commit()
    con.close()

# Call the function to create the database and tables
create_db()

import sqlite3

# database setup
DB_NAME = "password_manager.db"

#connecting to the database
def connect():
    return sqlite3.connect(DB_NAME)

#table creation
def create_tables():
    print(">>> create_tables() called")
    conn = connect()
    cursor = conn.cursor()

#creating tables 
#Stores one/more user accounts, each protected by a master password
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            master_password_hash TEXT NOT NULL,
            salt BLOB NOT NULL
        )
    """)
#Stores encrypted login credentials for various services (e.g., "Gmail", "Netflix")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password BLOB NOT NULL
        )
    """)

    conn.commit() #save changes
    conn.close()#closing DBconnection

    print(">>> database initialized") 

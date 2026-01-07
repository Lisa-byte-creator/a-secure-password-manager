from app.database import connect
from app.crypto import encrypt_password, decrypt_password


def add_password(service: str, username: str, password: str, master_password: str):

    #encrypting the plain text password
    encrypted = encrypt_password(password, master_password)

    #connecting to the database and inserting the encrypted credential
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO passwords (service, username, encrypted_password) VALUES (?, ?, ?)",
        (service, username, encrypted)
    )

    #saving the changes and closing the connection
    conn.commit()
    conn.close()

#retrieving and decrypting all saved passwords using the master password
def get_passwords(master_password: str):

    #connecting to the database and fetching all encrypted password records
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT service, username, encrypted_password FROM passwords")
    rows = cursor.fetchall()
    conn.close()

    #decrypting the passwords using master password
    results = []
    for service, username, encrypted in rows:
        decrypted = decrypt_password(encrypted, master_password)
        results.append((service, username, decrypted))

    #returns the list of service, username and plaintext password
    return results

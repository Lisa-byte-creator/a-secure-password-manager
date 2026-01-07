import hashlib
import os
import sqlite3
from app.database import connect


ITERATIONS = 100_000


def hash_master_password(password: str):
    """
    Hashes the master password using PBKDF2 with SHA-256.
    Returns (hash, salt).
    """
    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERATIONS
    )

    return password_hash, salt


def save_master_password(password: str):
    """
    Saves the hashed master password and salt to the database.
    Only one master password is allowed.
    """
    password_hash, salt = hash_master_password(password)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")  # ensure single master user

    cursor.execute(
        "INSERT INTO users (master_password_hash, salt) VALUES (?, ?)",
        (password_hash, salt)
    )

    conn.commit()
    conn.close()


def verify_master_password(password: str) -> bool:
    """
    Verifies a provided password against the stored hash.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT master_password_hash, salt FROM users LIMIT 1"
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return False

    stored_hash, salt = row

    check_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERATIONS
    )

    return check_hash == stored_hash

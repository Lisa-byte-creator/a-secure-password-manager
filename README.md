A Local Password Manager (Python)

This is a safe, local, commandline Password Manager built with Python showing basic security concepts which are encryption, hashing passwords and SQLite data storage.
The project was developed as a portfolio application to show real world knowledge in secure software design, cryptography and authentication.

FEATURES

Single master password authentication

Secure hashing of the master password using PBKDF2 (SHA-256)

Encryption of stored service passwords using symmetric encryption (Fernet)

Local data persistence with SQLite

Passwords are never stored in plaintext

Simple and intuitive command-line interface

Planned security enhancements

Password strength validation

Account lockout after multiple failed login attempts

TECH STACK

Python 3

SQLite3

cryptography (Fernet)

hashlib (PBKDF2-HMAC-SHA256)

os (secure salt generation)

SECURITY DESIGN OVERVIEW 

Master Password Protection

The master password is never stored in plaintext

It is hashed using PBKDF2-HMAC-SHA256 with:

A unique random salt

100,000 iterations

Only the hash and salt are stored in the database

Password Encryption

Service passwords are encrypted using Fernet symmetric encryption

An encryption key is derived from the master password

Encrypted passwords are stored in SQLite and decrypted only after successful authentication

HOW TO RUN THE PROJECT

Prerequisites

Python 3 installed

pip package manager

Setup Instructions

Clone the repository

git clone <repository-url>
cd password-manager


(Optional but recommended) Create a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install cryptography


Run the application

python main.py


Choose to:

Set up a master password (first run)

Log in and manage stored passwords

SECURITY DISCLAIMER

This application is intended for educational and portfolio purposes only.

While it applies standard security practices such as hashing and encryption, it is not intended for production use without additional protections such as:

Stronger key derivation (e.g., Argon2)

Persistent account lockout handling

Secure memory handling

Tamper detection

WHAT THIS PROJECT DEMONSTRATES

Understanding of hashing vs encryption

Secure password storage principles

Practical use of cryptographic libraries

Clean separation of concerns (auth, crypto, database, logic)

Real-world security thinking at a junior developer level

AUTHOR:

Lisa Elsie M
Aspiring Software Developer
Focused on secure systems and practical problem-solving.
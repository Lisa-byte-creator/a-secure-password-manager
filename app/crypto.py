import base64
import hashlib
from cryptography.fernet import Fernet


def derive_key(master_password: str) -> bytes:
    """
    Derives a 32-byte encryption key from the master password using SHA-256.
    The key is then encoded in URL-safe base64 format to be compatible with Fernet.
    """
    # Hash the master password using SHA-256 to get a 32-byte key
    key = hashlib.sha256(master_password.encode()).digest()
    # Encode the key in base64 (required by Fernet)
    return base64.urlsafe_b64encode(key)


def encrypt_password(password: str, master_password: str) -> bytes:
    """
    Encryptings a plaintext password using Fernet symmetric encryption.
    The encryption key is derived from the master password.
    Returns the encrypted password as bytes.
    """
    # Derive the encryption key from the master password
    key = derive_key(master_password)
    # Creating a Fernet instance with the derived key
    fernet = Fernet(key)
    # Encrypting the password 
    return fernet.encrypt(password.encode())


def decrypt_password(encrypted_password: bytes, master_password: str) -> str:
    """
    Decrypting an encrypted password using the master password then
    returns the original plaintext password as a string.
    """
    # Derive the same encryption key used during encryption
    key = derive_key(master_password)
    # Create a Fernet instance with the derived key
    fernet = Fernet(key)
    # Decrypt the password and convert it back to a string
    return fernet.decrypt(encrypted_password).decode()
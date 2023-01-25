from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def encrypt(message, secret_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(secret_key))
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()

def decrypt(encrypted_message, secret_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(secret_key))
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message.encode())
    return decrypted.decode()

salt = os.urandom(16)
secret_key = b'annaUniversity'
original_string = "www.annauniv.edu"
encrypted_string = encrypt(original_string, secret_key, salt)
decrypted_string = decrypt(encrypted_string, secret_key, salt)

print("URL Encryption Using AES Algorithm\n------------")
print("Original URL: ", original_string)
print("Encrypted URL: ", encrypted_string)
print("Decrypted URL: ", decrypted_string)

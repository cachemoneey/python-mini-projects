# pip/pip3 install cryptography

from cryptography.fernet import Fernet

def encrypt_password():
    password = input("Enter your password: ")
    password_bytes = password.encode()
    
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    encrypted_password = cipher_suite.encrypt(password_bytes)
    print("Encrypted password is: ", encrypted_password.decode())
    
encrypt_password()
# pip/pip3 install cryptography
from cryptography.fernet import Fernet
import os

def encrypt_file():
    path = "C:\\Users\\azizurrohman\\Desktop" # location of the file you want to encrypt
    os.chdir(path)
    password = input("Enter your password: ")
    password = password.encode()
    key = Fernet.generate_key()
    file_name = input("Enter full file name: ") # choose the file you want to encrypt
    
    with open(file_name, "rb") as file:
        encrypted_content = Fernet(key).encrypt(file.read())
        
    with open("encrypted_" + file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_content)
        
    print("File has been encrypted.")
    
encrypt_file() 
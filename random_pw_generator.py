import random
import time

new_password = []

def generate_password():
    ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lcase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@£$%^&*()/?."
    
    pass_string = ucase + lcase + numbers + symbols
    length_pass = int(input("Enter password length: "))
    password = "".join(random.sample(pass_string, length_pass))
    print("Generated password is: ", password)
    
generate_password()

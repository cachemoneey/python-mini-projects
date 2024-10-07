import os
import time
import re

def check_email():
    entry = input("Enter your email: ")
    # if the input does not have @ or .
    if not (re.search(r"@", entry) and re.search(r"\.", entry)):
        print("This email is not valid: ", entry)
    else:
        print("Valid entry.")
        
check_email()
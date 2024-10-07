import re
import time

# if characters are not present in password, do not save it. Get the length of the password

new_password = []

def create_password():
    print("Must contain number + underscore + capital ")
    pw = input("Password: ")
    if re.search(f"\d", pw) and re.search(F"_", pw) and re.search(f"[A-Z]", pw):
        print("Password is valid!")
        print("Updating...")
        new_password.append(pw)
        print("Updated: ", new_password)
        password_length()
    else:
        print("You are missing some necessary characters, please try again.")
        create_password()
        
def password_length():
    print("Password length is: ")
    time.sleep(1)
    print(len(new_password[0]))
    
create_password()
user = "Mo"
password = "123abc"

def login():
    print("Enter your username and password")
    entry1 = input("Username: ")
    entry2 = input("Password: ")
    if entry1 == user and entry2 == password:
        print("Access granted.")
        logged_in()
    else:
        print("Incorrect login details.")

def logged_in():
    print("Login successful!")
    quit()
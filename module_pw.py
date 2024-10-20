import getpass

passwords = ["abc123", "def456", "xyz789"]

def enter_password():
    entry = getpass.getpass(prompt="Enter password: ")
    if entry in passwords:
        print("Correct password")
    else:
        print("Incorrect password")
    
enter_password()
    
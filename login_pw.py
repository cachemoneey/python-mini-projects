password = "abc123"
message = []

def enter_password():
    entry = input("Enter password: ")
    if entry == password:
        print("Access granted!")
        check_msg_log()
    elif entry != password:
        print("Access denied. Incorrect password.")
        message.append(entry)
        enter_password()
    
def check_msg_log():
    entry2 = input("Check Logs, Y or N? ")
    if entry2.lower() == "y":
       if(len(message)) > 0:
           print("Login attempts: ", message)
    elif entry2.lower() == "n":
        print("Will quit the program")
        quit()
        
enter_password()
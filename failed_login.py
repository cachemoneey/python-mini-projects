import getpass

user = "admin"
password = "1234"

def login():
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        username = input("Enter username: ")
        pw = getpass.getpass(prompt="Enter password: ")
        if username == user and pw == password:
            print("Login successful.")
            break
        else:
            attempts = attempts + 1
            print("Login unsuccessful.", attempts - max_attempts, "attempts made.")
            if attempts == max_attempts:
                print("Message sent.")
                send_message()
            
def send_message():
   with open("Failed login.txt","w") as file_object:
       file_object.write("Someone has tried to login to your account.")

login()                
        
import time 
# Arrays in Python are known as lists
names = []
addresses = []
jobs = []

def welcome_message():
    print("Enter details into the database.")
    enter_name()

def enter_name():
    entry1 = input("Enter name: ")
    names.append(entry1)
    enter_addresses()
    
def enter_addresses():
    entry2 = input("Enter address: ")
    addresses.append(entry2)
    enter_job()
    
def enter_job():
    entry3 = input("Enter job: ")
    jobs.append(entry3)
    show_details()
    
def show_details():
    print("Searching wait...")
    time.sleep(1)
    print(names)
    print(addresses)
    print(jobs)
    clear_db()
    
def clear_db():
    print("Delete details?")
    answer = input("yes or no")
    if answer.lower() == ("yes" or "y"):
        names.clear()
        addresses.clear()
        jobs.clear()
        print("Deleted all details", names, addresses, jobs)
    else:
         print("You chose not to delete your info.")
         quit()
         
welcome_message()
            
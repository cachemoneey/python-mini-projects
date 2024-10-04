people = {"Aziz": "joiner", "Bob": "builder"}

def intro():
    print("Welcome to the database\n")
    print("To get access enter your password.")
    enter_password()
    
def enter_password():
    password = "123abc"
    entry1 = input("Enter your password")
    if (len(entry1)< 3) and (entry1!= password):
        print("Access denied!")
    else:
        print("Access granted!")
        data_base()

def data_base():
    x = int(input("Clear(1), Update(2), Print(3)"))
    if x == 1:
        people.clear()
        print(people)
        print("Database cleared")
    elif x == 2:
        update_dictionary()
        print(people)
    elif x == 3:
        print(people)

def update_dictionary():
    for i in range(3):
        name = input("Enter name: ")
        job = input("Enter job: ")
        people[name] = job
        print(people)
        
intro()
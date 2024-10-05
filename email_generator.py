import random

def generate_random_email():
    f_name = ["lionel", "cristiano", "wayne", "neymar", "andres"]
    l_name = ["messi", "ronaldo", "rooney", "junior", "iniesta"]
    
    rand_num = random.randint(20, 99) # Selects a random integer  between 20 - 99
    x = random.choice(f_name) # Selects a random choice from list 
    y = random.choice(l_name) 
    rand_email = f"{x}{y}{rand_num}@gmail.com"
    print(rand_email)
    another_email()

def another_email():
    print("Print more?")
    entry = input("Y or N? ")
    if entry.lower() == "y":
        generate_random_email()
    else:
        quit()
        
generate_random_email()
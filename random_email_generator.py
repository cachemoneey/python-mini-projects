import random

def generate_random_email():
    rand_num = random.randint(1000, 9999)
    rand_email = "mo{}@gmail.com".format(rand_num)
    print(rand_email)
    print("Generater another email?")
    entry = input(">> ")
    if entry.lower() == "y":
        generate_random_email()
    else:
        print("You chose to exit.")
        quit()
        
generate_random_email()
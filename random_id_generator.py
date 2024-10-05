import random
import time

new_id = []

def intro():
    print("Generate ID")
    generate_name()
    
def generate_name():
    names = ["lionel", "cristiano", "wayne", "andres"]
    x = random.choice(names) # Selects random choice string from list
    print("Generating random name...")
    time.sleep(1)
    print(x)
    new_id.append(x)
    surname()
    
def surname():
    surnames = ["messi", "ronaldo", "rooney", "iniesta"]
    x = random.choice(surnames) # Selects random choice string from list
    print("Generatin random surnames...")
    time.sleep(1)
    print(x)
    new_id.append(x)
    country()
    
def country():
    countries = ["UK", "USA", "UAE", "Spain"]
    x = random.choice(countries)
    print("Generating random country...")
    time.sleep(1)
    print(x)
    new_id.append(x)
    my_new_id()
    
def my_new_id():
    print("Your new id is:")
    print(new_id)
    
intro()
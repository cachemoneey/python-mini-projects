import time

def hello_message():
    print("Welcome to my Pizza restaurant")
    print("We are here to take your order")
    pizza_topping()

def pizza_topping():
    toppings = ["mushrooms", "onions", "anchovies"]
    request = input("Please enter a topping: ")
    if request in toppings:
        print(request, "Are available")
        soft_drinks()
    else:
        print("Processing...")
        time.sleep(1)
        print(request, "Sorry, not available.")
        quit()
        
def soft_drinks():
    print("Please order your drinks")
    drinks = ["cola", "juice", "coffee"]
    request = input("Please enter your drink: ")
    if request in drinks:
        print(request, "is available")
        thank_customer()
    else:
        print("Processing...")
        time.sleep(2)
        print(request, "is not currently available here")
        
def thank_customer():
    print("Enjoy your meal!")
    
hello_message()

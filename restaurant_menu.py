import time


def hello_message():
    print("Welcome to my pizza restaurant!")
    print("We are here to take your order.")
    pizza_toppings()
    
def pizza_toppings():
    toppings = ["onions", "chillis", "sweetcorn"]
    request = input("Please enter a topping: ")
    if request in toppings:
        print(request, "Are available.")
        soft_drinks()
    else:
        print("Processing your order...")
        time.sleep(1)
        print("Sorry, " + request + " is unavailable.")
        quit()
        
def soft_drinks():
    print("Please order your drink.")
    drinks = ["water", "juice", "cola"]
    request = input("Please enter your drink: ")
    if request in drinks:
        print(request, "is available.")
        thank_customer()
    else:
        print("Processing...")
        time.sleep(2)
        print("Sorry, " + request + " is unavailable.")
        
def thank_customer():
    print("Thank you for your order! Enjoy your meal!")
    

hello_message()
   
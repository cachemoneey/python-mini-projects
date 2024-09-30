class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        return f"Thank you, {self.age} year old, {self.name.title()}"
    
class Bank(User):
    total_deposits = 0
    total_withdraws = 0
    
    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
        
    def show_info(self):
        return f"{self.name} has a remaining balance of: £{round(self.balance, 2)}"
    
    def deposit(self):
       dp = float(input(f"{self.name.title()}, how much would you like to deposit?"))
       print("Thank you for depositing!")
       self.balance += dp
       self.total_deposits += 1
       return f"Your balance is: {round(self.balance, 2)}"
   
    def withdraws(self):
       wd = float(input(f"{self.name.title()}, how much would you like to withdraw?"))
       if self.balance < wd:
           return "You cannot withdraw that amount."
       else:
           print("Thank you for withdrawing.")
           self.balance -= wd
           self.total_withdraws += 1
           return f"Your balance is now: {round(self.balance, 2)}"
           
def options(user_two):
    print("Thank you for creating your bank account.")
    print("Here are a list of options, please choose the number you want.")
    while True:
        option_choice = int(input("1) See balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
        if option_choice == 1:
            print(user_one_bank.show_info())
            if option_choice == 1 and user_two != None:
                print(user_two_bank.show_info())
        elif option_choice == 2:
            print(user_one_bank.withdraws())
            if option_choice == 2 and user_two != None:
                wd = input(f"{user_two.name} would you like to withdraw? Yes or No: ")
                if wd.lower() == "yes":
                    print(user_two_bank.withdraws())
        elif option_choice == 3:
            print(user_one_bank.deposit())
            if option_choice == 3 and user_two != None:
                dep = input(f"{user_two.name} would you like to deposit? Yes or No: ")
                if dep.lower() == "yes":
                    print(user_two_bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_withdraws} withdraws.")
            if option_choice == 4 and user_two != None:
                print(f"There have been {user_two_bank.total_withdraws} withdraws.")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_deposits} deposits.")
            if option_choice == 5 and user_two != None:
                print(f"There have been {user_two_bank.total_deposits} deposits.")
        elif option_choice == 6:
            print("Thank you for using Py Bank")
            return False
            break
        else:
            print("Please choose a number from 1-6.")
            
def bank_creation(name):
    balance = float(input(f"{name.title()}, how much money do you have? "))
    return balance

while True:
    print("Welcome to Py Bank")
    name = input("Enter your name")
    age = int(input("Enter your age"))
    user_one = User(name, age)
    user_two = None
    new_user = input("Would you like to register a new person? Type 'No' to create your bank")
    if new_user.lower() == 'yes':
        name = input("Enter the second person's name: ")
        age = int(input("Enter the second person's age: "))
        user_two = User(name, age)
        print("Thank you for registering 2 people. Please create your bank account. ")
        user_one_balance = bank_creation(user_one.name)
        user_two_balance = bank_creation(user_two.name)
        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
        user_two_bank = Bank(user_two.name, user_two.age, user_two_balance)
        
        flag = options(user_two)
        if flag == False:
            break
    else:
        user_one_balance = bank_creation(user_one.name)
        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
        
        flag = options(user_two)
        if flag == False:
            break
        
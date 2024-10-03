import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def numbers_exit():
    for number in numbers:
        print(number)
    if number == "7":
        print("Number 7 reached, will exit loop now.")
    end_of_loop()
    
def end_of_loop():
    print("Waiting...")
    time.sleep(1)
    print("You reached number 8.")
    end_program()
    
def end_program():
    time.sleep(1)
    print("Program is shutting down.")
    quit()
    
numbers_exit()
print("Welcome to the Guessing Game!\n")
print("------------------------------")
print("You are in our Saturday Night Gameshow!")
print("------------------------------")
print("\nAnswer correctly to win!")

def first_question():
    entry1 = input("Only one of these is correct. What is the capital of Mexico, Guadalajara or Mexico City?")
    if entry1.lower() == "mexico city":
        print("You succeeded! Next question...")
        second_question()
    elif entry1.lower() == "guadalajara":
        print("You lose! Goodbye!")
        quit()
    else: 
        print("Answer not recognised. Try again.")

def second_question():
    entry2 = input("Only one of these is correct. Which pole do polar bears live? North or South?")
    if entry2.lower() == "north":
        print("Correct! Next question...")
        third_question()
    elif entry2.lower() == "south":
        print("You lose! Goodbye!")
        quit()
    else: 
        print("Answer not recognised. Try again.")

def third_question():
    entry3 = input("Only one answer is correct. From which country had the first astronaut to go into space? USA or the USSR?")
    if entry3.lower() == "ussr":
        print("Correct answer! On to the next question...")
        fourth_question()
    elif entry3 == "usa":
        print("Unlucky! That is incorrect.")
        quit()
    else:
        print("We need a valid answer.")

def fourth_question():
    entry4 = input("Only one answer is correct. What year was Google founded? 1998 or 1999?")
    if entry4 == "1998":
        print("Correct answer!")
        winner()
    elif entry4 == "1999":
        print("Unlucky! That is incorrect.")
        quit()
    else:
        print("We need a valid answer.")

def winner():
    x = "Congrats you have won the main prize!" * 7
    print(x.upper())

first_question()

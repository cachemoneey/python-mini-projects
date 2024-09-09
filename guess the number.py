target_number: int = 7

guess = int(input("Guess the number (1-10): "))
if guess == target_number:
    print("Congratulations! You guessed the correct number.")
elif guess < target_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again. ")


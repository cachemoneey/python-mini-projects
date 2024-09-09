import random


def computer_guess(x):  # computer guesses your number
    low = 1
    high = x
    feedback = ""
    while feedback != "c":  # "c" is your correct number
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low = high
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Congratulations! You got it right! It was {guess}")


computer_guess(10)

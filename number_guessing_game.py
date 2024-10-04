import random

number_to_guess = random.randint(1, 100)
# Loop
while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))

        if guess < number_to_guess:
            print('Too low.')
        elif guess > number_to_guess:
            print('Too high.')
        else:
            print('You guessed the number!')
    except ValueError:
        print('Please enter a valid number.')


# Generate random number
# ask user to make a guess
# if not a valid number
#   print an error
# if number < guess
#   print too low
# if number > guess
#   print too high
# else
#   print well done
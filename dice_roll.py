import random

while True:
    choice = input('Roll the dice (y/n)?: ')
    if choice.lower() == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice.')

    # Ask user to roll the dice
    # if user enters y
    #   generate 2 ranmdom numbers
    #   print them
    # if user enters n
    #   print msg
    #   terminate
    # else
    #   print invalid choice



from random import randint
import turtle

print("---Guess the number and win a mystery prize!---")

def lucky_number():
    number = randint(1, 3)
    guess = int(input("Pick a number between 1 - 3 "))
    if number != guess:
        print("Incorrect! You guessed wrong!")
        print("The number was " + number)
        fake_prize()
    elif number == guess:
        print("you guessed correctly!")
        prize()
     
def fake_prize():
    print("You get a pat on the back!" * 5)
    lucky_number()
    
def prize():
    t = turtle.Pen()
    t.forward(100)
    t.left(78)
    t.right(45)
    t.forward(66)
    t.left(78)
    
lucky_number()
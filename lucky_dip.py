import random 
lucky_names = []
winner_name = []
winner_prizes = []

def intro():
    print("Enter a name into the lucky dip!")
    entry = input("Enter a name: ")
    if (len(lucky_names)) >= 5:
        print("List is full.")
        lucky_names_winner()
    else:
        lucky_names.append(entry)
        intro()
        
def lucky_names_winner():
    winner = random.choice(lucky_names)
    print("The lucky winner is: ", winner)
    print("\nHello {} claim your prize money!".format(winner))
    winner_name.append(winner)
    claim =  input("Y or N?")
    if claim.lower() != "y":
        print("Bye!")
    else:
        prize_money()
        
def prize_money():
    prize_money = ["50 pounds", "100", "a slap", "1 million pounds", "a tenner"]
    cash_prize = random.choice(prize_money)
    print("You have won: ", cash_prize)
    winner_prizes.append(cash_prize)
    
intro()
        
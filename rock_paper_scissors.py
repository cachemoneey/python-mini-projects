import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'


    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    # do not need if statement when top 2 occurs bottom will happen
    # AKA if is_win(opponent, user)
    return 'You lost!'



def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
            player == 's' and opponent == 'p'):
        return True


print(play())


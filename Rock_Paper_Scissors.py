import random
import re

def play():
    user = input("Whats you choice? 'r' for Rock, 's' for Scissors, 'p' for Paper\n")
    computer = random.choice(['r','s','p'])
# r > s , s > p, p > r

    if user == computer:
        return "It's Tie"
        

    if is_win(user, computer):
        return "You Won!!!!!"

    return "You Loast...:("


def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or \
    (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

print(play())


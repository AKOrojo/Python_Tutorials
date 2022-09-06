import random
from unicodedata import name
from art import logo, vs
from game_data import data
import os


def random_guess():
    Choice = random.choice(data)
    return Choice


def compare(a, b):
    pick = input("Who has more followers? Type 'A' or 'B': ")
    if pick == 'A' and a['follower_count'] > b['follower_count']:
        return 1
    elif pick == 'B' and b['follower_count'] > a['follower_count']:
        return 2
    else:
        return 0


def game():
    print(logo)
    score = 0
    game_Over = False
    choice1 = random_guess()
    while game_Over != True:
        print(f"Your Current Score {score}")
        print(
            f"Compare A: {choice1['name']}, {choice1['description']}, {choice1['country']}.")
        print(vs)
        choice2 = random_guess()
        if choice2 == choice1:
            choice2 = random_guess()
        print(
            f"Against B: {choice2['name']}, {choice2['description']}, {choice2['country']}.")
        comp = compare(choice1, choice2)
        if comp == 1:
            score += 1
        elif comp == 2:
            score += 1
            choice1 = choice2
        else:
            game_Over = True
            print(f"You lose, Your Score is {score}")
        os.system("CLS")


game()

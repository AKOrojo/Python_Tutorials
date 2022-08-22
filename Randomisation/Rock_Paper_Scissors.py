import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# create a list of each option rock paper or scissors
# randomly select an index value(each represents an option)
# have that be the computers selection
# build this out make it work then declare a winner
choice = [rock, paper, scissors]

player_choice = int(input("Enter 0 FOR ROCK, 1 FOR PAPER, 2 FOR SCISSORS "))

if (player_choice >= 3 or player_choice < 0):
    print("wrong values")
else:
    computer_choice = random.randint(0, 2)

    print(choice[player_choice])
    print(choice[computer_choice])

    if player_choice == computer_choice:
        print("draw")
    elif player_choice == 0 & computer_choice == 1:
        print("Computer Wins")
    elif player_choice == 0 & computer_choice == 2:
        print("You Win")
    elif player_choice == 1 & computer_choice == 0:
        print("You Win")
    elif player_choice == 1 & computer_choice == 2:
        print("Computer Wins")
    elif player_choice == 2 & computer_choice == 1:
        print("You Win")
    elif player_choice == 2 & computer_choice == 0:
        print("Computer Wins")

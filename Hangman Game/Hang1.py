import random

word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter? ").lower()

chosen_word_split = list(chosen_word)
print(chosen_word_split)

for letter in chosen_word_split:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

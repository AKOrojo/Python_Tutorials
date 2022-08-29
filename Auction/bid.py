import os
from art import logo

print(logo)

bids = {}


def collect_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    os.system('cls')


bid_completed = False

while not bid_completed:
    collect_bid()
    cont = input("Is there another bid? (Y)es or (N)o ").lower()
    if cont == "n":
        bid_completed = True

# taking list of car values in v
v = list(bids.values())

# taking list of car keys in v
k = list(bids.keys())

print(f"Maximum value: {k[v.index(max(v))]} ${max(v)}")

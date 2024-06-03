#!/usr/bin/env python
# coding: utf-8

# In[1]:


from replit import clear
from auction_art import gavel_art
print(gavel_art)
print("\n Welcome to the secret auction program. ")

def find_winner(bids):
    winner = ""
    highest_bid = 0
    for person in auction :
        each_bid = auction[person]
        if each_bid > highest_bid :
            highest_bid = each_bid
            winner = person
    print(f"The winner is {winner} with a bid of {highest_bid}")
    
auction = {}
game_ends = False
while not game_ends :
    name = input("What is your name?\n")
    bid = int(input("What\'s your bid?"))
    auction[name] = bid
    other_bidders = input("Are there anu other bidders? Type \'Yes\' or \'no\'.").lower()
    if other_bidders == 'yes' :
        clear()
    elif other_bidders == 'no' :
        game_ends = True
        find_winner(auction)


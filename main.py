from art import logo
import os

# function to clear the output in the console
def clear():
    os.system('cls')

print(logo)

print("Welcome to the Secret Auction.")

bidders_available = True

bidders = {}

#function to get the highest bidder with its key value
def highest_bidder(biddings):
    highest_bid = 0
    winner = ""
    for bidder in biddings:
        bid = biddings[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while bidders_available:
    name = str(input("What is your name?\n"))
    bid = int(input("What's your bid?\n$"))
    bidders[name] = bid
    next_bid = str(input("Are there any bidders left?\nType Yes or No:\n")).lower()
    if next_bid == "no":
        bidders_available = False
        clear()
        highest_bidder(bidders)
    elif next_bid == "yes":
         clear()

# print(bidders)
# max_bid = max(bidders.values())
# print(max_bid)

    
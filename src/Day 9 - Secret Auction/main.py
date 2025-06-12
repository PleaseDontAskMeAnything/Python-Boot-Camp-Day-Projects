import os
from art import logo

bidTable = {}
biddingFinish = False
highestBidder = ""
highestBid = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def nextBid():
    continueBid = input("Are there any other bidders? Type 'yes' or 'no': ")
    if continueBid == 'yes' or continueBid == 'y':
        return False
    elif continueBid == 'no' or continueBid == 'n':
        return True
    else:
        print("Please start using your brain.")
        return nextBid()

print("Welcome to the Secret Auction Program!")
print(logo)
input("\nPress any key to continue...")

while not biddingFinish:
    clear()
    name = input("Name for this bid: ")
    bid = float(input("Bid Amount: $"))
    bidTable[name] = bid

    biddingFinish = nextBid()

for bidder in bidTable:
    if bidTable[bidder] > highestBid:
        highestBid = bidTable[bidder]
        highestBidder = bidder

print(f"The highest bidder is {highestBidder} with a bid of ${highestBid:.2f}.")
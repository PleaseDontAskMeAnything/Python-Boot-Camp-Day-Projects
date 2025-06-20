import os
import sys
from art import logo

bidTable = {}
biddingFinish = False
highestBidder = ""
highestBid = 0

def clear():
    # nt is for Windows, posix is for Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to wait for a key press without echoing it to the console
def keyPress():
    try:
        #For Windows
        if sys.platform.startswith('win'):
            import msvcrt
            msvcrt.getch()
            
        #For Unix/Linux/Mac
        else:
            import tty, termios
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
    except Exception as e:
        input("Something went wrong. Press any key to exit.")

def nextBid():
    continueBid = input("Are there any other bidders? Type 'yes' or 'no': ")
    if continueBid == 'yes' or continueBid == 'y':
        return False
    elif continueBid == 'no' or continueBid == 'n':
        return True
    else:
        print("Please start using your brain.")
        return nextBid()

clear()
print(f"Welcome to the Secret Auction Program!{logo}\n Press any key to start bidding.")
keyPress()

while not biddingFinish:
    clear()
    name = input("Name for this bid: ")
    while True:
        try:
            bid = float(input("Bid Amount: $"))
            break
        except ValueError:
            print("Please enter a valid number for the bid amount.")

    bidTable[name] = bid

    biddingFinish = nextBid()

for bidder in bidTable:
    if bidTable[bidder] > highestBid:
        highestBid = bidTable[bidder]
        highestBidder = bidder

clear()
print(f"The highest bidder is {highestBidder} with a bid of ${highestBid:.2f}.")
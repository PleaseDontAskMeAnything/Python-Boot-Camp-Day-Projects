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

choices = [rock, paper, scissors]

myChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if myChoice == "0" or myChoice == "1" or myChoice == "2":
    print(choices[int(myChoice)])
    print("Computer chose:")
    compChoice = random.randint(0, 2)
    print(choices[compChoice])

    if (myChoice == "0" and compChoice == 0) or \
    (myChoice == "1" and compChoice == 1) or \
    (myChoice == "2" and compChoice == 2):
        result = "It's a Draw! Lmao."

    elif (myChoice == "0" and compChoice == 1) or \
        (myChoice == "1" and compChoice == 2) or \
        (myChoice == "2" and compChoice == 0):
        result = "You lose, dumbass."

    elif (myChoice == "0" and compChoice == 2) or \
        (myChoice == "1" and compChoice == 0) or \
        (myChoice == "2" and compChoice == 1):
        result = "Oh wow, You won."
    
    print(result)

else:
    print("Bozo couldn't even choose a valid option.")
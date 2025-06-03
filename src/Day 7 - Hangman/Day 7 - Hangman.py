import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "donkey", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar"]

# chosen_word_text = random.choice(word_list)
chosen_word_text = "aardvark"  # For testing purposes
print(f"Chosen word: {chosen_word_text}")  # For debugging purposes
chosen_word = list(chosen_word_text.lower())
placeholder = ''
lives = 6

for i in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

placeholder_list = list(placeholder)
guess_list = []

while '_' in placeholder_list:
    correctGuess = False
    guess = input("Guess a letter: ").lower()
    if guess in guess_list:
        print("You already guessed that letter. Try again, maybe with a different letter this time.")
        continue
    else:
        guess_list.append(guess)

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholder_list[i] = guess
            correctGuess = True

    if correctGuess == False:
        print("Incorrect guess.")
        lives -= 1

    print(stages[lives])

    if lives == 0:
        print("You lost! The word was:", chosen_word_text)
        exit()      
          
    updated_placeholder = ''.join(placeholder_list)

    if '_' in updated_placeholder:
        print(f"Current Word: {updated_placeholder}.\nYou have {lives} lives remaining.\nKeep Trying\n" )

print(f"Congratulations! You've guessed the word: {updated_placeholder}")
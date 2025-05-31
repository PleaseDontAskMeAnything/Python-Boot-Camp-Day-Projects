import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "donkey", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar"]

chosen_word_text = random.choice(word_list)
print(f"Chosen word: {chosen_word_text}")  # For debugging purposes
chosen_word = list(chosen_word_text.lower())
placeholder = ''

for i in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

placeholder_list = list(placeholder)
guess_list = []

while '_' in placeholder_list:
    guess = input("Guess a letter: ").lower()
    if guess in guess_list:
        print("You already guessed that letter. Try again.")
        continue
    else:
        guess_list.append(guess)

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholder_list[i] = guess

    updated_placeholder = ''.join(placeholder_list)
    print(updated_placeholder)

print(f"Congratulations! You've guessed the word: {updated_placeholder}")
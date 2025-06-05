import random
import hangman_words
import hangman_art

def proceedIfNewChar(wordOfDeath, wordOfLife, guessOfGame, lifeOfHangman):
    correctGuess = False
    for i in range(len(wordOfDeath)):
        if wordOfDeath[i] == guessOfGame:
            wordOfLife[i] = guessOfGame
            correctGuess = True

    if correctGuess == True:
        print("That letter is indeed in the game. Good guess!")
    else:
        print("Yikes! That letter ain't in the word. Try again. In the meantime, you lose a life.")
        lifeOfHangman -= 1
    
    return wordOfLife, lifeOfHangman

lives = 6
guess_list = []
placeholder = []

print("Welcome to" + hangman_art.logo)

chosen_word_text = random.choice(hangman_words.word_list)
chosen_word = list(chosen_word_text.lower())

for i in range(len(chosen_word)):
    placeholder.append('_')

while '_' in placeholder:
    print(f"Word to guess: {''.join(placeholder)}")

    #guess = input("Guess a letter: ").lower()
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Please enter a single alphabetical character.")

    if guess in guess_list:
        print("You've already guessed that letter. Try again.")
    else:
        guess_list.append(guess)
        placeholder, lives = proceedIfNewChar(chosen_word, placeholder, guess, lives)

    print(f"You have {lives}/6 lives remaining.")
    print(hangman_art.stages[lives])
    if lives == 0:
        print(f"You lost! The word was: {chosen_word_text}")
        exit()

print(f"Congratulations! You've guessed the word: {''.join(placeholder)}")
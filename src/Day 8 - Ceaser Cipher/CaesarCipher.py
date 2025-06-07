from CaesarArt import logo

## The commented out code below is an alternative implementation of the Caesar cipher, and is here for show off.

# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for char in original_text:
#         if char in alphabetLower:
#             index = alphabetLower.index(char)
#             # Calculate the new index with wrapping around using modulo
#             new_index = (index + shift_amount) % len(alphabetLower)
#             encrypted_text += alphabetLower[new_index]
#         else:
#             # If it's not a letter, just append it unchanged
#             encrypted_text += char
#     print(f"Encrypted text: {encrypted_text}")

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for char in original_text:
#         if char in alphabetLower:
#             index = alphabetLower.index(char)
#             # Calculate the new index with wrapping around using modulo
#             new_index = (index - shift_amount) % len(alphabetLower)
#             decrypted_text += alphabetLower[new_index]
#         else:
#             # If it's not a letter, just append it unchanged
#             decrypted_text += char
#     print(f"Decrypted text: {decrypted_text}")

def caesar(directionCheck, original_text, shift_amount):
    output_text = ""
    for char in original_text:
        if char in alphabetLower:
            index = alphabetLower.index(char)
            # Calculate the new index with wrapping around using modulo
            if directionCheck == 'decode':
                new_index = (index - shift_amount) % len(alphabetLower)
            else:
                new_index = (index + shift_amount) % len(alphabetLower)
            output_text += alphabetLower[new_index]
        elif char in alphabetUpper:
            index = alphabetUpper.index(char)
            # Calculate the new index with wrapping around using modulo
            if directionCheck == 'decode':
                new_index = (index - shift_amount) % len(alphabetUpper)
            else:
                new_index = (index + shift_amount) % len(alphabetUpper)
            output_text += alphabetUpper[new_index]
        else:
            # If it's not a letter, just append it unchanged
            output_text += char
    print(f"Output text: {output_text}")

def gameStatus():
    toRepeat = input("Do you want to go again? Type 'yes' or 'no': ").lower()
    if toRepeat == 'yes' or toRepeat == 'y':
        return False
    elif toRepeat == 'no' or toRepeat == 'n':
        print("Goodbye, dear!")
        return True
    else:
        print("Please start using your brain.")
        return gameStatus()

alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabetUpper = [letter.upper() for letter in alphabetLower]

print(logo)
gameOver = False

while gameOver == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while direction not in ['encode', 'decode']:
        print("Dumbass. E or D. Try again!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    caesar(direction, text, shift)

    gameOver = gameStatus()
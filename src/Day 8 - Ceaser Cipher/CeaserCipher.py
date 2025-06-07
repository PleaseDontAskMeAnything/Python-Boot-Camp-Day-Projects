alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#TODO 1: Create 'encrypt()' that takes original_text and shift_amount as 2 inputs.

#TODO 2: Inside 'encrypt()', shift each letter of original_text forward by shift_amount and print the encrypted text.

#TODO 4: What happens if the shift is greater than 26? Try it out!

#TODO 3: Call 'encrypt()' and pass in the user inputs.
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            # Calculate the new index with wrapping around using modulo
            new_index = (index + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            # If it's not a letter, just append it unchanged
            encrypted_text += char
    print(f"Encrypted text: {encrypted_text}")

if direction == "encode":
    encrypt(text, shift)
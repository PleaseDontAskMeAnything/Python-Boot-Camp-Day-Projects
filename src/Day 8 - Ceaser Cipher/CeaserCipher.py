alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

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

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            # Calculate the new index with wrapping around using modulo
            new_index = (index - shift_amount) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            # If it's not a letter, just append it unchanged
            decrypted_text += char
    print(f"Decrypted text: {decrypted_text}")

def ceaser(directionCheck, original_text, shift_amount):
    output_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            # Calculate the new index with wrapping around using modulo
            if directionCheck == 'decode':
                new_index = (index - shift_amount) % len(alphabet)
            else:
                new_index = (index + shift_amount) % len(alphabet)
            output_text += alphabet[new_index]
        else:
            # If it's not a letter, just append it unchanged
            output_text += char
    print(f"Output text: {output_text}")


ceaser(direction, text, shift)
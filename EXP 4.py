# Polyalphabetic Cipher (Vigenere Cipher)

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char

    return ciphertext

plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

ciphertext = encrypt(plaintext, key)

print("Ciphertext:", ciphertext)

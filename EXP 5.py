    # Generalized Caesar Cipher

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key value: "))

ciphertext = ""

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            ciphertext += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    else:
        ciphertext += char

print("Ciphertext:", ciphertext)

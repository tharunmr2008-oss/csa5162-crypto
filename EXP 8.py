# Simple Substitution Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == "E":
    plaintext = input("Enter Plaintext: ").upper()
    ciphertext = ""

    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += key[index]
        else:
            ciphertext += char

    print("Ciphertext:", ciphertext)

elif choice == "D":
    ciphertext = input("Enter Ciphertext: ").upper()
    plaintext = ""

    for char in ciphertext:
        if char in key:
            index = key.index(char)
            plaintext += alphabet[index]
        else:
            plaintext += char

    print("Plaintext:", plaintext)

else:
    print("Invalid Choice")

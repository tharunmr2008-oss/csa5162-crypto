# Monoalphabetic Cipher Encryption and Decryption

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == "E":
    plaintext = input("Enter the plaintext: ").upper()
    ciphertext = ""

    for ch in plaintext:
        if ch in alphabet:
            index = alphabet.index(ch)
            ciphertext += key[index]
        else:
            ciphertext += ch

    print("Ciphertext:", ciphertext)

elif choice == "D":
    ciphertext = input("Enter the ciphertext: ").upper()
    plaintext = ""

    for ch in ciphertext:
        if ch in key:
            index = key.index(ch)
            plaintext += alphabet[index]
        else:
            plaintext += ch

    print("Plaintext:", plaintext)

else:
    print("Invalid Choice")

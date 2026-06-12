# Letter Frequency Attack on Additive Cipher

def decrypt(ciphertext, shift):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            plaintext += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += char

    return plaintext

ciphertext = input("Enter Ciphertext: ").upper()
n = int(input("Enter number of possible plaintexts to display: "))

print("\nPossible Plaintexts:\n")

for shift in range(min(n, 26)):
    print("Key =", shift)
    print(decrypt(ciphertext, shift))
    print()

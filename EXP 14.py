# One-Time Pad Encryption

plaintext = input("Enter Plaintext: ").upper()

# Enter random key values separated by space
key = list(map(int, input("Enter Key Stream: ").split()))

ciphertext = ""

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        p = ord(plaintext[i]) - ord('A')
        c = (p + key[i]) % 26
        ciphertext += chr(c + ord('A'))

print("Ciphertext:", ciphertext)

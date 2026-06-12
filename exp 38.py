# Hill Cipher Encryption (2x2 Matrix)

key = [[3, 3],
       [2, 5]]

plaintext = input("Enter Plaintext: ").upper()
plaintext = plaintext.replace(" ", "")

if len(plaintext) % 2 != 0:
    plaintext += 'X'

ciphertext = ""

for i in range(0, len(plaintext), 2):
    p1 = ord(plaintext[i]) - ord('A')
    p2 = ord(plaintext[i + 1]) - ord('A')

    c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
    c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

    ciphertext += chr(c1 + ord('A'))
    ciphertext += chr(c2 + ord('A'))

print("Ciphertext:", ciphertext)

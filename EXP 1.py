 # Caesar Cipher Encryption

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

cipher_text = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        cipher_text += char

print("Encrypted Text:", cipher_text)

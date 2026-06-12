

# Affine Cipher

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            c = (a * x + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def decrypt(text, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)

    for char in text.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            p = (a_inv * (y - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

plaintext = input("Enter Plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

ciphertext = encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)

decrypted = decrypt(ciphertext, a, b)
print("Decrypted Text:", decrypted)

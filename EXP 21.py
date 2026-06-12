# CBC Mode using Affine Cipher (Modulo 256)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt_cbc(plaintext, a, b, iv):
    ciphertext = []
    prev = iv

    for p in plaintext:
        x = p ^ prev
        c = (a * x + b) % 256
        ciphertext.append(c)
        prev = c

    return ciphertext

def decrypt_cbc(ciphertext, a, b, iv):
    plaintext = []
    prev = iv
    a_inv = mod_inverse(a, 256)

    for c in ciphertext:
        x = (a_inv * (c - b)) % 256
        p = x ^ prev
        plaintext.append(p)
        prev = c

    return plaintext

plaintext = [1, 35]
a = 5
b = 8
iv = 170

ciphertext = encrypt_cbc(plaintext, a, b, iv)
print("Ciphertext:", ciphertext)

decrypted = decrypt_cbc(ciphertext, a, b, iv)
print("Decrypted Plaintext:", decrypted)

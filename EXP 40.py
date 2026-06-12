from collections import Counter

ciphertext = input("Enter Ciphertext: ").upper()
top_n = int(input("Enter number of possible plaintexts: "))

# English letter frequency order
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# Count letter frequencies in ciphertext
freq = Counter(c for c in ciphertext if c.isalpha())

# Ciphertext letters ordered by frequency
cipher_freq = ''.join([item[0] for item in freq.most_common()])

for attempt in range(top_n):
    mapping = {}

    for i in range(min(len(cipher_freq), 26)):
        mapping[cipher_freq[i]] = english_freq[(i + attempt) % 26]

    plaintext = ""

    for ch in ciphertext:
        if ch.isalpha():
            plaintext += mapping.get(ch, ch)
        else:
            plaintext += ch

    print("\nPossible Plaintext", attempt + 1)
    print(plaintext)

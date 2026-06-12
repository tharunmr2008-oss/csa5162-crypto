from collections import Counter

ciphertext = input("Enter Ciphertext: ").upper()
top_n = int(input("Enter number of possible plaintexts: "))

english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

freq = Counter(c for c in ciphertext if c.isalpha())
cipher_freq = ''.join([item[0] for item in freq.most_common()])

for attempt in range(top_n):
    mapping = {}

    for i in range(min(len(cipher_freq), len(english_freq))):
        mapping[cipher_freq[i]] = english_freq[(i + attempt) % 26]

    plaintext = ""

    for ch in ciphertext:
        if ch.isalpha():
            plaintext += mapping.get(ch, ch)
        else:
            plaintext += ch

    print("\nPossible Plaintext", attempt + 1)
    print(plaintext)

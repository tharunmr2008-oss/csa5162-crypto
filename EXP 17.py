# DES Key Generation for Decryption

# Standard DES shift schedule
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

# Sample round keys
encryption_keys = []

key = "K"

for i in range(16):
    encryption_keys.append(key + str(i + 1))

print("Encryption Keys:")
for k in encryption_keys:
    print(k)

# Reverse order for decryption
decryption_keys = encryption_keys[::-1]

print("\nDecryption Keys:")
for k in decryption_keys:
    print(k)

# DES Subkey Generation Demonstration

# 56-bit key (example)
key = input("Enter 56-bit binary key: ")

# Split into two 28-bit halves
left = key[:28]
right = key[28:]

# Select first 24 bits from left half
left_sub = left[:24]

# Select first 24 bits from right half
right_sub = right[:24]

# Combine to form 48-bit subkey
subkey = left_sub + right_sub

print("Left Half (28 bits):", left)
print("Right Half (28 bits):", right)
print("First 24 bits from Left:", left_sub)
print("First 24 bits from Right:", right_sub)
print("48-bit Subkey:", subkey)

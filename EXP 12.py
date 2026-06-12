import math

# Effective unique Playfair keys
unique_keys = math.factorial(25) // 2

# Approximate power of 2
power = math.log2(unique_keys)

print("Effectively unique keys =", unique_keys)
print("Approximate power of 2 = 2^", round(power))

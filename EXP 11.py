import math

# Number of possible Playfair cipher keys
keys = math.factorial(25)

# Approximate power of 2
power = math.log2(keys)

print("Number of possible keys =", keys)
print("Approximate power of 2 = 2^", round(power))

# RSA Common Factor Check

import math

n = int(input("Enter n: "))
plaintext_block = int(input("Enter plaintext block: "))

g = math.gcd(plaintext_block, n)

if g > 1:
    print("Common factor found:", g)
    print("Other factor:", n // g)
    print("RSA modulus can be factored!")
else:
    print("No common factor found.")

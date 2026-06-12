# DSA vs RSA Signature Demonstration

import random

message = "HELLO"

# Simulating DSA signatures
k1 = random.randint(1, 100)
k2 = random.randint(1, 100)

dsa_signature1 = hash(message + str(k1))
dsa_signature2 = hash(message + str(k2))

print("DSA Signature 1:", dsa_signature1)
print("DSA Signature 2:", dsa_signature2)

# Simulating RSA signatures
rsa_signature1 = hash(message)
rsa_signature2 = hash(message)

print("\nRSA Signature 1:", rsa_signature1)
print("RSA Signature 2:", rsa_signature2)

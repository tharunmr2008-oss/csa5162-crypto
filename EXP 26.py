# RSA Key Leak Demonstration

print("RSA Security Check")

print("\nIf Bob's private key (d) is leaked:")

print("1. Attacker can compute phi(n)")
print("2. Attacker can derive new private keys")
print("3. Attacker can decrypt messages")

print("\nConclusion:")
print("Generating only a new public key and private key is NOT safe.")
print("A new modulus n (new primes p and q) must also be generated.")

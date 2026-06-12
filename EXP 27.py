# RSA Small Message Attack Demonstration

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Alphabet Mapping:")
for i in range(26):
    print(letters[i], "=", i)

print("\nSecurity Analysis")
print("Only 26 possible plaintext values exist (0-25).")
print("An attacker can encrypt all 26 values using the public key.")
print("Then compare the results with the intercepted ciphertext.")
print("This reveals the plaintext immediately.")

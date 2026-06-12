# CBC Error Propagation Demonstration

plaintext = ["P1", "P2", "P3", "P4"]

print("Original Plaintext Blocks:")
print(plaintext)

print("\nCase 1: Error in Ciphertext Block C1")
print("Affected Plaintext Blocks: P1 and P2")
print("Unaffected Plaintext Blocks: P3 and P4")

print("\nCase 2: Bit Error in Source Plaintext P1")
print("Affected Ciphertext Blocks: C1, C2, C3, C4")
print("Error propagates through all subsequent ciphertext blocks")

print("\nReceiver Side:")
print("All plaintext blocks from P1 onward may be corrupted")

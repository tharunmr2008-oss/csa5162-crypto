# CBC-MAC Forgery Demonstration

X = int(input("Enter message block X: "))
T = int(input("Enter MAC value T: "))

second_block = X ^ T

print("\nOriginal Message Block (X):", X)
print("MAC(X) =", T)

print("\nForged Two-Block Message:")
print("X || (X XOR T)")

print("Second Block =", second_block)

print("\nObservation:")
print("The CBC-MAC of X || (X XOR T) is again T.")

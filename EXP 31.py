# CMAC Subkey Generation

def left_shift(value, bits):
    return (value << 1) & ((1 << bits) - 1)

block_size = int(input("Enter block size (64 or 128): "))

if block_size == 64:
    Rb = 0x1B
elif block_size == 128:
    Rb = 0x87
else:
    print("Invalid block size")
    exit()

# Example L = E(K,0)
L = int(input("Enter L in hexadecimal: "), 16)

# Generate K1
if (L >> (block_size - 1)) & 1:
    K1 = left_shift(L, block_size) ^ Rb
else:
    K1 = left_shift(L, block_size)

# Generate K2
if (K1 >> (block_size - 1)) & 1:
    K2 = left_shift(K1, block_size) ^ Rb
else:
    K2 = left_shift(K1, block_size)

print("K1 =", hex(K1))
print("K2 =", hex(K2))

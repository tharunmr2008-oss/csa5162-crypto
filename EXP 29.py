# SHA-3 Capacity Lane Filling Demonstration

state_size = 1600      # SHA-3 state size
block_size = 1024      # Rate (r)

capacity = state_size - block_size

print("State Size =", state_size)
print("Block Size =", block_size)
print("Capacity =", capacity)

# Each lane = 64 bits
capacity_lanes = capacity // 64

print("Capacity Lanes =", capacity_lanes)

# After first absorption
filled = 0
rounds = 0

while filled < capacity_lanes:
    rounds += 1
    filled += 1

print("Number of message blocks needed =", rounds)

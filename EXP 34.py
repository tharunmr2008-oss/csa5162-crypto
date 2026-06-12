# Padding Demonstration

block_size = 8

message = input("Enter Binary Message: ")

padding_needed = block_size - (len(message) % block_size)

if padding_needed == block_size:
    # Add an entire padding block
    padded_message = message + "1" + "0" * (block_size - 1)
else:
    padded_message = message + "1" + "0" * (padding_needed - 1)

print("Original Message :", message)
print("Padded Message   :", padded_message)
print("Original Length  :", len(message))
print("Padded Length    :", len(padded_message))

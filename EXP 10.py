
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(plaintext, matrix):
    plaintext = plaintext.upper().replace("J", "I")
    text = ""

    i = 0
    while i < len(plaintext):
        a = plaintext[i]

        if i + 1 < len(plaintext):
            b = plaintext[i + 1]

            if a == b:
                text += a + "X"
                i += 1
            else:
                text += a + b
                i += 2
        else:
            text += a + "X"
            i += 1

    ciphertext = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]

        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

key = input("Enter Key: ")
plaintext = input("Enter Plaintext: ")

matrix = generate_matrix(key)

print("\n5x5 Matrix:")
for row in matrix:
    print(" ".join(row))

ciphertext = encrypt(plaintext, matrix)

print("\nCiphertext:", ciphertext)

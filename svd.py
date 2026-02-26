import math

# Original Matrix A
A = [
    [4, 8],
    [8, 4]
]

# 1/sqrt(2)  
val = 1 / math.sqrt(2)

# Correct U (eigenvectors aligned with singular values 12 and 4)
U = [
    [val, val],
    [val, -val]
]

# Sigma (singular values)
Sigma = [
    [12, 0],
    [0, 4]
]

# V^T (since A is symmetric, V = U)
VT = [
    [val, val],
    [val, -val]
]

# Function to multiply two 2x2 matrices
def multiply(X, Y):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Step 1: U * Sigma
US = multiply(U, Sigma)

# Step 2: (U * Sigma) * V^T
A_reconstructed = multiply(US, VT)

print("U:")
for row in U:
    print(row)

print("\nSigma:")
for row in Sigma:
    print(row)

print("\nV^T:")
for row in VT:
    print(row)

print("\nReconstructed Matrix A = U * Sigma * V^T:")
for row in A_reconstructed:
    print(row)
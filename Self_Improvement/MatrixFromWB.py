countZeros = 0
countObstacles = 0

M = [
    [1, 1, 2, 2, 1, 1, 1, 3],
    [1, 0, 1, 0, 0, 0, 0, 3],
    [1, 0, 2, 1, 3, 3, 0, 1],
    [3, 0, 0, 0, 0, 1, 1, 1],
    [2, 0, 4, 1, 1, 0, 4, 1],
    [1, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 2, 3, 0, 4, 4]
]

for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == 0:
            countZeros += 1
        elif M[i][j] >= 2:
            M[i][j] *= 2
        elif M[i][j] > 0:
            countObstacles += 1
        
print(f"Number of entries equal to 0: ", countZeros)
print(f"Number of entries higher than 0: ", countObstacles)
print(f"Number of entries after doubling Matrix: ")
print(M)
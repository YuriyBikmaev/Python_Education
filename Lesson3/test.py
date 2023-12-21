def spiral_transposition(matrix):
    return matrix and list(matrix.pop(0)) + spiral_transposition(list(zip(*matrix))[::-1])

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(spiral_transposition(m))
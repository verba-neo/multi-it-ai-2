import sys
sys.stdin = open("input.txt", "r")
import numpy as np

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = np.zeros((N,N))
    row = 0
    col = 0
    new_row = 0
    new_col = 0
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]
    idx = 0
    move = 0
    while move != N ** 2:
        new_row = row + d_row[idx]
        new_col = row + d_col[idx]

        if 0 < new_row < N and 0 < new_col < N and matrix[new_row][new_col] == 0:
            row, col = new_row ,new_col
            matrix[row][col] = move
        else:
            idx = (idx + 1)% 4
        print(matrix)


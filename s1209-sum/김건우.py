import sys
from typing import List

sys.stdin = open('input.txt')

T = 10
size = 100

for tc in range(1, T + 1):
    N = int(input())

    # 빈 메트릭스
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # 메트릭스에 입력 받은 값 넣기
    for row in range(size):
        matrix[row] = list(map(int, input().split()))

    # 가로 최댓값
    max_row_sum = 0
    for row in range(size):
        row_sum = sum(matrix[row])
        if max_row_sum < row_sum:
            max_row_sum = row_sum

    # 세로 최댓값
    max_col_sum = 0
    rotated = list(zip(*matrix[::-1]))
    for col in range(size):
        col_sum = sum(rotated[col])
        if max_col_sum < col_sum:
            max_col_sum = col_sum

    # 순방향 대각선의 합
    diagonal_sum1 = 0
    for i in range(size):
        diagonal_sum1 += matrix[i][i]

    # 역방향 대각선의 합
    diagonal_sum2 = 0
    for i in range(size):
        j = size - i - 1
        diagonal_sum2 += matrix[i][j]

    # 대각선 최댓값
    max_diagonal_sum = diagonal_sum1 if diagonal_sum1 > diagonal_sum2 else diagonal_sum2

    # 최댓값 구하기
    max_sum = max(max_row_sum, max_col_sum, max_diagonal_sum)
    print(f'#{tc} {max_sum}')

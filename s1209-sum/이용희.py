import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    matrix = [[0 for _ in range(100)] for _ in range(100)]
    max_sum = 0
    for row in range(100):
        matrix[row] = list(map(int, input().split()))
    for row in range(100):
        if max_sum < sum(matrix[row]):
            max_sum = sum(matrix[row])
    for column in range(100):
        sum_value = 0
        for row in range(100):
            sum_value += matrix[row][column]
        if max_sum < sum_value:
            max_sum = sum_value

    sum_cross_value = 0
    for cross in range(100):
        sum_cross_value += matrix[cross][cross]
    if max_sum < sum_cross_value:
        max_sum = sum_cross_value

    sum_reverse_cross_value = 0
    for cross in range(99, -1, -1):
        sum_reverse_cross_value += matrix[cross][cross]
    if max_sum < sum_reverse_cross_value:
        max_sum = sum_reverse_cross_value

    print(f'#{test_case} {max_sum}')

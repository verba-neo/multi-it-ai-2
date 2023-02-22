# 10개의 테스트 케이스
# 100X100 배열
# 각 행/열/대각선의 합 중 최대값 구하기

import sys
sys.stdin = open("input.txt", "r")

T = 10    # 테스트 케이스
for test_case in range(1, T+1):
    tc = int(input())   # 각 테스트 케이스 번호
    num = [[0 for q in range(100)] for r in range(100)]
    max_sum = 0
    for i in range(0, 100):     # 100X100 배열 입력
        num[i] = list(map(int, input().split()))
    for j in range(0, 100):     # 각 행의 합 중 최대값
        sum_row = 0
        for k in range(0, 100):     # j 행의 총합
            sum_row += num[j][k]
        if sum_row >= max_sum:
            max_sum = sum_row
    for m in range(0,100):      # 각 열의 합 중 최대값
        sum_col = 0
        for n in range(0,100):      # m 열의 총합
            sum_col += num[n][m]
        if sum_col >= max_sum:
            max_sum = sum_col
    sum_dig = 0
    for p in range(0, 100):
        sum_dig += num[p][p]
    if sum_dig >= max_sum:
        max_sum = sum_dig

    print(f"#{tc} {max_sum}")




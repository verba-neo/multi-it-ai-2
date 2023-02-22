import sys
sys.stdin = open('input.txt')
for _ in range(10):
    test_case = int(input())
    sum_matrix = []
    sum_max = 0
    sum_cross_list = 0
    sum_cross_div_list = 0
    # matrix 생성
    for _ in range(100):
        row_matrix = list(map(int, input().split(' ')))
        sum_matrix.append(row_matrix)
    for i in range(100):
        # column 합구하기 초기화
        sum_column_list = 0
        # cross 합구하기
        sum_cross_list += sum_matrix[i][i]
        # 역 cross 합구하기
        sum_cross_div_list += sum_matrix[99-i][i]
        # column 합구하기
        for j in range(100):
            sum_column_list += sum_matrix[j][i]
        if sum_max < max(sum(sum_matrix[i]), sum_column_list):
            sum_max = max(sum(sum_matrix[i]), sum_column_list)
    print(f'#{test_case} {max(sum_max, sum_cross_list, sum_cross_div_list)}')


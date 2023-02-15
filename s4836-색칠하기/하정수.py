import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    coloring = int(input())
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    info_of_colors = [list(map(int, input().split())) for _ in range(coloring)]
    purple = 0

    for n in range(coloring):
        row_now = info_of_colors[n][0]
        col_now = info_of_colors[n][1]
        row_to = info_of_colors[n][2] + 1
        col_to = info_of_colors[n][3] + 1

        if info_of_colors[n][4] == 1:
            for r in range(row_now, row_to):
                for c in range(col_now, col_to):
                    if matrix[r][c] == 2:
                        purple += 1
                    else:
                        matrix[r][c] = 1

        elif info_of_colors[n][4] == 2:
            for r in range(row_now, row_to):
                for c in range(col_now, col_to):
                    if matrix[r][c] == 1:
                        purple += 1
                    else:
                        matrix[r][c] = 2

    print(f'#{test_case} {purple}')




import sys

sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    T = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]
    now = []
    for col in range(100):
        if ladder_matrix[99][col] == 2:
            now = [98, col]

    while now[0] > 0:
        if now[1] == 0:
            if ladder_matrix[now[0]][now[1] + 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] + 1]
            else:
                now = [now[0] - 1, now[1]]

        elif now[1] == 99:
            if ladder_matrix[now[0]][now[1] - 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]
            else:
                now = [now[0] - 1, now[1]]

        else:
            if ladder_matrix[now[0]][now[1] + 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] + 1]

            elif ladder_matrix[now[0]][now[1] - 1] == 1:
                ladder_matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]

            else:
                now = [now[0] - 1, now[1]]

    print(f'#{test_case} {now[1]}')

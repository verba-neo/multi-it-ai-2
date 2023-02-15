import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    triangle = [[] for _ in range(num)]
    triangle[0] = [1]
    col = 1
    for row in range(1, num):
        for n in range(row + 1):
            if n == 0 or n == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row - 1][n - 1] + triangle[row - 1][n])

    print(f'#{test_case}')
    for i in range(len(triangle)):
        print(*triangle[i])



import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    red_list = []
    blue_list = []
    result = 0
    for _ in range(N):
        *coordinate, color = list(map(int, input().split()))
        if color == 1:
            for x in range(coordinate[0], coordinate[2]+1):
                for y in range(coordinate[1], coordinate[3] + 1):
                    red_list.append([x, y])
        else:
            for x in range(coordinate[0], coordinate[2]+1):
                for y in range(coordinate[1], coordinate[3] + 1):
                    blue_list.append([x, y])

    for red in red_list:
        for blue in blue_list:
            if red == blue:
                result += 1
    print(f'#{test_case} {result}')

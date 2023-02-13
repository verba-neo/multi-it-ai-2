import sys
sys.stdin = open("input.txt", "r")

T = int(input())    # testcase를 받을 개수

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    count = 0
    result = 0  # 결과 값을 추가할 값
    for list_num in range(N):
        puzzle.append(list(map(int, input().split())))  # 퍼즐에 2차원 배열 추가

    for i in range(0, N):
        check = 0
        for j in range(0, N):
            if puzzle[i][j] == 1:
                check += 1
            else:
                if check == K:
                    result += 1
                check = 0

        if check == K:
            result += 1

    for x in range(0, N):
        check = 0
        for y in range(0, N):
            if puzzle[y][x] == 1:
                check += 1
            else:
                if check == K:
                    result += 1
                check = 0
        if check == K:
            result += 1

    print(f"#{tc} {result}")




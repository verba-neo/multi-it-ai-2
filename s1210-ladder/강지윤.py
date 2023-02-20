import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    graph = [list(map(int,input().split())) for i in range(100)]
    memoezation = [[0]*100 for i in range(100)]

    row_col = []
    answer = []

    for i in range(100):
        if not row_col:
            print(answer)
            break

        if graph[0][i] == 1:
            row_col.append((0,i))














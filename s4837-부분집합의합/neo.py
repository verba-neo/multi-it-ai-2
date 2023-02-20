import sys
sys.stdin = open('input.txt')


def dfs(idx):
    global count, subset

    if idx == len(numbers):
        return

    if len(subset) == N:
        if sum(subset) == K:
            print(subset)
            count += 1
        return

    subset.append(numbers[idx])
    dfs(idx+1)
    subset.pop()
    dfs(idx+1)


T = int(input())

for tc in range(1, T+ 1):
    N, K = map(int, input().split())

    numbers = [i for i in range(1, 13)]
    subset = []
    count = 0
    dfs(0)
    print(f'{tc} {count}')



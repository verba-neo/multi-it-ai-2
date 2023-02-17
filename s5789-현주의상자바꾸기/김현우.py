from collections import deque


def solution(s, e):
    answer = 0
    check = [0] * 10001
    queue = deque()
    queue.append(s)
    check[s] = 1
    L = 0

    while (queue):
        length = len(queue)
        for _ in range(length):
            x = queue.popleft()
            for nx in [x - 1, x + 1, x + 5]:
                if nx == e:
                    return L + 1
                if nx > 0 and nx <= 10000 and check[nx] == 0:  # 오류가 발생했던 부분
                    check[nx] = 1
                    queue.append(nx)
        L += 1
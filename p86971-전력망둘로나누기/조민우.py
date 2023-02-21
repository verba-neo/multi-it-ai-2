def dfs(v):
    visited[v] = True
    for new_v in graph[v]:
        if not visited[new_v]:
            dfs(new_v)


def solution(n, wires):
    global graph
    graph = [[] for _ in range(n + 1)]
    global visited
    visited = [False for _ in range(n + 1)]
    # 간선 입력
    print(wires[0])
    for i in range(len(wires)):
        start, end = wires[i][0], wires[i][1]
        graph[start].append(end)
        # 양방향(무향)그래프 일 경우 아래 줄 추가
        graph[end].append(start)
    print(graph)
    answer = -1
    dfs(n)
    return answer


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

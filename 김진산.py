import sys
from collections import deque
sys.stdin = open('input.txt')

# N은 정점 Node, M은 간선 V는 탐색
N, M, V = map(int,input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N + 1)
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

def bfs(graph, v, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
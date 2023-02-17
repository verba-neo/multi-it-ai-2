import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):

    Vertex, Edge = map(int,input().split())

    graph = {}

    for i in range(Edge):
        Start, Arrive = map(int,input().split())

        if Start not in graph:
            graph[Start] = []
            graph[Start].append(Arrive)
        else:
            graph[Start].append(Arrive)

    S, G = map(int,input().split())


    history_graph = []
    visited = [S]
    flag = 0
    #판단
    def dfs(V,G):
        if V == G:
            global flag
            flag = 1
            return


        if V in graph:
            for next_v in graph[V]:
                if next_v not in visited:
                    visited.append(next_v)
                    dfs(next_v,G)
                    visited.pop()


    dfs(S, G)
    if flag == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')


















import sys
sys.stdin = open('input.txt')
def dfs(s):
    visit[s] = False
    for i in graph[s]:
        if visit[i] == True:
            dfs(i)

testCase = int(input())

for i in range(testCase):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visit  = [True for _ in range(v+1)] #방문여부 확인

    for j in range(e):
        a,b = map(int,input().split())
        graph[a].append(b) #각 노드별 간선들을 추가

    s,g = map(int,input().split()) #출발노드와 도착노드
    dfs(s)
    result = 1
    if visit[g]==True:
        result = 0
    print('#'+str(i+1)+' '+str(result))
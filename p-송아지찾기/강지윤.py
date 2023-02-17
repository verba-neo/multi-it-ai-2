from collections import deque

def solution(s, e):
    #몇번만에 찾았는지
    count = 0
    #목적지
    to_visits = [s]
    #방문여부
    visited = [False for _ in range(10000)]
    while(to_visits):
        for _ in range(len(to_visits)):
            current = to_visits.pop(0)

            if not visited[current]:
                #현재 위치 갱신
                visited[current] = True
                if current == e:
                    return count

                for nxt in [current-1, current+1, current+5]:
                    #다음 갈 노드들
                    if 0<nxt<=10000 and not visited[nxt]:
                        to_visits.append(nxt)

        count+=1
    return count


# 3
print(solution(5, 14))
# 5
print(solution(8, 3))
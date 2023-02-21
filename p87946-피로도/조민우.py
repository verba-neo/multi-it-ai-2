import itertools

def dfs(idx,k,dungeons,count_d_1):
    global count_d, k_d
    k_d = k
    count_d = count_d_1

    # 현재 idx 가 numbers의 길이와 같다 => 부분 집합 완성
    if idx == len(dungeons):
        # 조건을 만족했다면, count 추가
        print(subset)
        if subset:
            if k_d >= subset[0][0]:
                print(subset)
                count_d += 1
                k_d -= subset[0][1]
                print(k_d)
        return

    subset.append(dungeons[idx])
    dfs(idx+1,k_d,dungeons,count_d)
    # visited[idx] = True

    subset.pop()
    dfs(idx+1,k_d,dungeons,count_d)
    # visited[idx] = False
def solution(k, dungeons):
    answer = []
    global subset
    subset =[]
    dfs(0,k,dungeons,0)
    #  itertools.permutations을 이용해 피로도와 상관없이 던전 이용의 모든 경우의 수 생성
    for i in itertools.permutations(dungeons,len(dungeons)):
        # 현재 피로도
        fatigue = k
        count = 0
        # 필요 피로도, 소모 피로도
        for essential, consume in i:
            # 필요 피로도가 현재 피로도 이하 일때
           if fatigue >= essential:
               # 현재 피로도에서 소모 피로도를 차감
               fatigue -= consume
               # count를 증가시켜서 던전 이용 기록
               count += 1
        answer.append(count)
        print(count_d)
        # max()를 이용해 가장 큰 값 리턴
    # dfs

        # 포함 여부
        # visited = [False] * 12



    return max(answer)






print(solution(80,[[80,20],[50,40],[30,10]]))
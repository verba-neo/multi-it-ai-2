
def solution(ability):
    answer = 0
    sum_p = 0
    def dfs(ab_sum, idx):
        nonlocal sum_p


        if  ab_sum >= sum_p:
            return
        for i in range(len(ability)):
            if not visited[i]:
                visited[i] =True
                ab_sum += dfs(ab_sum,idx+1) + sum_p
                visited[i] = False
                sum_p = ab_sum

    visited = [False for _ in range(len(ability))]
    dfs(0,0)
    print(sum_p)
    return answer



# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))
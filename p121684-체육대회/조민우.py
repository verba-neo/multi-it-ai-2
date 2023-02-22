def solution(ability):
    answer = 0
    for i in range(len(ability[0])):
        for j in range(len(ability)):
            print(ability[j][i])
    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))
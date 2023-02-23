from itertools import combinations, permutations
def solution(ability):
    answer = 0
    point = 0
    for i in permutations(ability,3):
        for j in range(3):
            for k in range(3):
                print(i[j][k])
            if point < sum(i[j]):
                point = sum(i[j])
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
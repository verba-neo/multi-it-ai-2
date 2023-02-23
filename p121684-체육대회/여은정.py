from itertools import permutations


def solution(arr_list):

    #
    max_value = 0
    # print(itertools.permutations(arr_list, 3))
    p = list(permutations(arr_list, len(arr_list[0])))
    for i in range(len(p)):
        total = 0
        for j in range(len(p[i])):
            total += p[i][j][j]     #
        max_value = max(max_value, total)

    return max_value



print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))





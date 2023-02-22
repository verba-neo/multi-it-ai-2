from itertools import combinations


def solution(numbers, target):
    answer = 0
    idx_list = [idx for idx in range(len(numbers))]
    for idx in range(len(idx_list) + 1):
        for combinations_list in combinations(idx_list, idx):
            sum_number = 0
            for number in range(len(numbers)):
                cal = numbers[number]
                if number in combinations_list:
                    cal *= -1
                sum_number += cal
            if sum_number == target:
                answer += 1
    return answer


solution([4, 1, 2, 1], 4)

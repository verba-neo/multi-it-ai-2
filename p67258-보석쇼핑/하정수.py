def solution(gems):
    every = len(gems)
    gem = list(set(gems))
    kind = len(gem)
    possible = [0, 0, every]
    for start in range(every - kind + 1):
        test_gem = gem[:]
        test_gem.remove(gems[start])
        for end in range(start, every):
            if gems[end] in test_gem:
                test_gem.remove(gems[end])
            if len(test_gem) == 0:
                if (end - start) < possible[2]:
                    possible = [start + 1, end + 1, end - start]

    answer = possible[0:2]
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

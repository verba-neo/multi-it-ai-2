def solution(gems):


    shelf = [i for i in gems]
    gems_set = {i for i in gems}
    answer = []
    i = 0
    j = len(shelf)
    k = 0
    while i < j:
        print(set(shelf[i:]) & gems_set)
        if len(set(shelf[i:]) & gems_set) == len(gems_set):
            k = i
        else:
            answer.append(k+1)
            break
        i += 1
    return answer


print('1',solution(["DIA", "RUBY", "RUBY","DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print('2',solution(["AA", "AB", "AC", "AA", "AC"]))
print('3',solution(["XYZ", "XYZ", "XYZ"]))
print('4',solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
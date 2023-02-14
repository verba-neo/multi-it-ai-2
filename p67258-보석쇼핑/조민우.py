def solution(gems):


    shelf = [i for i in gems]
    gems_set = {i for i in gems}
    answer = []
    i = 0
    j = len(shelf)
    k = 0
    while i < j:
        if len(set(shelf[i:]) & gems_set) == 4:
                i += 1
        else:
            if i == 0:
                answer.append(i+1)
                break
            elif i != 0:
                answer.append(i)
                break

    while j > i-1:
        if len(set(shelf[i-1:j]) & gems_set) == len(gems_set):
            j -= 1
        else:
            break
    if len(gems_set) == 1:
        print(shelf[i - 1:j])
        answer.append(i+1)
    elif len(shelf[i-1:j]) >= len(gems_set):

        answer.append(len(shelf[i-1:j]))
        print(shelf[i-1:j])
    else:
        print(shelf[i - 1:j])
        answer.append(j+1)

    return answer


print('1',solution(["DIA", "RUBY", "RUBY","DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print('2',solution(["AA", "AB", "AC", "AA", "AC"]))
print('3',solution(["XYZ", "XYZ", "XYZ"]))
print('4',solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
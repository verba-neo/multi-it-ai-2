def solution(input_string):
    answer = ''
    solo_alphabet = []
    check_list = []
    temp = []
    for i in input_string:
        check_list.append(i)
    for i in range(0, len(check_list)-1):
        if check_list[i] != check_list[i + 1]:
            for j in range(i + 1, len(check_list)):
                if check_list[i] == check_list[j]:
                    solo_alphabet.append(check_list[i])


    if len(solo_alphabet) == 0:
        answer = 'N'
        return answer
    else:
        temp = list(sorted(set(solo_alphabet)))
        answer = ''.join(temp)
        return answer




    return answer


print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))
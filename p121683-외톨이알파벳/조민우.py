def solution(input_string):

    check = []
    list = []
    check_str = 'r'
    if len(input_string) != len(set(input_string)):
        for txt in input_string:
            if check and txt == check[-1]:
                check_str = check.pop()
                list.append(check_str)
            else:
                if check_str != txt:
                    check.append(txt)
        result = ""
        for string in set(check):
            result += string
        return result
    else:
        return 'N'




print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution('string'))
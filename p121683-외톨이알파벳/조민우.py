def solution(input_string):

    check = []
    list = []
    check_str = [0]
    if len(input_string) != len(set(input_string)):
        for txt in input_string:
            if check and txt == check[-1]:
                check_str.append(check.pop())

            elif check_str[-1] != txt:
                check.append(txt)


        for i in set(check_str):
            if check_str.count(i) >= 2:
                check.append(i)

        result = ""

        for string in sorted(set(check)):

            result += string

        return result
    else:
        return 'N'




print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution('string'))
print(solution('zbzbz'))
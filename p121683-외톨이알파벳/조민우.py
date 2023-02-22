def solution(input_string):
    answer =''
    count =1
    dict = {}
    dict[input_string[0]] = []
    check = [input_string[0]]
    for txt in input_string:
        if txt not in check[-1]:
            check.append(txt)
            dict[txt] = []
    print(dict)

    for txt in check:
        dict[txt].append(count)
    for key in dict.keys():
        if len(dict[key]) >= 2:
            answer += key

    answer = "".join(sorted(answer))
    if answer:
        return answer
    else:
        return "N"

    print(check)
    print(dict)

    # check = []
    # list = []
    # check_str = [0]
    # if len(input_string) != len(set(input_string)):
    #     for txt in input_string:
    #         if check and txt == check[-1]:
    #             check_str.append(check.pop())
    #
    #         elif check_str[-1] != txt:
    #             check.append(txt)
    #
    #
    #     for i in set(check_str):
    #         if check_str.count(i) >= 2:
    #             check.append(i)
    #
    #     result = ""
    #
    #     for string in sorted(set(check)):
    #
    #         result += string
    #
    #     return result
    # else:
    #     return 'N'




print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution('string'))
print(solution('zbzbz'))
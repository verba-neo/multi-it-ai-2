
def solution(input_string):
    answer = []
    string_dic = {}
    for string in input_string:
        string_dic[string] = []

    string_num = 0
    for string in input_string:
        string_dic[string].append(string_num)
        string_num += 1

    string_set = 0
    for string_key in string_dic:
        for string_value in range(len(string_dic[string_key])):
            if string_value == 0:
                string_set = string_dic[string_key][string_value]
            else:
                if string_dic[string_key][string_value] - string_set != 1:
                    answer.append(string_key)
                string_set = string_dic[string_key][string_value]
    if len(string_dic) == 1:
        for string_key in string_dic:
            answer.append(string_key)

    done = ''
    for result in sorted(list(set(answer))):
        done += result
    if not done:
        done = 'N'
    print(done)


solution("string")


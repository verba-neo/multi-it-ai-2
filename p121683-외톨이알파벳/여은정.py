def solution(input_string):
    answer = ''

    # 수를 세기 위해 알파벳 딕셔너리 선언
    count = {}

    # 딕셔너리에 저장된 요소 중에 value 의 길이가 2 이상인 요소들
    answer_list = []

    for idx, alpha in enumerate(input_string):
        if alpha not in count:
            count[alpha] = [idx]
        else:
            count[alpha].append(idx)
    #
    for key, value in count.items():
        if len(value) >= 2:  #  여러번 등장하는 애들 중
            for i in range(len(value) - 1):
                if abs(value[i] - value[i + 1]) > 1: # 거리가 떨어져 있으면 외톨이
                    answer_list.append(key)
                    break
    if len(answer_list) == 0: # 없으면
        answer = 'N'
    else:
        answer = ''.join(sorted(answer_list))

    return answer

print(solution("edeaaabbccd"))
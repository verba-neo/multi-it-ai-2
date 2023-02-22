알파벳 소문자로만 이루어진 어떤 문자열에서, 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.

문자열 "edeaaabbccd"를 예시로 들어보면,

a는 2회 이상 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ede(aaa)bbccd"
b, c도 a와 같은 이유로 외톨이 알파벳이 아닙니다.
d는 2회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"e(d)eaaabbcc(d)"
e도 d와 같은 이유로 외톨이 알파벳입니다.
문자열 "eeddee"를 예시로 들어보면,

e는 4회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
"(ee)dd(ee)"
d는 2회 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
"ee(dd)ee"
문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요. 만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.

import sys
sys.stdin = open('input.txt')
def solution(input_string):
    answer = ''
    count = {}
    answer_list = []
    for idx, alpha in enumerate(input_string):
        if alpha not in count:
            count[alpha] = [idx]
        else:
            count[alpha].append(idx)

    for key, value in count.items():
        if len(value) >= 2:
            for i in range(len(value) - 1):
                if abs(value[i] - value[i + 1]) > 1:
                    answer_list.append(key)
                    break

    if len(answer_list) == 0:
        answer = "N"
    else:
        answer = ''.join(sorted(answer_list))

    return answer
def solution(input_string):
    first = []   # 처음 나온 알파벳 저장 리스트(확인 겸용)
    lone = []   # 두 번 나와서 외톨이가 된 알파벳 리스트
    now = -1   # 리스트 인덱싱을 위해 -1로 초기화
    for char in input_string:
        if now == -1:   # 첫 알파벳은
            first.append(char)   # first리스트에 저장하고
            now += 1   # 현재 인덱스 수정
        else:
            if char not in first:   # 처음나온 알파벳이면
                first.append(char)   # first리스트에 저장하고
                now += 1   # 현재 인덱스 수정
            else:
                if char != first[now]:   # 처음 나온 알파벳이 아닌경우 이전 알파벳과 다를 때
                    first.append(char)   # 현재 알파벳을 first리스트에 저장하고(다음과 현재가 같은지 확인하기 위해)
                    now += 1   # 현재 인덱스 수정
                    lone.append(char)   # 외톨이 알파벳에 추가
# sort 후 set을 하여 계산 시 pycharm에서는 정상작동하지만 제출시 순서가 바뀌지 않음
    cal = []   # 계산용 리스트를 초기화
    for char in set(lone):   # set한 외톨이 알파벳을
        cal.append(char)   # 계산리스트에 추가하고
    cal.sort()   # sort하여 순서를 정렬한다

    answer = ""   # answer에 저장한다
    for char in cal:
        answer += char

    if lone:   # 외톨이알파벳이 있으면 저장한 값을 반환하고
        return answer
    else:   # 없으면 "N"을 추가하여 반환한다
        answer = "N"
        return answer
#1. git pull
#2. 자기 브랜치에서 자기 이름으로 파일 만들기
#3. 문제 풀기
#4. 푼 코드 add -> commit
#5.git push orgin <브랜치이름>
def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i

    return sum


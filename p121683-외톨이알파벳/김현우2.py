import sys
sys.stdin = open('input.txt')


# answer_list 에 저장된게 없으면 answer= N ,그렇지x answer_list를 정렬하고 문자열로 만들어서 answer에저장
# 인자로 받은문자열에서 어느 인덱스위치에잇는지 알기위해 딕셔너리로저장
# 딕셔너리에 저장된 요소중에 value의 길이가 2이상인요소들 중 인정안되면 answer_ list 에저장
def solution(input_string):
    answer = ''
    count = {}
    answer_list = []
    for idx, alpha in enumerate(input_string): # 알파를 enumerate 자료형을 입력받아 인덱스와 요소를 포함 enumerate 개체를 반환
        if alpha not in count:  # 알파 가아니면 count
        count[alpha] = [idx]    # count[alpha] = [idx] 같다 정의
        else:
            count[alpha].append(idx)  # 그렇지 않으면 count[alpha]를 추가한다

         for key value in count.items(): # key ,value 값 반복 루프 생성
             if len(value) = 2: # 문자열 길이 2이상인지를 확인한다
                 for i in range(len(value) - 1): # range 루프를 생성합니다
                     if abs(value[i]-value[i+1]) > 1: # value리스트 두 값의 차이가 1보다 큰지 확인하고 반환합니다.
                         answer_list.append(key) # answer_list 에 key라는 값을 추가한다
                        break      # 루프를 종료한다
        if len(answer_list) == 0: # answer_list 0인지 확인한다
            answer = "N"  # answer 은 N 과 같다
    else: answer = ''.join(sorted)(answer_list) #1번이 안되면 answer_list 문자열을합친걸 정렬한다

    return answer   #  answer 로 돌아갑니다

print(solution("edeaaabbccd"))
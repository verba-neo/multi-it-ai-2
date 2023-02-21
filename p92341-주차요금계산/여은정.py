import math

# 시간 계산 함수
def convert(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)

def solution(fees, records):
    intime = {} # 키 값을 가진 현재 상태 딕셔너리
    result = {} # 키 값을 가진 결과 딕셔너리

    for r in records:
        time, num, inout = r.split()
        if inout == 'IN':
            intime[num] = convert(time) # 차량번호를 키로 설정
            if num not in result:
                result[num] = 0
        else:
            result[num] += convert(time) - intime[num] # 주차 시간 계산 입차시간 - 출차시간
            del intime[num]

    for key, val in intime.items():  # 출차 하지 않은 차들 주차 시간 계산
        result[key] += 23*60 + 59 - val

    answer = []
    for key, val in sorted(result.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((val - fees[0])/fees[2]) * fees[3])

    return answer
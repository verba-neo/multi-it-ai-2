import sys

sys.stdin = open('input.txt')


# 남학생 : 스위치 번호가 자기가 받은 수의 배수 이면 스위치의 상태를 바꾼다.
# 여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의
# 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

T = int(input())

switch = list(map(int, input().split()))

switch.insert(0,0)

numOfStudent = int(input())

flag = 0

li = []
for _ in range(numOfStudent):
    tp = tuple(map(int,input().split()))
    li.append(tp)



for tp in li :
    if tp[0] == 1:
        for i in range(1, len(switch)):
            if i%tp[1] == 0:
                if switch[i] == 1:
                    switch[i] = 0
                else:
                    switch[i] = 1


    else:
        if switch[tp[1]] == 1:
            switch[tp[1]] = 0
        else:
            switch[tp[1]] = 1

        for i in range(1,T):
            if tp[1]-i <= 0 or tp[1]+i>T-1:
                break
            if switch[tp[1]-i] == switch[tp[1]+i]:
                flag = 1
                if switch[tp[1]-i] ==1 :
                    switch[tp[1]+i] = switch[tp[1]-i] = 0
                else:
                    switch[tp[1] + i] = switch[tp[1] - i] = 1




print(*switch[1:])





#남학생은 1 여학생은 2


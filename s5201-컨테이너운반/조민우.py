# N개의 컨테이너 M대의 트럭 A to B
# M대의 트럭 편도로 운반, 컨테이너마다 화물의 무게와 트럭의 적재용량 주어짐
# 화물의 총 중량이 최대 -> 화물의 전체 무게가 얼마인지 출력
# 컨테이너를 한 개도 옮길 수 없는 경우 0 출력

# 출력 값으로 화물의 전체 무게 or 0
from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 컨테이너 수 , 트럭 대 수
    N, M = map(int, input().split())
    # 적재화물의 무게
    container = list(map(int, input().split()))
    container.sort(key=lambda x: -x)
    # 트럭 적재용량
    capacity = list(map(int, input().split()))
    capacity.sort(key=lambda x: x)
    # 현재 사용되는 트럭의 용량
    truck_cnt = 0
    # 운반되는 화물의 무게
    total_weight = []
    for truck in capacity:
        for weight in container:

            if truck >= weight:
                container.remove(weight)
                total_weight.append(weight)
                truck_cnt += weight
                truck -= weight

    if weight:
        print(f'#{test_case} {truck_cnt}')
    else:
        print(f'#{test_case} {0}')





import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    view_count = 0
    # 앞에서 세번째 건물부터 뒤에서 세번째 건물까지 확인
    for i in range(2, N-2):
        # 왼쪽으로 두칸 전 높이값을 최대값으로 설정
        height = buildings[i-2]
        # 내 위치에서 바로 왼쪽 건물에서 오른쪽으로 두 번째까지 확인하기
        for j in range(i-1, i+3):
            if i == j:             # 나를 나와 비교할 때는 패스
                continue
            # 최대값이 내 위치보다 낮을 때 최대값을 바꾸기
            if height < buildings[j]:
                height = buildings[j]
        # 내 높이가 구해 낸 최대값보다 크면 조망권 획득
        if buildings[i] > height:
            view_count += buildings[i] - height

    print(f'#{tc} {view_count}')

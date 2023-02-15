import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 색깔 좌표 갯수
    N = int(input())
    # 빨간색 좌표 리스트
    red_list = []
    # 파란색 좌표 리스트
    blue_list = []
    # 겹치는 좌표 갯수
    result = 0
    # 색깔 좌표 갯수 만큼 반복
    for _ in range(N):
        # 좌표(리스트)와 색깔을 저장
        *coordinate, color = list(map(int, input().split()))
        # 색깔이 레드(1)일 경우
        if color == 1:
            # 좌표 리스트에서 X의 최소값에서 최대값 + 1 까지 반복
            for x in range(coordinate[0], coordinate[2]+1):
                # 좌표 리스트에서 Y의 최소값에서 최대값 + 1 까지 반복
                for y in range(coordinate[1], coordinate[3] + 1):
                    # X, Y 값을 레드 리스트에 저장
                    red_list.append([x, y])
        # 색깔이 블루(2)일 경우
        else:
            # 좌표 리스트에서 X의 최소값에서 최대값 + 1 까지 반복
            for x in range(coordinate[0], coordinate[2]+1):
                # 좌표 리스트에서 Y의 최소값에서 최대값 + 1 까지 반복
                for y in range(coordinate[1], coordinate[3] + 1):
                    # X, Y 값을 블루 리스트에 저장
                    blue_list.append([x, y])

    # 레드 리스트와 블루 리스트를 탐색하여 같은 좌표가 있을 경우 result에 1씩 더한다.
    for red in red_list:
        # 중복되는 값이 있는지 체크하기 위해
        value_check = 0
        for blue in blue_list:
            if red == blue and value_check == 0:
                result += 1
                # 레드 리스트 값과 블루 리스트 값이 같을 경우 이후에 나오는 중복값을 무시하기 위해
                value_check = 1
    print(f'#{test_case} {result}')


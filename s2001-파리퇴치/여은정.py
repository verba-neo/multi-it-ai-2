import sys

sys.stdin = open('./input.txt')  # 읽어 오기


def fly_catch():
    t = int(input())  # 숫자로 데이터 인풋
    for tc in range(1, t + 1):

        N, M = map(int, input().split())

        # 2차원 배열 만들기 
        arr = [list(map(int, input().split())) for _ in range(N)]

        # 배열 정렬하기 
        # for i in range(0, N):
        #     # temp_arr = list(map(int, input().split()))
        #     arr[i] = list(map(int, input().split()))
        # # matrix= [list(map(int, input().split())) for _in range(N)]
        result = 0
        #최대 파리 수

        # m의 배열의 수 만큼 파리 잡고
        # for i in range(0, n):
        # for j, in range(i, i+m):
        #     if j < n:
        #         for k in range(k, k + 1):
        #             if k < n:
        #                 sum_value += arr[j][k]

        for j in range(N - M + 1):
            for i in range(N - M + 1):
                total = 0
                # M x M의 크기에 있는 파리 수 검사
                for y in range(j, j + M):
                    for x in range(i, i + M):
                        total += arr[y][x]
                # 현재 결과보다 큰 경우 저장
                if total > result:
                    result = total
        print('#{} {}'.format(tc, result))

        # print(f'#{tc} {sum_value}')


fly_catch()

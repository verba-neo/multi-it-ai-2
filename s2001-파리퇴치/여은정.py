import sys

sys.stdin = open('./input.txt')  # 읽어 오기


def flycatch():
    t = int(input())  # 숫자로 데이터 인풋
    for tc in range(1, t + 1):

        n, m = map(int, input().split())

        # 2차원 배열 만들기 
        arr = [[0 for j in range(n)] for i in range(n)]

        # 배열 정렬하기 
        for i in range(0, n):
            # temparr = list(map(int, input().split()))
            arr[i] = list(map(int, input().split()))
            
        sumValue = 0
        # m의 배열의 수 만큼 파리 잡고 
        for j in range(m - 1, 2 * m - 1):
            if (j < n):
                for k in range(m - 1, 2 * m - 1):
                    # print(f'[{j}][{k}]')
                    if (k < n):
                        # print(arr[j][k])
                        sumValue += arr[j][k]

        print(f'#{tc} {sumValue}')


flycatch()

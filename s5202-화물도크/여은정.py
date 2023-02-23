import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    N = int(input())
    result = []
    works = [tuple(map(int, input().split())) for _ in range(N)]  # (시작시간, 종료시간)
    # 끝나는 시간 기준 오름 차순으로 정렬
    works.sort(key=lambda x: x[1], reverse=True)
    result.append(works.pop())  # 첫 작업은 가장 빨리 끝나는 작업으로 할당

    while works:
        cur_end = result[-1][1]  # 할당된 작업의 끝나는 시간
        work = works.pop()       # 다음 작업 시간을 가져오기
        next_start = work[0]     # 다음 시작 시간 설정

        if cur_end <= next_start:  # 현재 끝나는 시간이 다음 시작 시간보다 작거나 같으면 할당
            result.append(work)

    print(f'#{test_case} {len(result)}')

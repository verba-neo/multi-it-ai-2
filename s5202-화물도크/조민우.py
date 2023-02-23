# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     working_time = [list(map(int, input().split())) for _ in range(N)]
#     working_time.sort(key = lambda x: x[1])
#     cnt = 0
#     finish = 0
#     for i in range(0,len(working_time)):
#         if working_time[i][0] >= finish:
#             cnt += 1
#             finish = working_time[i][1]
#     print(f'#{test_case} {cnt}')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
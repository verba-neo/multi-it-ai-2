import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    length, check = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_max = sum_min = now = 0
    for n in range(check):
        sum_max += numbers[n]
    sum_min = now = sum_max

    for n in range(check, length):
        now = now + numbers[n] - numbers[n - check]
        if now > sum_max:
            sum_max = now

        if now < sum_min:
            sum_min = now

    sol = sum_max - sum_min

    print(f'#{test_case} {sol}')


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    numbers = [int(n[0:1]) for n in input()]
    maximum = 0
    max_num = 0

    for i in range(10):
        if numbers.count(i) >= maximum:
            maximum = numbers.count(i)
            max_num = i

    print(f'#{test_case} {max_num} {maximum}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    width = N
    height = 20

    small_count = 0
    big_count = 0


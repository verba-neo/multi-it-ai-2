import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
   N, K = map(int, input().split())
   # N * N 행렬
   matrix = [list(map(int, input().split())) for i in range(N)]
   part_mat = git
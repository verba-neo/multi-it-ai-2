import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    h_buildings = list(map(int, input().split()))
    search = [-2, -1, 1, 2]
    count = 0
    for building_idx in range(len(h_buildings)):

        max_side = 0
        if building_idx == 0 or building_idx == 1 or building_idx == N - 2 or building_idx == N - 1:
            continue
        else:

            for search_num in search:
                if h_buildings[building_idx + search_num] > max_side:
                    max_side = h_buildings[building_idx + search_num]
            if max_side < h_buildings[building_idx]:
                count += h_buildings[building_idx] - max_side
            else:
                continue
    print(f'#{test_case} {count}')

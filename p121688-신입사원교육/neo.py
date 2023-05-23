from itertools import combinations


# dfs
def solution(ability, number):
    n = len(ability)
    minimum = float('INF')

    def dfs(x, arr):
        nonlocal minimum

        if x == number:
            total = sum(arr)
            if total < minimum:
                minimum = total
            return

        for case in combinations(range(n), 2):
            copy_arr = arr[:]
            p1, p2 = case
            copy_arr[p1] = copy_arr[p2] = copy_arr[p1] + copy_arr[p2]

            if sum(copy_arr) < minimum:
                dfs(x+1, copy_arr)

    dfs(0, ability)

    return minimum

# sort
def solution(ability, number):
    # number번 반복
    ability
    for _ in range(number):
        ability.sort()
        # 제일 능력치 안좋은 사람, 두번째로 안좋은 사람
        new_ability = ability[0] + ability[1]
        # 둘의 합으로 능력치 갱신
        ability[0] = ability[1] = new_ability

    return sum(ability)


# heap
import heapq

def solution(ability, number):
    # 기존 리스트를 (최소)힙으로 만들겠다.

    heapq.heapify(ability)  # O(n)

    # number 번 교육을 시작함
    for _ in range(number):
        # 최소힙에서 최소값 pop (가장 낮은 능력치)
        p1 = heapq.heappop(ability)  # O(log2n)
        # 최소힙에서 최소값 pop (그 다음으로 낮은 능력치)
        p2 = heapq.heappop(ability)  # O(log2n)
        p3 = p1 + p2
        heapq.heappush(ability, p3)  # O(log2n)
        heapq.heappush(ability, p3)  # O(log2n)

    return sum(ability)


print(solution([10, 3, 7, 2], 2))
print(solution([1, 2, 3, 4], 3))

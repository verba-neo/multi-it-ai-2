import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    charge_location = list(map(int, input().split()))
    # print(charge_location)
    bus = [0]
    next_bus = 0
    charge_count = 0
    while next_bus < n:
        next_bus = bus[-1] + k
        charge_count = 0
        for _ in range(bus[-1] + k, bus[-1], -1):
            if (next_bus in charge_location) and charge_count == 0:
                bus.append(next_bus)
                charge_count = 1
            if next_bus not in charge_location:
                next_bus -= 1
            if _ == bus[-1] + 1 :
                next_bus = n
                bus = [0]
        next_bus = next_bus + k

    print("#{} {}".format(test_case, len(bus) - 1))


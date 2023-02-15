import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    battery, total_len, charge = map(int, input().split())
    charge_list = list(map(int, input().split()))
    charge_list.reverse()
    charge_list.append(0)
    charged = 0
    back = total_len
    before = 0
    for i in range(charge + 1):
        distance = back - charge_list[i]

        if distance > battery:
            charged = 0
            break

        if before + distance <= battery:
            charged -= 1

        else:
            before = 0

        back = charge_list[i]
        charged += 1
        before += distance

    print(f'#{test_case} {charged}')

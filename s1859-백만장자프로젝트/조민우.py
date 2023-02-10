import sys
sys.stdin = open("input.txt", "r")

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sell_price = 0
    last_day = numbers[-1]
    for i in range(len(numbers)-1, -1, -1):
        if last_day > numbers[i]:
            sell_price += last_day - numbers[i]
        else:
            last_day = numbers[i]
print(f'#{tc} {sell_price}')
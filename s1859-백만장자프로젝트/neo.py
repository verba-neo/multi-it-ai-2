import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    max_price = 0

    # 미래 부터 현재 까지 가격 확인
    for idx in range(N-1, -1, -1):
        # 지금 보고 있는 가격
        price = prices[idx]
        
        # 지금 가격이 미래 가격보다 싸니까 무조건 삼 
        # 미래 최대가격에서 현재 구매가격 뺀 값이 수익
        if price > max_price:
            # 팔아야 하는 가격
            max_price = price
        else:
            profit = max_price - price
            total += profit

    print(f'#{tc} {total}')

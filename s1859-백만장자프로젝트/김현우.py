def max_profit(n, prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

t = int(input().strip())
for i in range(1, t + 1):
    n = int(input().strip())
    prices = list(map(int, input().strip().split()))
    result = max_profit(n, prices)
    print(f"#{i} {result}")
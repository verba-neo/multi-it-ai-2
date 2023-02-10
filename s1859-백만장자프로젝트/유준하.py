
testcase = int(input())  # 테스트 케이스 입력
while testcase > 0:
    number = int(input())   # 테스트 케이스 별 자연수 N 입력
    prices = list(map(int, input().split()))  # 자연수 만큼의 가격 입력 받기
    maxprice = max(prices)  # 가격 리스트 최대값 찾기
    maxprice_index = prices.index(max(prices))  # 최대값 인덱스
    costprice = 0
    item = 0
    profit = 0
    # 최대값 인덱스가 0일 경우는 0 출력
    if maxprice_index == 0:
        profit = 0
        print(f"#{testcase} {profit}")
    else:
        # 우선 최대값 인덱스까지는 profit을 그대로 연산
        for i in range(0, maxprice_index):
            profit += maxprice - prices[i]
        # 최대값 인덱스가 마지막이 아니라 중간에 껴있는 경우에 대한 처리
        if maxprice_index < len(prices):
            maxprice = prices[-1]  #최대값을 마지막값으로 변경
            for i in range(maxprice_index+1, len(prices)):
                if prices[i] >= maxprice:
                    maxprice = prices[i]
                else:
                    profit += maxprice - prices[i]
        print(f"#{testcase} {profit}")











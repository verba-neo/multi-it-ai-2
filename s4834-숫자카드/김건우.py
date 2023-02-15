import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):

    N = int(input())  # 카드 장수

    # 카드 종류
    # card = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 카드 개수 초기화
    card_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    card_num = input()  # N개의 숫자

    # 카드 소트
    card_num_list = list(map(int, card_num))
    card_num_list.sort()

    # unique_card
    unique_card = set(card_num_list)

    # 각 카드가 몇 장인지 센다.
    for i in unique_card:
        for num in card_num_list:
            # unique_card 와 소트된 카드 리스트를 비교하여
            # 카드가 발견되면 카드 갯수(card_count)에 1을 추가한다.
            if i == num:
                card_count[i] += 1

    # 가장 많은 카드 장수
    max_card_count = max(card_count)

    # 가장 많은 카드
    max_cards = []
    for i in range(10):
        if max_card_count == card_count[i]:
            max_cards.append(i)

    # 가장 많은 카드 중에 숫자가 가장 큰 것
    max_card = max(max_cards)

    print(f'#{test_case} {max_card} {max_card_count}')
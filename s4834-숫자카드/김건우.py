import sys

sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):

    N = int(input())  # 카드 장수

    # 카드 종류 : 실제 코드에서 쓰지 않고, 대신 card_count의 index를 활용한다.
    # card =     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 각 번호 별 카드 갯수
    card_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # N개의 숫자 (49679)
    card_num_list = list(map(int, input()))
    # 소트 (46799)
    card_num_list.sort()

    # unique_card (4679)
    unique_card = set(card_num_list)

    # 1. 각 카드가 몇 장인지 센다.
    for i in unique_card:
        for num in card_num_list:
            # unique_card 와 소트된 카드 리스트를 비교하여
            # 카드가 발견되면 카드 갯수(card_count)에 1을 추가한다.
            if i == num:
                card_count[i] += 1
    #                	[ 4 9 6 7 9 ]
    # 가장 많은 카드 장수	[ 1 1 1 1 2 ]
    max_card_count = max(card_count)

    # [ 0 8 2 7 1 ]
    # [ 1 1 1 1 1 ]

    # 2. 가장 많은 카드 장수에 해당하는 숫자들
    max_cards = []
    for i in range(10):
        #  가장 많은 카드 갯수(1) ==  카드 갯수(1)
        if max_card_count == card_count[i]:
            # index를 카드번호로 저장
            max_cards.append(i)

    # 3. 가장 많은 카드 중에 숫자가 가장 큰 것
    max_card = max(max_cards)
    # T(테스트 케이스 번호),  가장 많은 카드의 숫자,  가장 많은 카드의 장 수
    print(f'#{test_case} {max_card} {max_card_count}')
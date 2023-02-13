import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input().split()
    puzzle = []
    # 단어의 길이
    word_len = int(N[1])
    # 퍼즐의 길이
    puzzle_len = int(N[0])
    for list_num in range(0, puzzle_len):
        puzzle.append(list(map(int, input().split())))

    zero_or_one_count = 0
    search_word = 0
    for line in range(0, puzzle_len):
        for column in range(0, puzzle_len):
            if puzzle[line][column] == 1:
                zero_or_one_count += 1
            else:
                if zero_or_one_count == word_len:
                    search_word += 1
                zero_or_one_count = 0
        if zero_or_one_count == word_len:
            search_word += 1
        zero_or_one_count = 0

    for column in range(0, puzzle_len):
        for line in range(0, puzzle_len):
            if puzzle[line][column] == 1:
                zero_or_one_count += 1
            else:
                if zero_or_one_count == word_len:
                    search_word += 1
                zero_or_one_count = 0
        if zero_or_one_count == word_len:
            search_word += 1
        zero_or_one_count = 0

    print(f'#{tc} {search_word}')



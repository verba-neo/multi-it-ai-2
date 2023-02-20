import sys

sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T + 1):
    txt = input()
    check_list =[]
    loc = 0
    for check_txt in txt:
        if check_txt == '(':
            check_list.append(check_txt)
            loc += 1
        elif check_txt == '{':
            check_list.append(check_txt)
            loc += 1
        elif check_txt == ')':
            if check_list[-1] == '(':
                check_list.pop()
                loc -= 1
        elif check_txt == '}':
            if check_list[-1] == '{':
                check_list.pop()
                loc -= 1

    if loc == 0:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')


# 10 개중 8 개
# for test_case in range(1, T + 1):
#     txt = input()
#     check_dict = {'()': 0, '{}': 0}
#     chck_list =[]
#     for check_txt in txt:
#         if check_txt == '(':
#             chck_list.append(check_txt)
#             check_dict["()"] += 1
#
#         elif check_txt == '{':
#             check_dict["{}"] += 1
#             chck_list.append(check_txt)
#         elif check_txt == '}':
#             if chck_list[-1] == '{':
#                 check_dict["{}"] -= 1
#         elif check_txt == ')':
#             if chck_list[-1] == '(':
#                 check_dict["()"] -= 1
#
#     if check_dict["()"]== 0 and check_dict["{}"] == 0:
#         print(f'#{test_case} {1}')
#     else:
#         print(f'#{test_case} {0}')

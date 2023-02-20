import sys

sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T + 1):
    txt = input()
    # 괄호 입력받는 리스트
    check_list =[]
    # 입력받은 괄호의 위치
    loc = 0
    for check_txt in txt:
        if check_txt == '(' or check_txt == '{':
            check_list.append(check_txt)
        elif check_txt == ')' or check_txt == '}':
            if check_txt == ')' and check_list.pop() != '(':
                loc += 1
            elif check_txt == '}' and check_list.pop() != '{':
                loc += 1
    if loc == 0 and check_list:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {1}')


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

def solution(id_list, report, k):
    a = dict() #신고된 횟수
    b = dict() #누가 누구를 신고했는지
    result = []
    list_num = 0
    for i in id_list:
        a[i] = 0
        b[i] = []
        result.append(0)
    check = 0
    for i in report:
        for x in b[i.split()[0]]:
            if x == i.split()[1]:
                check += 1
        if check == 0:
            b[i.split()[0]].append(i.split()[1])
            a[i.split()[1]] += 1
        check = 0

    for i in b:

        for x in b[i]:
            if a[x] >= k:
                result[list_num] += 1
        list_num += 1
    return result
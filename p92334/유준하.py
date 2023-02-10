from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    user = defaultdict(set)
    reported = defaultdict(int)
    reportc= list(set(report))
    for item in reportc:
        nid, rid = item.split(' ')
        user[nid].add(rid)
        reported[rid] += 1

    for i in id_list:
        result=0
        for j in user[i]:
            if reported[j] >= k:
                result += 1
        answer.append(result)

    return answer


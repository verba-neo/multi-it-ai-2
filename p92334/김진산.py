def solution(id_list, report, k):
    answer = [0 i for i in range(len(id_list))]
    # 신고횟수
    report_count = {}
    # 신고내역
    report_history = {}
    # 각각 딕셔너리에 키값 하고 값 넣기
    for user_id in id_list:
        report_count[user_id] = 0
        report_history[user_id] = []

    # 신고 내역 추가/ 신고 횟수 누적
    for report_process in report:
        post_user, receive_user = report_process.split()

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
               2))

print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))
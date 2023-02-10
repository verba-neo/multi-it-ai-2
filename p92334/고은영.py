# def solution(id_list, report, k):
#     s1 = [i.split()[1] for i in set(report)] #중복없는 리스트 뽑아서 신고당한 사람 뽑기
#     print(s1)
#     s2 = [i for i in set(s1) if s1.count(i) >= k] # s1에서 카운트해서 k번이상이면 추출하기
#     print(s2)
#     s3 = [i.split()[0] for i in set(report) if i.split()[1] in s2] #중복없는 리스트에서 신고당한사람이 s2애 존재하면 신고자 추출
#     print(s3) # k번 이상 신고당한 사람의 신고자들
#     return [s3.count(i) for i in id_list] # s2메일발송대상 신고한 횟수


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
#print((report)[0].split(' ')[0])

# for index, j in enumerate(id_list):
#     print(index, j)

a =[]
for i in set(report):
    a.append(i.split(' ')[1]) #신고자 내역들
print(a)
for j in id_list:
    if a.count(j) >=2: #무지가 a 몇번있니
        answer.append(j) #2번이상 신고당한사람 추출
        print(answer)


# # [2,1,1,0]
# print(solution(
#                 ["muzi", "frodo", "apeach", "neo"]
#                ,["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
#                ,2))
# # [0,0]
# print(solution(
#             ["con", "ryan"]
#         ,["ryan con", "ryan con", "ryan con", "ryan con"]
#         ,3))
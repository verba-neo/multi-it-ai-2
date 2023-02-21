import itertools
def solution(k, dungeons):
    answer = []

    nPr = itertools.permutations(dungeons,len(dungeons))
    for i in nPr:
        fatigue = k
        count = 0
        for essential, consume in i:
           if fatigue >= essential:
               fatigue -= consume
               count += 1


        answer.append(count)
    return max(answer)



print(solution(80,[[80,20],[50,40],[30,10]]))
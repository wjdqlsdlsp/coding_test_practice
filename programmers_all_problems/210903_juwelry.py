# 다른사람 코드 참고
def solution(gems):
    dict = {gems[0]:1}
    need_gem = len(set(gems))
    answer = [0,len(gems)-1]
    start, end = 0, 0
    while True:
        if need_gem == len(dict.keys()):
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if dict[gems[start]] == 1:
                del dict[gems[start]]
            else:
                dict[gems[start]] -=1
            start +=1
        else:
            end +=1
            if end == len(gems):
                break
            if gems[end] in dict.keys():
                dict[gems[end]]+=1
            else:
                dict[gems[end]]=1

    return [answer[0]+1, answer[1]+1 ]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

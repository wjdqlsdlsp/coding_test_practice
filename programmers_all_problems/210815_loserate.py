def solution(N, stages):
    now_stage = [0 for _ in range(N+1)]
    for stage in stages:
        now_stage[stage-1] +=1
    lose_rate = {}
    for i in range(len(now_stage)-1):
        if sum(now_stage[i:]) ==0: lose_rate[i+1] =0
        else: lose_rate[i+1]= now_stage[i]/sum(now_stage[i:])
    lose_rate = sorted(lose_rate.items(), key = lambda x : x[1], reverse=True)
    return list(map(lambda x: x[0], lose_rate))

print(solution(5, [2, 1, 2, 4, 2, 4, 3, 3]))
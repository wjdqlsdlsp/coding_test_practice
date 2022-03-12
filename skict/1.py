def solution(money, costs):
    costs_list = [5, 10, 50, 100, 500]
    dp = [costs[0]*i for i in range(money+1)]

    for index, v in enumerate(costs_list,1):
        for j in range(money+1):
            if j + v < money+1:
                dp[j+v] = min(dp[j+v], dp[j]+ costs[index]) 
    return dp[money]

print(solution(4578, [1,4,99,35,50,1000]))
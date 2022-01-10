# 시간초과
# import copy
# count = 0
# def DFS(n, money):
#     global count
#     if n == 0:
#         count+=1
#         return

#     if money:
#         pop_num = money.pop()
#         max_num = n//pop_num

#         for i in range(max_num+1):
#             tmp = copy.copy(money)
#             DFS(n-pop_num*i,tmp)

# def solution(n, money):
#     money.sort()
#     pop_num = money.pop()
#     max_num = n//pop_num
    
#     for i in range(max_num+1):
#         tmp = copy.copy(money)
#         DFS(n-pop_num*i, tmp)

#     return count

# 다른사람 풀이
def solution(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price-coin]
        print(dp)
    return dp[n]

print(solution(5, [1,2,5]))
def solution(price, money, count):
    return max(0, sum(list(map(lambda x : x * price, list(range(1,count+1)))))-money)
print(solution(3, 20, 4))
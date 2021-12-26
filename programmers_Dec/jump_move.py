def solution(n):
    ans = 0
    s = bin(n)[2:]
    for i in s:
        if i == '1':
            ans+=1
    return ans

print(solution(5))
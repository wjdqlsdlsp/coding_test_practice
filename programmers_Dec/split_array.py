def solution(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]

# 시간초과 코드
# def solution(n, left, right):
#     arr = [[max((j+1),(i+1)) for j in range(n)] for i in range(n)]
#     t = []
#     for i in arr:
#         t+=i
#     return t[left:right+1]


print(solution(3,2,5))
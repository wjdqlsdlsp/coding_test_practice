def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    s = ''
    while n:
        n, r = divmod(n, k)
        s+= str(r)
    s = s[::-1]
    s = s.split('0')
    s = [*filter(lambda x : x!='', s)]
    for i in s:
        if isprime(int(i)):
            answer +=1
    return answer

print(solution(437674, 3))
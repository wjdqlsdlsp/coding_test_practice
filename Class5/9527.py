import sys
s, e = map(int, sys.stdin.readline().split())

def func(n):
    count = 0
    k = 0
    while 2**k <=n:
        p = 2**(k+1)
        p_count = (n+1)//p

        count += p_count *(p//2)
        left = (n+1)%p
        count += max(0, left-p//2)
        k+=1
    return count

print(func(e) - func(s-1))
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]


l, r = 0,0
sum_all = 0
min_len = sys.maxsize


while 1:
    if sum_all >= m:
        min_len = min(min_len, r-l)
        sum_all -= arr[l]
        l +=1
    elif r == n:
        break
    else:
        sum_all += arr[r]
        r +=1

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)
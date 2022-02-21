import sys

page_n = int(sys.stdin.readline())

point = 1
arr = [0 for i in range(10)]

while page_n != 0:
    while page_n % 10 != 9:
        for i in str(page_n):
            arr[int(i)] += point
        page_n -=1
    
    if page_n < 10:
        for i in range(page_n+1):
            arr[i] += point
        arr[0] -= point
        break

    else:
        arr = [*map(lambda x : x + (page_n // 10 + 1)* point, arr)]
    
    arr[0] -= point
    point *= 10
    page_n //= 10

print(" ".join(map(str,arr)))

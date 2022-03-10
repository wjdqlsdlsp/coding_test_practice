import sys
while True:
    tmp = [*map(int, sys.stdin.readline().split())]
    if tmp[0] == 0:
        break
    n = tmp[0]
    arr = tmp[1:]
    max_size = 0
    s = []
    for i in range(n):
        while len(s) != 0 and arr[s[-1]] > arr[i]:
            tmp = s.pop()
            if len(s) == 0:
                width = i
            else:
                width = i - s[-1] -1
            max_size = max(max_size, width * arr[tmp])
        s.append(i)

    while s:
        tmp = s.pop()
        if len(s) == 0:
            width= n
        else:
            width = n - s[-1] -1
        max_size = max(max_size, width * arr[tmp])
    print(max_size)

from collections import deque
def solution(n):
    arr = deque([])
    while n >=3:
        n, b = divmod(n, 3)
        arr.appendleft(b)
    arr.appendleft(n)
    for i in range(len(arr)-1, 0, -1):
        if arr[i] <= 0:
            arr[i-1] -=1
            arr[i] = 4 +arr[i]
            if arr[i] == 3:
                arr[i] =2

    arr = list(map(lambda x : str(x), arr))
    return str(int("".join(arr)))

for i in range(1,15):
    print(i, " : " ,solution(i))
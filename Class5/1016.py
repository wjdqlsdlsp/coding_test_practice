import sys

# min_num, max_num = map(int, sys.stdin.readline().split())
min_num, max_num = 1, 10
count = 0
i = 2

arr = [True for i in range(max_num - min_num + 1)]

while i**2 <= max_num:
    s = min_num // i**2

    while s * (i**2) <= max_num:
        if s * (i**2) >= min_num and s * (i**2) <= max_num:
            arr[s * (i**2) -min_num] = 0
        s +=1
    i+1

print(sum(arr))
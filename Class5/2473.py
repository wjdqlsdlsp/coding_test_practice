import sys

N = int(sys.stdin.readline())
arr = [*map(int, sys.stdin.readline().split())]

arr.sort()
result = sys.maxsize
my_result = [arr[0], arr[1], arr[2]]
while len(arr) > 3:
    pop_num = arr.pop()
    l, r = 0, len(arr)-1
    while l < r:
        check = arr[l] +arr[r] + pop_num
        if result > abs(check):
            result = abs(check)
            my_result = [arr[l], arr[r], pop_num]
        if check == 0:
            break
        elif check > 0:
            r-=1
        else:
            l+=1

if len(arr) == 3 and abs(arr[0] + arr[1] + arr[2]) < result:
    my_result = arr

for i in my_result:
    print(i, end=" ")
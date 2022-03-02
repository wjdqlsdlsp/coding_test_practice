import sys

N = int(sys.stdin.readline())

arr = [*map(int, sys.stdin.readline().split())]

l, r =0, N-1


result = abs(arr[l] + arr[r])
result_input = [l,r]

if result == 0:
    print(arr[l], arr[r])
else:
    while l < r:
        if result > abs(arr[l] + arr[r]):
            result = abs(arr[l] + arr[r])
            result_input = [l, r]
        if arr[l] + arr[r] == 0:
            result_input = [l, r]
            break
        elif arr[l] + arr[r] > 0:
            r-=1
        else:
            l+=1
    
    print(arr[result_input[0]], arr[result_input[1]])
